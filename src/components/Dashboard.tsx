import React, { useState, useEffect } from 'react';
import { motion } from 'motion/react';
import { useAuth } from '../context/AuthContext';
import { useEducation, Course, Badge } from '../hooks/useEducation';
import { LearnBoostMascot } from './LearnBoostMascot';
import { 
  TrendingUp, 
  Zap, 
  Users, 
  BookOpen, 
  Check, 
  Trophy 
} from 'lucide-react';

export const Dashboard = ({ 
  onSelectCourse, 
  overallProgress, 
  badges,
  onSeed
}: { 
  onSelectCourse: (c: Course) => void,
  overallProgress: Record<string, number>,
  badges: Badge[],
  onSeed?: () => void
}) => {
  const { profile } = useAuth();
  const { courses, loading, getProgress, getUserAttempts } = useEducation();
  const [dailyXP, setDailyXP] = useState(0);
  const [selectedTerm, setSelectedTerm] = useState<'Term 1' | 'Term 2' | 'Term 3' | 'Full Year'>('Full Year');
  const [selectedSubject, setSelectedSubject] = useState<string>('Mathematics');
  const usesFullYearCurriculum = profile?.syllabus === 'CBSE' || ['Class 9', 'Class 10', 'Class 11', 'Class 12'].includes(profile?.grade || '');
  const termOptions: Array<'Term 1' | 'Term 2' | 'Term 3' | 'Full Year'> = usesFullYearCurriculum
    ? ['Full Year']
    : ['Term 1', 'Term 2', 'Term 3'];
  const subjectOptions = profile?.syllabus === 'CBSE' || usesFullYearCurriculum ? ['Mathematics'] : ['Mathematics', 'Environmental Science'];

  useEffect(() => {
    if (usesFullYearCurriculum && selectedTerm !== 'Full Year') {
      setSelectedTerm('Full Year');
    }
    if (subjectOptions.length === 1 && selectedSubject !== subjectOptions[0]) {
      setSelectedSubject('Mathematics');
    }
    if (!usesFullYearCurriculum && selectedTerm === 'Full Year') {
      setSelectedTerm('Term 1');
    }
  }, [selectedSubject, selectedTerm, subjectOptions, usesFullYearCurriculum]);

  useEffect(() => {
    if (!profile) return;
    let progressXp = 0;
    let quizXp = 0;
    const updateDailyXp = () => setDailyXP(progressXp + quizXp);
    const getDate = (value: any) => value?.toDate ? value.toDate() : value instanceof Date ? value : null;
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const unsubProgress = getProgress(profile.uid, (p) => {
      progressXp = 0;

      p.forEach(item => {
        if (item.status === 'completed') {
          const updateDate = getDate(item.updatedAt);
          if (updateDate && updateDate >= today) {
            progressXp += 50;
          }
        }
      });
      updateDailyXp();
    });

    const unsubAttempts = getUserAttempts(profile.uid, (attempts) => {
      quizXp = 0;
      attempts.forEach(attempt => {
        const attemptDate = getDate(attempt.timestamp);
        if (attemptDate && attemptDate >= today) {
          quizXp += (attempt.score || 0) * 2;
        }
      });
      updateDailyXp();
    });

    return () => {
      unsubProgress();
      unsubAttempts();
    };
  }, [profile, getProgress, getUserAttempts]);

  // Filter courses based on user profile and selection
  const getCourseOrder = (course: Course) => {
    const idChapter = course.id.match(/_ch_(\d+)/i)?.[1];
    if (idChapter) return Number(idChapter);

    const titleChapter = course.title.match(/Chapter\s+(\d+)/i)?.[1];
    if (titleChapter) return Number(titleChapter);

    return Number.MAX_SAFE_INTEGER;
  };

  const filteredCourses = courses.filter(c => 
    c.syllabusId === profile?.syllabus && 
    c.grade === profile?.grade &&
    c.term === selectedTerm &&
    c.subject === selectedSubject
  ).sort((a,b) => getCourseOrder(a) - getCourseOrder(b) || a.title.localeCompare(b.title));

  const dailyGoalXPMap = {
    'Casual': 10,
    'Regular': 30,
    'Serious': 50,
    'Insane': 100
  };
  const targetXP = dailyGoalXPMap[profile?.dailyGoal || 'Regular'];
  const progressPercent = Math.min((dailyXP / targetXP) * 100, 100);

  if (loading) return <div className="flex items-center justify-center h-full text-slate-400 font-black uppercase text-xs tracking-widest">Compiling Learning Path...</div>;

  return (
    <div className="p-12 max-w-4xl mx-auto pb-40">
      {/* Progress Overview Section */}
      <section className="mb-20">
         <div className="flex items-center justify-between mb-8">
            <h2 className="text-xs font-black uppercase tracking-[0.2em] text-slate-400">Curriculum Health</h2>
            <div className="flex items-center gap-2">
               <TrendingUp className="w-3 h-3 text-indigo-500" />
               <span className="text-[10px] font-black text-indigo-900 uppercase">Growth Mode Active</span>
            </div>
         </div>
         <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {subjectOptions.map(sub => {
               const subCourses = courses.filter(c => c.subject === sub && c.syllabusId === profile?.syllabus && c.grade === profile?.grade);
               const completedTasks = subCourses.reduce((acc, c) => acc + (overallProgress[c.id] || 0), 0);
               const totalPossible = subCourses.reduce((acc, c) => acc + (c.moduleCount || 5), 0);
               const pct = totalPossible > 0 ? Math.round((completedTasks / totalPossible) * 100) : 0;

               return (
                  <div key={sub} className="bg-white p-6 rounded-3xl border border-slate-100 shadow-sm flex flex-col items-center text-center group hover:shadow-md transition-all">
                     <div className="relative w-16 h-16 mb-4">
                        <svg className="w-full h-full -rotate-90">
                           <circle cx="32" cy="32" r="28" className="stroke-slate-50 fill-none" strokeWidth="4" />
                           <motion.circle 
                              cx="32" cy="32" r="28" 
                              className="stroke-indigo-500 fill-none" 
                              strokeWidth="4" 
                              strokeLinecap="round"
                              initial={{ strokeDasharray: "176", strokeDashoffset: "176" }}
                              animate={{ strokeDashoffset: `${176 - (176 * pct) / 100}` }}
                              transition={{ duration: 2, delay: 0.5 }}
                           />
                        </svg>
                        <div className="absolute inset-0 flex items-center justify-center">
                           <span className="text-[10px] font-black text-slate-900">{pct}%</span>
                        </div>
                     </div>
                     <p className="text-[8px] font-black text-slate-400 uppercase tracking-widest mb-1">{sub === 'Mathematics' ? 'Logic' : 'Nature'}</p>
                     <p className="text-[10px] font-black text-slate-900 uppercase leading-none">{sub === 'Mathematics' ? 'Math' : 'EVS'}</p>
                  </div>
               );
            })}
            
            <div className="bg-indigo-600 p-6 rounded-3xl text-white flex flex-col items-center justify-center text-center shadow-lg shadow-indigo-200">
               <Zap className="w-6 h-6 fill-white mb-2" />
               <p className="text-[8px] font-black text-indigo-200 uppercase tracking-widest">Global Rank</p>
               <p className="text-xl font-black italic">#14</p>
            </div>

            <div className="bg-slate-900 p-6 rounded-3xl text-white flex flex-col items-center justify-center text-center">
               <Users className="w-6 h-6 text-indigo-400 mb-2" />
               <p className="text-[8px] font-black text-slate-500 uppercase tracking-widest">Peers Online</p>
               <p className="text-xl font-black italic">128</p>
            </div>
         </div>
      </section>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-20">
         {/* Daily Goal Card */}
         <div className="col-span-2 bg-white rounded-[40px] p-8 border border-slate-100 shadow-xl shadow-indigo-100/30 flex items-center gap-8 group">
            <div className="relative w-24 h-24 shrink-0">
               <svg className="w-full h-full -rotate-90">
                  <circle cx="48" cy="48" r="40" className="stroke-slate-50 fill-none" strokeWidth="8" />
                  <motion.circle 
                    cx="48" cy="48" r="40" 
                    className="stroke-amber-400 fill-none" 
                    strokeWidth="8" 
                    strokeLinecap="round"
                    initial={{ strokeDasharray: "251", strokeDashoffset: "251" }}
                    animate={{ strokeDashoffset: `${251 - (251 * progressPercent) / 100}` }}
                    transition={{ duration: 1.5, ease: "easeOut" }}
                  />
               </svg>
               <div className="absolute inset-0 flex flex-col items-center justify-center">
                  <span className="text-xl font-black text-slate-900 leading-none">{Math.round(progressPercent)}%</span>
               </div>
            </div>
            <div>
               <h3 className="text-xs font-black text-slate-400 uppercase tracking-widest mb-1">Today's Goal: {profile?.dailyGoal}</h3>
               <p className="text-xl font-black text-slate-900 mb-2">{dailyXP} / {targetXP} XP earned</p>
               <div className="flex items-center gap-2">
                  <div className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse" />
                  <span className="text-[10px] font-bold text-slate-400 uppercase">You're doing great, {profile?.name.split(' ')[0]}!</span>
               </div>
            </div>
         </div>

         {/* Badge Teaser */}
         <div className="bg-slate-900 rounded-[40px] p-8 border border-slate-800 shadow-xl flex flex-col justify-center items-center text-center">
             <div className="text-4xl mb-4 grayscale hover:grayscale-0 transition-all cursor-pointer">
                {badges[0]?.icon || 'Locked'}
             </div>
             <h3 className="text-[10px] font-black text-indigo-400 uppercase tracking-widest mb-1">Latest Achievement</h3>
             <p className="text-white font-black text-sm uppercase truncate w-full">{badges[0]?.title || 'Locked'}</p>
         </div>
      </div>

      <header className="flex flex-col items-center text-center gap-4 mb-16 relative">
        <LearnBoostMascot mood={progressPercent >= 100 ? 'excited' : 'happy'} />
        <div className="mt-4">
          <h2 className="text-indigo-900 font-black uppercase text-[12px] tracking-[0.3em] mb-2">{profile?.grade} - {profile?.syllabus}</h2>
          <h1 className="text-4xl font-black text-slate-900 tracking-tight leading-none uppercase italic underline decoration-[10px] decoration-indigo-200 underline-offset-4">{selectedSubject} Quest</h1>
        </div>
      </header>

      {/* Filters */}
      <div className="flex flex-wrap justify-center gap-4 mb-20">
         <div className="bg-slate-100 p-1.5 rounded-2xl flex gap-1">
            {termOptions.map((t) => (
               <button 
                 key={t}
                 onClick={() => setSelectedTerm(t as any)}
                 className={`px-4 py-2 rounded-xl text-[10px] font-black uppercase tracking-widest transition-all ${
                   selectedTerm === t ? 'bg-white text-slate-900 shadow-sm' : 'text-slate-400 hover:text-slate-600'
                 }`}
               >
                 {t}
               </button>
            ))}
         </div>
         <div className="bg-slate-100 p-1.5 rounded-2xl flex gap-1">
            {subjectOptions.map((s) => (
               <button 
                 key={s}
                 onClick={() => setSelectedSubject(s)}
                 className={`px-4 py-2 rounded-xl text-[10px] font-black uppercase tracking-widest transition-all ${
                   selectedSubject === s ? 'bg-white text-slate-900 shadow-sm' : 'text-slate-400 hover:text-slate-600'
                 }`}
               >
                 {s === 'Mathematics' ? 'Math' : 'EVS'}
               </button>
            ))}
         </div>
      </div>
      
      <div className="relative flex flex-col items-center gap-12">
        {/* The Connection Line */}
        <div className="absolute top-0 bottom-0 w-3 bg-slate-100 rounded-full left-1/2 -translate-x-1/2 -z-10" />

        {filteredCourses.length > 0 ? filteredCourses.map((course, idx) => {
          const completedCount = overallProgress[course.id] || 0;
          const totalModules = course.moduleCount || 5;
          const isDone = completedCount >= totalModules;

          return (
            <motion.div 
               key={course.id}
               initial={{ opacity: 0, x: idx % 2 === 0 ? -20 : 20 }}
               whileInView={{ opacity: 1, x: idx % 2 === 0 ? -40 : 40 }}
               viewport={{ once: true }}
               className="relative"
            >
               <button 
                  onClick={() => onSelectCourse(course)}
                  className={`path-node ${
                    isDone 
                      ? 'path-node-completed'
                      : 'path-node-unlocked'
                  }`}
               >
                  {/* Progress Ring */}
                  <svg className="absolute inset-0 w-full h-full -rotate-90 pointer-events-none p-1">
                    <circle cx="56" cy="56" r="50" className="stroke-slate-100/10 fill-none" strokeWidth="6" />
                    <motion.circle 
                      cx="56" 
                      cy="56" 
                      r="50" 
                      className={`fill-none ${isDone ? 'stroke-emerald-200' : 'stroke-indigo-400'}`}
                      strokeWidth="6" 
                      strokeLinecap="round"
                      initial={{ strokeDasharray: "314", strokeDashoffset: "314" }}
                      animate={{ strokeDashoffset: `${314 - (314 * Math.min(completedCount / totalModules, 1))}` }} 
                      transition={{ duration: 1.5 }}
                    />
                  </svg>

                  {isDone ? <Check className="w-10 h-10" /> : <Zap className="w-10 h-10 fill-white" />}
                  
                  {/* Tooltip Content Label */}
                  <div className={`absolute top-1/2 -translate-y-1/2 whitespace-nowrap p-4 rounded-2xl bg-white border-2 border-slate-100 shadow-xl pointer-events-none group transition-all z-10 ${
                    idx % 2 === 0 ? 'right-[120%] mr-4' : 'left-[120%] ml-4'
                  }`}>
                     <div className="flex items-center gap-2 mb-1">
                        <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Chapter {idx + 1}</span>
                        <span className="w-1 h-1 bg-slate-200 rounded-full" />
                        <span className={`text-[8px] font-black uppercase px-1.5 py-0.5 rounded-md ${
                          idx < 3 ? 'bg-emerald-100 text-emerald-600' : idx < 7 ? 'bg-indigo-100 text-indigo-600' : 'bg-rose-100 text-rose-600'
                        }`}>
                          {idx < 3 ? 'Foundation' : idx < 7 ? 'Intermediate' : 'Advanced'}
                        </span>
                     </div>
                     <span className="text-sm font-black text-slate-900 uppercase">{course.title.split(': ')[1]?.split(' (')[0] || course.title}</span>
                     <span className="text-[8px] font-black text-indigo-500 uppercase tracking-widest block mt-1">
                       {isDone ? 'Completed' : 'Available anytime'}
                     </span>
                     <div className="mt-2 h-1.5 w-24 bg-slate-50 rounded-full overflow-hidden">
                        <div className="h-full bg-indigo-500 transition-all duration-1000" style={{ width: `${Math.min(completedCount / totalModules, 1) * 100}%` }} />
                     </div>
                  </div>
               </button>
            </motion.div>
          );
        }) : (
           <div className="flex flex-col items-center justify-center py-32 text-slate-300 gap-6">
              <div className="relative">
                <div className="absolute inset-0 bg-indigo-100 rounded-full blur-3xl opacity-20 animate-pulse" />
                <BookOpen className="w-20 h-20 opacity-20 relative" />
              </div>
              <div className="text-center">
                <p className="text-[10px] font-black uppercase tracking-[0.4em] text-slate-400">Library Empty</p>
                <p className="text-sm font-bold text-slate-300 mt-2 max-w-xs mx-auto">No courses found for {profile?.syllabus} {profile?.grade} {selectedSubject} {selectedTerm}.</p>
              </div>
              {profile?.role === 'teacher' ? (
                <button 
                  onClick={onSeed}
                  className="mt-4 px-8 py-4 bg-[#2e5b82] text-white rounded-2xl font-black text-[10px] uppercase tracking-widest shadow-xl shadow-indigo-100 hover:scale-105 active:scale-95 transition-all"
                >
                  Populate My Curriculum
                </button>
              ) : (
                <p className="text-[8px] font-bold text-slate-400 uppercase tracking-widest">Awaiting Teacher to initialize modules</p>
              )}
           </div>
        )}

        {filteredCourses.length > 0 && (
          <div className="w-40 h-40 bg-slate-900 rounded-[40px] flex flex-col items-center justify-center text-white border-b-[12px] border-slate-950 shadow-2xl rotate-3 mt-12">
             <Trophy className="w-16 h-16 text-amber-400 mb-2" />
             <span className="text-[10px] font-black uppercase tracking-widest text-slate-400">{selectedTerm} Finale</span>
          </div>
        )}
      </div>
    </div>
  );
};
