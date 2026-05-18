// Final stabilized App entry point
import React, { useState, useEffect } from 'react';
import { useAuth, AuthProvider } from './context/AuthContext';
import { useEducation, Course, Badge } from './hooks/useEducation';
import { AuthEntrance } from './components/AuthEntrance';
import { ProfileSetupFlow } from './components/ProfileSetupFlow';
import { Dashboard } from './components/Dashboard';
import { CourseView } from './components/CourseView';
import { TeacherAlertHub } from './components/TeacherAlertHub';
import { ErrorBoundary } from './components/ErrorBoundary';
import { 
  LayoutDashboard, 
  User, 
  LogOut, 
  Sparkles, 
  Menu, 
  X,
  Database
} from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';

const AppContent = () => {
  const { user, profile, signOutUser } = useAuth();
  const { seedData, getProgress, getBadges } = useEducation();
  const [view, setView] = useState<'dashboard' | 'learning' | 'teacher-console'>('dashboard');
  const [selectedCourse, setSelectedCourse] = useState<Course | null>(null);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [overallProgress, setOverallProgress] = useState<Record<string, number>>({});
  const [badges, setBadges] = useState<Badge[]>([]);

  useEffect(() => {
    if (!profile) return;
    const unsubProgress = getProgress(profile.uid, (p) => {
      const pMap: Record<string, number> = {};
      p.forEach(item => {
        if (!pMap[item.courseId]) pMap[item.courseId] = 0;
        if (item.status === 'completed') pMap[item.courseId] += 1;
      });
      setOverallProgress(pMap);
    });

    const unsubBadges = getBadges(profile.uid, setBadges);

    return () => {
      unsubProgress();
      unsubBadges();
    };
  }, [profile, getProgress, getBadges]);

  useEffect(() => {
    if (!profile || !selectedCourse) return;
    if (selectedCourse.syllabusId !== profile.syllabus || selectedCourse.grade !== profile.grade) {
      setSelectedCourse(null);
    }
  }, [profile, selectedCourse]);

  if (!user) return <AuthEntrance />;
  if (profile && (!profile.grade || !profile.syllabus)) return <ProfileSetupFlow />;

  return (
    <div className="min-h-screen bg-[#f8fafc] flex">
      {/* Sidebar Navigation */}
      <aside className={`fixed inset-y-0 left-0 z-50 w-72 bg-slate-900 text-white transform transition-transform duration-300 lg:translate-x-0 lg:static ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'}`}>
        <div className="p-8 flex flex-col h-full">
           <div className="flex items-center gap-3 mb-12">
              <img src="/logo-purple.png" alt="Learn Boost Logo" className="w-12 h-12 object-contain" />
              <h1 className="text-2xl font-black italic tracking-tighter uppercase">Learn Boost</h1>
           </div>

           <nav className="flex-1 space-y-2">
              {[
                { id: 'dashboard', icon: LayoutDashboard, label: 'Learning Path' },
                ...(profile?.role === 'teacher' ? [{ id: 'teacher-console', icon: Database, label: 'Teacher Hub' }] : [])
              ].map(item => (
                <button 
                  key={item.id}
                  onClick={() => { setView(item.id as any); setIsSidebarOpen(false); setSelectedCourse(null); }}
                  className={`w-full flex items-center gap-4 px-4 py-4 rounded-2xl font-black text-[10px] uppercase tracking-widest transition-all ${
                    view === item.id ? 'bg-indigo-600 text-white shadow-xl shadow-indigo-900/20' : 'text-slate-400 hover:bg-white/5 hover:text-white'
                  }`}
                >
                   <item.icon className="w-5 h-5" />
                   {item.label}
                </button>
              ))}
           </nav>

           <div className="pt-8 border-t border-white/5 space-y-6">
              <div className="flex items-center gap-4 px-2">
                 <div className="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center border border-white/10">
                    <User className="w-5 h-5 text-indigo-400" />
                 </div>
                 <div className="overflow-hidden">
                    <p className="text-xs font-black truncate uppercase tracking-tighter">{profile?.name}</p>
                    <p className="text-[8px] font-bold text-slate-500 uppercase tracking-widest">{profile?.role}</p>
                 </div>
              </div>
              <button 
                onClick={() => signOutUser()}
                className="w-full flex items-center gap-4 px-4 py-4 rounded-2xl font-black text-[10px] uppercase tracking-widest text-rose-400 hover:bg-rose-500/10 transition-all"
              >
                 <LogOut className="w-5 h-5" />
                 Secure Sign Out
              </button>
           </div>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col h-screen overflow-hidden">
         {/* Mobile Header */}
         <header className="lg:hidden h-16 bg-white border-b border-slate-200 flex items-center justify-between px-6 shrink-0">
            <div className="flex items-center gap-2">
               <img src="/logo-purple.png" alt="Learn Boost Logo" className="w-8 h-8 object-contain" />
               <h1 className="text-lg font-black italic tracking-tighter uppercase text-slate-900">Learn Boost</h1>
            </div>
            <button onClick={() => setIsSidebarOpen(true)} className="p-2 text-slate-900">
               <Menu className="w-6 h-6" />
            </button>
         </header>

         <div className="flex-1 overflow-y-auto">
            <AnimatePresence mode="wait">
               {selectedCourse ? (
                 <motion.div 
                   key="course-view"
                   initial={{ opacity: 0, y: 10 }}
                   animate={{ opacity: 1, y: 0 }}
                   exit={{ opacity: 0, y: -10 }}
                   className="h-full"
                 >
                    <CourseView 
                      course={selectedCourse} 
                      onBack={() => setSelectedCourse(null)} 
                    />
                 </motion.div>
               ) : view === 'dashboard' ? (
                 <motion.div 
                   key="dashboard"
                   initial={{ opacity: 0 }}
                   animate={{ opacity: 1 }}
                   exit={{ opacity: 0 }}
                 >
                    <Dashboard 
                      onSelectCourse={setSelectedCourse} 
                      overallProgress={overallProgress}
                      badges={badges}
                      onSeed={seedData}
                    />
                 </motion.div>
               ) : (
                 <motion.div 
                   key="teacher-console"
                   className="p-12 max-w-4xl mx-auto"
                 >
                    <TeacherAlertHub />
                    <div className="bg-white rounded-[40px] p-10 border border-slate-100 shadow-xl shadow-indigo-100/20">
                       <h2 className="text-2xl font-black text-slate-900 uppercase italic mb-8 underline decoration-8 decoration-indigo-100 underline-offset-4">Teacher Console</h2>
                       <p className="text-slate-400 font-medium mb-12">Select a curriculum module from the sidebar to review student submissions and provide feedback.</p>
                       <div className="grid grid-cols-1 md:grid-cols-2 gap-6 opacity-30 pointer-events-none">
                          <div className="p-8 border-2 border-dashed border-slate-200 rounded-3xl flex flex-col items-center justify-center text-center">
                             <Sparkles className="w-12 h-12 mb-4" />
                             <p className="text-[10px] font-black uppercase tracking-widest">Student Analytics</p>
                          </div>
                          <div className="p-8 border-2 border-dashed border-slate-200 rounded-3xl flex flex-col items-center justify-center text-center">
                             <Database className="w-12 h-12 mb-4" />
                             <p className="text-[10px] font-black uppercase tracking-widest">Class Management</p>
                          </div>
                       </div>
                    </div>
                 </motion.div>
               )}
            </AnimatePresence>
         </div>
      </main>

      {/* Overlay for mobile sidebar */}
      {isSidebarOpen && (
        <div 
          className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-40 lg:hidden"
          onClick={() => setIsSidebarOpen(false)}
        />
      )}
    </div>
  );
};

const App = () => {
  return (
    <ErrorBoundary>
      <AuthProvider>
        <AppContent />
      </AuthProvider>
    </ErrorBoundary>
  );
};

export default App;
