import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import html2canvas from 'html2canvas';
import { jsPDF } from 'jspdf';
import { useAuth } from '../context/AuthContext';
import { useEducation, Course, Module } from '../hooks/useEducation';
import { getStudyMaterialPath } from '../data/formulaCurriculum';
import { LessonPlayer } from './LessonPlayer';
import { QuizView } from './QuizView';
import { ForumView } from './ForumView';
import { TeacherReview } from './TeacherReview';
import { LearnBoostMascot } from './LearnBoostMascot';
import { 
  ChevronRight, 
  BookOpen, 
  HelpCircle, 
  MessageCircle, 
  FileText, 
  Check, 
  Zap, 
  Send,
  Map as MapIcon,
  Flag,
  Award,
  Target,
  ShieldCheck,
  UnlockKeyhole
} from 'lucide-react';

const SyllabusRoadmap = ({ modules, progress, onSelect, moduleDescriptions }: { modules: Module[], progress: Record<string, string>, onSelect: (m: Module) => void, moduleDescriptions: Record<string, string> }) => {
  return (
    <div className="py-12 px-6 max-w-2xl mx-auto">
      <div className="relative flex flex-col items-center gap-16">
        <div className="absolute top-0 bottom-0 w-2 bg-slate-200 rounded-full left-1/2 -translate-x-1/2 -z-10" />
        
        {modules.map((m, idx) => {
          const isCompleted = progress[m.id] === 'completed';
          const isInProgress = progress[m.id] === 'in-progress';
          
          return (
            <motion.div 
              key={m.id}
              initial={{ opacity: 0, x: idx % 2 === 0 ? -20 : 20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              className={`relative flex items-center w-full ${idx % 2 === 0 ? 'flex-row' : 'flex-row-reverse'}`}
            >
              <div className={`w-1/2 flex ${idx % 2 === 0 ? 'justify-end pr-10' : 'justify-start pl-10'}`}>
                <button 
                  onClick={() => onSelect(m)}
                  className={`p-6 rounded-[32px] border-2 transition-all text-left max-w-xs group shadow-lg ${
                    isCompleted 
                      ? 'bg-emerald-50 border-emerald-200 text-emerald-900 shadow-emerald-100/50' 
                      : isInProgress
                        ? 'bg-indigo-50 border-indigo-200 text-indigo-900 shadow-indigo-100/50'
                        : 'bg-white border-slate-100 text-slate-600 hover:border-indigo-300 shadow-slate-100/50'
                  }`}
                >
                  <p className="text-[10px] font-black uppercase tracking-widest opacity-50 mb-1">Step {idx + 1}</p>
                  <h4 className="text-sm font-black uppercase leading-tight mb-2">{m.title}</h4>
                  <p className="text-[10px] font-medium text-slate-500 line-clamp-2 mt-2">Overview: {moduleDescriptions[m.id] || `Explore key concepts in ${m.title}. Focus on understanding core principles.`}</p>
                  <div className="flex items-center gap-2 mt-4">
                    <span className={`text-[8px] font-bold uppercase px-2 py-0.5 rounded-full ${
                       isCompleted ? 'bg-emerald-200 text-emerald-700' : isInProgress ? 'bg-indigo-200 text-indigo-700' : 'bg-indigo-100 text-indigo-600'
                    }`}>
                      {isCompleted ? 'Mastered' : isInProgress ? 'In Progress' : 'Ready'}
                    </span>
                  </div>
                </button>
              </div>

              <div className={`absolute left-1/2 -translate-x-1/2 w-12 h-12 rounded-2xl flex items-center justify-center border-4 border-white shadow-xl transition-all ${
                isCompleted ? 'bg-emerald-500' : isInProgress ? 'bg-indigo-500 animate-pulse' : 'bg-slate-200'
              }`}>
                {isCompleted ? <Check className="w-6 h-6 text-white" /> : <Flag className="w-6 h-6 text-white" />}
              </div>
            </motion.div>
          );
        })}

        <div className="w-24 h-24 bg-slate-900 rounded-[40px] flex items-center justify-center border-b-[8px] border-slate-950 shadow-2xl mt-8">
           <Award className="w-12 h-12 text-amber-400" />
        </div>
      </div>
    </div>
  );
};

export const CourseView = ({ course, onBack }: { course: Course, onBack: () => void }) => {
  const { profile } = useAuth();
  const { getModules, updateProgress, getProgress, sendInteraction, getInteractions } = useEducation();
  const [modules, setModules] = useState<Module[]>([]);
  const [selectedModule, setSelectedModule] = useState<Module | null>(null);
  const [progress, setProgress] = useState<Record<string, string>>({});
  const [messages, setMessages] = useState<any[]>([]);
  const [newMessage, setNewMessage] = useState('');
  const [activeTab, setActiveTab] = useState<'lessons' | 'roadmap' | 'quizzes' | 'forum' | 'review'>('lessons');
  const [isDownloading, setIsDownloading] = useState(false);
  const [isMarkingDone, setIsMarkingDone] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [permissionRequest, setPermissionRequest] = useState<{ module: Module, targetTab: 'lessons' | 'quizzes' } | null>(null);
  const [moduleDescriptions, setModuleDescriptions] = useState<Record<string, string>>({});
  const [isFullscreen, setIsFullscreen] = useState(false);
  const contentRef = useRef<HTMLDivElement>(null);
  const isCourseInProfileScope = course.syllabusId === profile?.syllabus && course.grade === profile?.grade;
  const studyMaterialPath = getStudyMaterialPath(course.syllabusId, course.grade);

  useEffect(() => {
    const handleFullscreenChange = () => {
      setIsFullscreen(!!document.fullscreenElement);
    };
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', handleFullscreenChange);
  }, []);

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => console.error(`Error attempting to enable full-screen mode: ${err.message}`));
    } else {
      document.exitFullscreen();
    }
  };

  useEffect(() => {
    if (modules.length > 0) {
      const descriptions: Record<string, string> = {};
      modules.forEach(m => {
        descriptions[m.id] = m.explanation || `Explore key concepts in ${m.title}. Focus on understanding core principles and applying formulas to master this topic.`;
      });
      setModuleDescriptions(descriptions);
    }
  }, [modules]);

  useEffect(() => {
    if (!profile || !isCourseInProfileScope) return;
    const unsubModules = getModules(course.id, setModules);
    const unsubProgress = getProgress(profile.uid, (p) => {
      const map: Record<string, string> = {};
      p
        .filter(item => item.courseId === course.id)
        .forEach(item => map[item.moduleId] = item.status);
      setProgress(map);
    });
    const unsubMessages = getInteractions(course.id, setMessages);

    return () => {
      unsubModules();
      unsubProgress();
      unsubMessages();
    };
  }, [course.id, profile, isCourseInProfileScope, getModules, getProgress, getInteractions]);

  const handleSendMessage = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newMessage.trim()) return;
    sendInteraction(course, newMessage);
    setNewMessage('');
  };

  const handleModuleProgress = (module: Module, status: 'completed' | 'in-progress') => {
    setProgress(prev => {
      // Always update local state immediately
      return { ...prev, [module.id]: status };
    });
    updateProgress(course.id, module.id, status, { moduleTitle: module.title });
  };

  const requestModuleOpen = (module: Module, targetTab: 'lessons' | 'quizzes' = 'lessons') => {
    setPermissionRequest({ module, targetTab });
  };

  const acceptModuleOpen = () => {
    if (!permissionRequest) return;
    setSelectedModule(permissionRequest.module);
    setActiveTab(permissionRequest.targetTab);
    setPermissionRequest(null);
  };

  const markCourseDone = async () => {
    if (modules.length === 0 || isMarkingDone) return;
    setIsMarkingDone(true);
    setError(null);
    try {
      setProgress(prev => {
        const next = { ...prev };
        modules.forEach(module => {
          next[module.id] = 'completed';
        });
        return next;
      });
      await Promise.all(
        modules.map(module => updateProgress(course.id, module.id, 'completed', { moduleTitle: module.title }))
      );
    } catch (err) {
      console.error('Marking course done failed:', err);
      setError('Could not update course progress. Please try again.');
    } finally {
      setIsMarkingDone(false);
    }
  };

  const calculateProgress = () => {
    if (modules.length === 0) return 0;
    const progressUnits = modules.reduce((total, module) => {
      const status = progress[module.id];
      if (status === 'completed') return total + 1;
      if (status === 'in-progress') return total + 0.5;
      return total;
    }, 0);
    return Math.round((progressUnits / modules.length) * 100);
  };

  const downloadPDF = async () => {
    if (!contentRef.current || !selectedModule) return;
    setIsDownloading(true);
    try {
      const element = contentRef.current;
      const canvas = await html2canvas(element, {
        scale: 2,
        useCORS: true,
        logging: false,
        backgroundColor: '#ffffff'
      });
      const imgData = canvas.toDataURL('image/png');
      const pdf = new jsPDF({
        orientation: 'portrait',
        unit: 'px',
        format: [canvas.width, canvas.height]
      });
      pdf.addImage(imgData, 'PNG', 0, 0, canvas.width, canvas.height);
      pdf.save(`${selectedModule.title.replace(/\s+/g, '_')}_Study_Notes.pdf`);
    } catch (error) {
      console.error('PDF generation failed:', error);
    } finally {
      setIsDownloading(false);
    }
  };

  if (!isCourseInProfileScope) {
    return (
      <div className="h-full flex items-center justify-center bg-slate-50 p-8">
        <div className="max-w-md bg-white border border-slate-100 rounded-[32px] p-8 text-center shadow-xl shadow-indigo-100/20">
          <p className="text-[10px] font-black uppercase tracking-[0.3em] text-rose-500 mb-3">Content Scope Mismatch</p>
          <h2 className="text-2xl font-black text-slate-900 uppercase italic mb-4">Wrong Class or Board</h2>
          <p className="text-sm font-bold text-slate-400 mb-8">
            This course belongs to {course.syllabusId} {course.grade}, but your profile is set to {profile?.syllabus} {profile?.grade}.
          </p>
          <button
            onClick={onBack}
            className="px-8 py-4 bg-[#2e5b82] text-white rounded-2xl font-black text-[10px] uppercase tracking-widest"
          >
            Back to My Curriculum
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col lg:flex-row h-full overflow-hidden font-sans">
      {/* Course Sidebar */}
      {!selectedModule && (
        <div className="w-full lg:w-72 border-r border-slate-200 flex flex-col bg-white shrink-0">
          <div className="p-5 border-b border-slate-100">
            <div className="flex items-center justify-between">
              <div>
                <button onClick={onBack} className="text-slate-400 hover:text-indigo-600 mb-2 flex items-center gap-1 text-[10px] font-bold uppercase tracking-tighter transition-colors">
                  <ChevronRight className="w-3 h-3 rotate-180" /> Back to Dashboard
                </button>
                <div className="mb-4">
                  <span className="text-[10px] font-black text-indigo-500 uppercase tracking-widest block mb-1">Current Syllabus: {course.syllabusId}</span>
                  <h2 className="font-bold text-lg text-slate-900 leading-tight">{course.title}</h2>
                </div>
              </div>

              <div>
                <button
                  onClick={markCourseDone}
                  disabled={isMarkingDone}
                  className="px-3 py-2 bg-emerald-50 text-emerald-700 border border-emerald-100 rounded-xl text-[10px] font-black uppercase tracking-widest hover:bg-emerald-100 disabled:opacity-50"
                >
                  {isMarkingDone ? 'Updating...' : 'Mark Course Done'}
                </button>
              </div>
            </div>
            <div className="flex items-center gap-3">
              <div className="flex-1 bg-slate-100 rounded-full h-1.5 overflow-hidden">
                <motion.div
                  initial={{ width: 0 }}
                  animate={{ width: `${calculateProgress()}%` }}
                  className="h-full bg-indigo-600"
                />
              </div>
              <span className="text-[10px] font-black text-slate-400">{calculateProgress()}%</span>
            </div>
          </div>

          {error && (
            <div className="p-3 bg-rose-50 border border-rose-200 text-rose-600 rounded-lg text-[10px] font-bold text-center mx-3 my-2">
              {error}
            </div>
          )}

          <div className="p-3 border-b border-slate-100 space-y-1">            {[
              { id: 'lessons', icon: BookOpen, label: 'Lessons' },
              { id: 'roadmap', icon: MapIcon, label: 'Roadmap' },
              { id: 'quizzes', icon: HelpCircle, label: 'Assessments' },
              { id: 'forum', icon: MessageCircle, label: 'Discussion' },
              ...(profile?.role === 'teacher' ? [{ id: 'review', icon: FileText, label: 'Verifications' }] : [])
            ].map(tab => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id as any)}
                className={`w-full text-left px-3 py-2 rounded-lg flex items-center gap-3 transition-all ${
                  activeTab === tab.id ? 'bg-indigo-50 text-indigo-700' : 'text-slate-500 hover:bg-slate-50'
                }`}
              >
                <tab.icon className="w-4 h-4" />
                <span className="text-[10px] font-black uppercase tracking-widest">{tab.label}</span>
              </button>
            ))}
          </div>

          <div className="flex-1 overflow-y-auto p-3 space-y-1">
            {activeTab === 'lessons' ? (
              modules.map((m, idx) => {
                const isCompleted = progress[m.id] === 'completed';
                const isInProgress = progress[m.id] === 'in-progress';
                const isSelected = selectedModule?.id === m.id;

                return (
                  <button
                    key={m.id}
                    onClick={() => requestModuleOpen(m)}
                    className={`w-full text-left px-3 py-3 rounded-xl flex items-center gap-3 transition-all border ${
                      isSelected
                        ? 'bg-slate-900 text-white border-slate-900 shadow-md translate-x-1'
                        : isCompleted
                          ? 'bg-emerald-50/50 text-emerald-900 border-emerald-100/50 hover:bg-emerald-50 hover:border-emerald-200'
                          : isInProgress
                            ? 'bg-indigo-50/60 text-indigo-900 border-indigo-100 hover:bg-indigo-50 hover:border-indigo-200'
                            : 'hover:bg-slate-50 border-transparent text-slate-600'
                    }`}
                  >
                    <div className="flex-shrink-0 relative">
                      {isCompleted ? (
                        <div className={`w-6 h-6 rounded-full flex items-center justify-center transition-colors ${isSelected ? 'bg-indigo-400 text-slate-900' : 'bg-emerald-500 text-white shadow-sm shadow-emerald-200'}`}>
                          <Check className="w-3.5 h-3.5 stroke-[3]" />
                        </div>
                      ) : (
                        <div className={`w-6 h-6 rounded-lg border-2 flex items-center justify-center transition-colors ${isSelected ? 'border-indigo-400 text-white' : 'border-slate-200 text-slate-300'}`}>
                          {isInProgress ? (
                            <span className={`text-[10px] font-black ${!isSelected ? 'text-indigo-600' : ''}`}>{idx + 1}</span>
                          ) : (
                            <UnlockKeyhole className={`w-3.5 h-3.5 ${isSelected ? 'text-white' : 'text-indigo-500'}`} />
                          )}
                        </div>
                      )}
                    </div>
                    <div className="overflow-hidden flex-1">
                      <div className="flex items-center justify-between gap-2 mb-0.5">
                        <p className={`text-[8px] font-black uppercase tracking-[0.15em] ${isSelected ? 'text-white/40' : isCompleted ? 'text-emerald-600/40' : isInProgress ? 'text-indigo-500/60' : 'text-slate-400'}`}>Part {idx + 1}</p>
                        {!isSelected && (
                          <div className="flex items-center gap-1">
                            <span className={`text-[7px] font-black uppercase ${isCompleted ? 'text-emerald-600' : 'text-indigo-600'}`}>
                              {isCompleted ? 'Complete' : isInProgress ? 'In Progress' : 'Unlocked'}
                            </span>
                          </div>
                        )}
                      </div>
                      <p className={`font-bold text-[11px] truncate leading-none tracking-tight ${isSelected ? 'text-white' : isCompleted ? 'text-emerald-900' : isInProgress ? 'text-indigo-900' : 'text-slate-700'}`}>{m.title}</p>
                    </div>
                  </button>
                );
              })
            ) : activeTab === 'quizzes' ? (
              <div className="p-1 space-y-2">
                <div className="bg-indigo-50 border border-indigo-100 rounded-xl p-4 mb-4">
                  <p className="text-[10px] font-black text-indigo-400 uppercase tracking-widest mb-1">Interactive Challenge</p>
                  <h3 className="text-sm font-black text-slate-900 uppercase">Knowledge Sprinkles</h3>
                </div>
                {modules.map((m, idx) => (
                  <button
                    key={`quiz_${m.id}`}
                    onClick={() => requestModuleOpen(m, 'quizzes')}
                    className="w-full text-left px-4 py-4 rounded-xl flex items-center justify-between transition-all border border-slate-100 hover:bg-slate-50 group"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded-lg bg-indigo-100 flex items-center justify-center text-indigo-600 group-hover:scale-110 transition-transform">
                        <Zap className="w-4 h-4 fill-indigo-600" />
                      </div>
                      <div>
                        <p className="text-[9px] font-bold text-slate-400 uppercase tracking-tighter">Quiz {idx + 1}</p>
                        <p className="text-xs font-black text-slate-900 uppercase leading-none">{m.title} Fun</p>
                      </div>
                    </div>
                    <ChevronRight className="w-4 h-4 text-slate-300 group-hover:translate-x-1 transition-transform" />
                  </button>
                ))}
              </div>
            ) : (
              <div className="p-4 text-center">
                <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest leading-relaxed">System routing active for {activeTab}</p>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Content Area */}
      <div className={`flex-1 overflow-y-auto bg-slate-50/50 ${selectedModule ? 'lg:w-full' : ''}`}>
        <header className="h-14 bg-white border-b border-slate-200 flex items-center px-8 sticky top-0 z-10 justify-between">
           <span className="text-xs font-bold text-slate-400 uppercase tracking-widest italic">{activeTab === 'lessons' ? (selectedModule?.title || 'Curriculum Overview') : activeTab.toUpperCase()}</span>
           {activeTab === 'lessons' && selectedModule && (
             <div className="flex items-center gap-4">
               <button
                onClick={toggleFullscreen}
                className={`flex items-center gap-1 px-3 py-1 rounded-full border transition-all ${isFullscreen ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-amber-50 text-amber-700 border-amber-100'}`}>
                  <Target className="w-3.5 h-3.5" />
                  <span className="text-[10px] font-black uppercase">{isFullscreen ? 'Exit Focus' : 'Focus Mode'}</span>
               </button>
             </div>
           )}
           {activeTab === 'lessons' && modules.length > 0 && !selectedModule && (
             <button
               onClick={markCourseDone}
               disabled={isMarkingDone}
               className="px-4 py-2 bg-emerald-50 text-emerald-700 border border-emerald-100 rounded-xl text-[10px] font-black uppercase tracking-widest hover:bg-emerald-100 disabled:opacity-50"
             >
               {isMarkingDone ? 'Updating...' : 'Mark Course Done'}
             </button>
           )}
        </header>
        <div className="p-8">
          <AnimatePresence mode="wait">
            {activeTab === 'lessons' ? (
              selectedModule ? (
                <div ref={contentRef}>
                  <LessonPlayer 
                    key={selectedModule.id} 
                    module={selectedModule} 
                    course={course}
                    progress={progress[selectedModule.id]}
                    onComplete={(status) => handleModuleProgress(selectedModule, status)}
                    onBack={() => setSelectedModule(null)}
                  />
                  <div className="mt-8 flex justify-center">
                    {studyMaterialPath ? (
                      <a
                        href={encodeURI(studyMaterialPath)}
                        download
                        className="px-6 py-3 bg-slate-100 text-slate-600 rounded-xl text-[10px] font-black uppercase tracking-widest hover:bg-slate-200 transition-all flex items-center gap-2"
                      >
                        <FileText className="w-4 h-4" />
                        Download Study Material
                      </a>
                    ) : (
                      <button 
                        onClick={downloadPDF}
                        disabled={isDownloading}
                        className="px-6 py-3 bg-slate-100 text-slate-600 rounded-xl text-[10px] font-black uppercase tracking-widest hover:bg-slate-200 transition-all flex items-center gap-2"
                      >
                        <FileText className="w-4 h-4" />
                        {isDownloading ? 'Generating PDF...' : 'Download Study Notes'}
                      </button>
                    )}
                  </div>
                </div>
              ) : (
                <div className="flex items-center justify-center h-[calc(100vh-140px)] text-slate-300 flex-col gap-6">
                  <div className="relative flex items-center justify-center">
                    <motion.div
                      className="absolute -inset-8 rounded-full bg-indigo-100/50"
                      animate={{ scale: [0.92, 1.08, 0.92], opacity: [0.45, 0.2, 0.45] }}
                      transition={{ repeat: Infinity, duration: 2.8, ease: 'easeInOut' }}
                    />
                    <LearnBoostMascot mood="thinking" />
                    <motion.div
                      className="absolute -right-10 -top-3 bg-white border border-indigo-100 rounded-2xl px-3 py-2 shadow-lg"
                      animate={{ y: [0, -6, 0], rotate: [-2, 2, -2] }}
                      transition={{ repeat: Infinity, duration: 3.2, ease: 'easeInOut' }}
                    >
                      <BookOpen className="w-5 h-5 text-indigo-500" />
                    </motion.div>
                  </div>
                  <div className="text-center">
                    <p className="font-black uppercase tracking-[0.2em] text-xs text-slate-400">Mission Awaits</p>
                    <p className="text-[10px] font-bold text-slate-300 mt-1 uppercase">Select a module or view the roadmap</p>
                    <button 
                      onClick={() => setActiveTab('roadmap')}
                      className="mt-6 px-6 py-3 bg-indigo-600 text-white rounded-xl text-[10px] font-black uppercase tracking-widest hover:bg-indigo-700 transition-all"
                    >
                      View Syllabus Roadmap
                    </button>
                  </div>
                </div>
              )
            ) : activeTab === 'roadmap' ? (
              <SyllabusRoadmap 
                modules={modules} 
                progress={progress} 
                onSelect={(m) => requestModuleOpen(m)}
                moduleDescriptions={moduleDescriptions}
              />
            ) : activeTab === 'quizzes' ? (
              <QuizView
                courseId={course.id}
                moduleId={selectedModule?.id || 'general'}
                moduleTitle={selectedModule?.title}
                onModuleCompleted={() => selectedModule && handleModuleProgress(selectedModule, 'completed')}
              />
            ) : activeTab === 'review' ? (
              <TeacherReview courseId={course.id} />
            ) : (
              <ForumView courseId={course.id} />
            )}
          </AnimatePresence>
        </div>
      </div>

      <AnimatePresence>
        {permissionRequest && (
          <motion.div
            className="fixed inset-0 z-50 bg-slate-950/50 backdrop-blur-sm flex items-center justify-center p-6"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            <motion.div
              role="dialog"
              aria-modal="true"
              aria-labelledby="module-permission-title"
              className="w-full max-w-md bg-white rounded-[32px] border border-slate-100 shadow-2xl p-8"
              initial={{ scale: 0.96, y: 16 }}
              animate={{ scale: 1, y: 0 }}
              exit={{ scale: 0.96, y: 16 }}
            >
              <div className="w-14 h-14 rounded-2xl bg-indigo-50 text-indigo-600 flex items-center justify-center mb-6">
                <ShieldCheck className="w-7 h-7" />
              </div>
              <p className="text-[10px] font-black uppercase tracking-[0.25em] text-indigo-500 mb-2">Permission Required</p>
              <h2 id="module-permission-title" className="text-2xl font-black text-slate-900 uppercase tracking-tight mb-3">
                Open this module?
              </h2>
              <p className="text-sm font-bold text-slate-500 leading-relaxed mb-8">
                You are about to open {permissionRequest.targetTab === 'quizzes' ? 'the assessment for' : 'the lesson'} "{permissionRequest.module.title}". Accept to continue.
              </p>
              <div className="flex flex-col sm:flex-row gap-3">
                <button
                  onClick={() => setPermissionRequest(null)}
                  className="flex-1 px-5 py-4 bg-slate-100 text-slate-500 rounded-2xl text-[10px] font-black uppercase tracking-widest hover:bg-slate-200"
                >
                  Cancel
                </button>
                <button
                  onClick={acceptModuleOpen}
                  className="flex-1 px-5 py-4 bg-indigo-600 text-white rounded-2xl text-[10px] font-black uppercase tracking-widest hover:bg-indigo-700"
                >
                  Accept & Open
                </button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Side Chat */}
      {!selectedModule && (
        <div className="w-full lg:w-80 border-l border-slate-200 flex flex-col bg-slate-900 text-white shrink-0">
        <div className="p-5 border-b border-white/10 flex items-center justify-between">
          <div>
            <h3 className="text-sm font-black uppercase tracking-widest text-indigo-400">Class Feed</h3>
            <div className="flex items-center gap-1 mt-1">
               <span className="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-pulse" />
               <span className="text-[10px] font-bold text-white/50 lowercase italic">questions notify class teachers</span>
            </div>
          </div>
        </div>
        
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.map(msg => (
            <div key={msg.id} className="flex flex-col">
              <div className={`p-3 rounded-xl text-xs border-l-2 transition-colors ${
                msg.senderId === profile?.uid 
                  ? 'bg-white/5 border-indigo-500' 
                  : msg.role === 'teacher' 
                    ? 'bg-amber-500/10 border-amber-500 text-amber-200'
                    : 'bg-white/5 border-slate-700'
              }`}>
                <div className="flex justify-between items-center mb-1">
                  <span className={`font-black text-[9px] uppercase tracking-tighter ${msg.role === 'teacher' ? 'text-amber-500' : 'text-indigo-400'}`}>
                    {msg.senderName} {msg.role === 'teacher' && '- INSTRUCTOR'}
                  </span>
                </div>
                <p className="leading-relaxed opacity-90">{msg.message}</p>
              </div>
            </div>
          ))}
        </div>

        <form onSubmit={handleSendMessage} className="p-4 bg-white/5 border-t border-white/10">
          <div className="relative">
            <input 
              type="text"
              value={newMessage}
              onChange={(e) => setNewMessage(e.target.value)}
              placeholder="Type message..."
              className="w-full bg-slate-800 text-white text-xs pl-4 pr-10 py-3 rounded-lg focus:outline-none focus:ring-1 focus:ring-indigo-500 transition-all placeholder:text-slate-600"
            />
            <button type="submit" className="absolute right-2 top-2 p-1 text-indigo-500 hover:text-white transition-colors">
              <Send className="w-4 h-4" />
            </button>
          </div>
        </form>
      </div>
      )}
    </div>
  );
};
