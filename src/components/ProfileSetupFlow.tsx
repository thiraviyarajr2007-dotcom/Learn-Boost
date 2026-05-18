import React, { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { useAuth } from '../context/AuthContext';
import { Check } from 'lucide-react';

export const ProfileSetupFlow = () => {
  const { profile, updateProfile } = useAuth();
  const [step, setStep] = useState(1);
  const [grade, setGrade] = useState(profile?.grade || 'Class 1');
  const [syllabus, setSyllabus] = useState<'CBSE' | 'TN State Board'>(profile?.syllabus || 'CBSE');
  const [goal, setGoal] = useState(profile?.learningGoal || '');
  const [dailyGoal, setDailyGoal] = useState<'Casual' | 'Regular' | 'Serious' | 'Insane'>(profile?.dailyGoal || 'Regular');
  const [loading, setLoading] = useState(false);
  const isTeacher = profile?.role === 'teacher';
  const totalSteps = isTeacher ? 2 : 4;

  const classes = Array.from({ length: 12 }, (_, i) => `Class ${i + 1}`);

  const handleNext = () => setStep(s => s + 1);
  const handleBack = () => setStep(s => s - 1);

  const handleFinish = async () => {
    setLoading(true);
    try {
      await updateProfile(isTeacher
        ? { grade, syllabus }
        : {
            grade,
            syllabus,
            learningGoal: goal,
            dailyGoal
          }
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#f8fafc] flex flex-col items-center justify-center p-6 bg-[radial-gradient(#e2e8f0_1px,transparent_1px)] [background-size:24px_24px]">
      {/* Progress Bar */}
      <div className="w-full max-w-lg mb-12 flex items-center gap-4">
         <div className="flex-1 h-4 bg-slate-100 rounded-full overflow-hidden border border-slate-200">
            <motion.div 
               className="h-full bg-[#2e5b82]"
               initial={{ width: 0 }}
               animate={{ width: `${(step / totalSteps) * 100}%` }}
               transition={{ type: "spring", bounce: 0, duration: 0.5 }}
            />
         </div>
         <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest">{step} / {totalSteps}</span>
      </div>

      <AnimatePresence mode="wait">
        {step === 1 && (
          <motion.div 
            key="step1"
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            className="w-full max-w-lg bg-white rounded-[40px] p-10 shadow-2xl shadow-indigo-100/30 border border-slate-100"
          >
            <h1 className="text-3xl font-black text-slate-900 mb-2">Choose your Level</h1>
            <p className="text-slate-400 font-medium mb-8">What class/grade are you currently studying in?</p>
            
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 mb-10 overflow-y-auto max-h-[300px] p-2 custom-scrollbar">
              {classes.map(c => (
                <button 
                  key={c}
                  onClick={() => setGrade(c)}
                  className={`py-4 rounded-2xl font-black text-xs uppercase tracking-widest border-2 transition-all ${
                    grade === c ? 'border-indigo-600 bg-indigo-50 text-indigo-700 shadow-lg shadow-indigo-100/50' : 'border-slate-50 bg-slate-50 text-slate-400 hover:border-slate-100'
                  }`}
                >
                  {c}
                </button>
              ))}
            </div>

            <button 
              onClick={handleNext}
              className="w-full bg-[#2e5b82] text-white py-5 rounded-3xl font-black text-sm uppercase tracking-widest shadow-xl shadow-indigo-100 hover:scale-[1.02] active:scale-[0.98] transition-all"
            >
              Continue
            </button>
          </motion.div>
        )}

        {step === 2 && (
          <motion.div 
            key="step2"
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            className="w-full max-w-lg bg-white rounded-[40px] p-10 shadow-2xl shadow-indigo-100/30 border border-slate-100"
          >
            <h1 className="text-3xl font-black text-slate-900 mb-2">Your Syllabus</h1>
            <p className="text-slate-400 font-medium mb-8">Confirm your educational stream to unlock specialized content.</p>
            
            <div className="space-y-4 mb-10">
              {['CBSE', 'TN State Board'].map(s => (
                <button 
                  key={s}
                  onClick={() => setSyllabus(s as 'CBSE' | 'TN State Board')}
                  className={`w-full p-6 rounded-[32px] border-2 transition-all flex items-center gap-6 ${
                    syllabus === s ? 'border-indigo-600 bg-indigo-50 shadow-lg shadow-indigo-100' : 'border-slate-50 bg-slate-50'
                  }`}
                >
                  <div className="w-16 h-16 bg-white rounded-2xl flex items-center justify-center text-3xl shadow-sm border border-slate-100">
                    {s === 'CBSE' ? 'CBSE' : 'TN'}
                  </div>
                  <div className="text-left">
                    <span className={`block font-black text-sm uppercase tracking-widest ${syllabus === s ? 'text-indigo-700' : 'text-slate-400'}`}>{s}</span>
                    <span className="text-[10px] font-bold text-slate-300 uppercase">Mathematics Curriculum</span>
                  </div>
                  {syllabus === s && <Check className="ml-auto text-indigo-600 w-6 h-6" />}
                </button>
              ))}
            </div>

            <div className="flex gap-4">
              <button onClick={handleBack} className="flex-1 py-5 rounded-3xl font-black text-sm uppercase tracking-widest text-slate-400 border-2 border-slate-50 hover:bg-slate-50 transition-all">Back</button>
              <button 
                onClick={isTeacher ? handleFinish : handleNext}
                disabled={loading}
                className="flex-[2] bg-[#2e5b82] text-white py-5 rounded-3xl font-black text-sm uppercase tracking-widest shadow-xl shadow-indigo-100 hover:scale-[1.02] transition-all disabled:opacity-50"
              >
                {isTeacher ? (loading ? 'Finalizing...' : 'Enter Dashboard') : 'Continue'}
              </button>
            </div>
          </motion.div>
        )}

        {step === 3 && (
          <motion.div 
            key="step3"
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            className="w-full max-w-lg bg-white rounded-[40px] p-10 shadow-2xl shadow-indigo-100/30 border border-slate-100"
          >
            <h1 className="text-3xl font-black text-slate-900 mb-2">Why Math?</h1>
            <p className="text-slate-400 font-medium mb-8">What's your main goal for learning mathematics?</p>
            
            <div className="space-y-3 mb-10">
              {[
                { id: 'exam', label: 'Ace my school exams', icon: 'EXAM' },
                { id: 'foundation', label: 'Build a strong foundation', icon: 'BASE' },
                { id: 'fun', label: 'Just for fun & puzzles', icon: 'FUN' },
                { id: 'future', label: 'Prepare for future career', icon: 'JOB' },
              ].map(g => (
                <button 
                  key={g.id}
                  onClick={() => setGoal(g.label)}
                  className={`w-full p-4 rounded-2xl border-2 transition-all flex items-center gap-4 ${
                    goal === g.label ? 'border-indigo-600 bg-indigo-50 shadow-lg' : 'border-slate-50 bg-slate-50'
                  }`}
                >
                  <span className="w-12 text-center text-[10px] font-black tracking-widest text-indigo-500">{g.icon}</span>
                  <span className={`text-xs font-black uppercase tracking-widest ${goal === g.label ? 'text-indigo-700' : 'text-slate-400'}`}>{g.label}</span>
                </button>
              ))}
            </div>

            <div className="flex gap-4">
              <button onClick={handleBack} className="flex-1 py-5 rounded-3xl font-black text-sm uppercase tracking-widest text-slate-400 border-2 border-slate-50 hover:bg-slate-50 transition-all">Back</button>
              <button 
                onClick={handleNext}
                disabled={!goal}
                className="flex-[2] bg-[#2e5b82] text-white py-5 rounded-3xl font-black text-sm uppercase tracking-widest shadow-xl shadow-indigo-100 hover:scale-[1.02] transition-all disabled:opacity-50"
              >
                Continue
              </button>
            </div>
          </motion.div>
        )}

        {step === 4 && (
          <motion.div 
            key="step4"
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            className="w-full max-w-lg bg-white rounded-[40px] p-10 shadow-2xl shadow-indigo-100/30 border border-slate-100"
          >
            <h1 className="text-3xl font-black text-slate-900 mb-2">Daily Goal</h1>
            <p className="text-slate-400 font-medium mb-8">Commit to a daily learning habit. You can change this later.</p>
            
            <div className="space-y-3 mb-10">
              {[
                { id: 'Casual', desc: '5 mins / day', pts: '10' },
                { id: 'Regular', desc: '10 mins / day', pts: '30' },
                { id: 'Serious', desc: '20 mins / day', pts: '50' },
                { id: 'Insane', desc: '30 mins / day', pts: '100' },
              ].map(g => (
                <button 
                  key={g.id}
                  onClick={() => setDailyGoal(g.id as any)}
                  className={`w-full p-5 rounded-2xl border-2 transition-all flex items-center justify-between ${
                    dailyGoal === g.id ? 'border-amber-400 bg-amber-50 shadow-lg' : 'border-slate-50 bg-slate-50'
                  }`}
                >
                  <div className="text-left">
                    <span className={`block font-black text-sm uppercase tracking-widest ${dailyGoal === g.id ? 'text-amber-700' : 'text-slate-400'}`}>{g.id}</span>
                    <span className="text-[10px] font-bold text-slate-300 uppercase">{g.desc}</span>
                  </div>
                  <div className={`px-3 py-1 rounded-full font-black text-[10px] ${dailyGoal === g.id ? 'bg-amber-400 text-white' : 'bg-slate-200 text-slate-400 italic font-bold'}`}>
                    +{g.pts} XP
                  </div>
                </button>
              ))}
            </div>

            <div className="flex gap-4">
              <button onClick={handleBack} className="flex-1 py-5 rounded-3xl font-black text-sm uppercase tracking-widest text-slate-400 border-2 border-slate-50 hover:bg-slate-50 transition-all">Back</button>
              <button 
                onClick={handleFinish}
                disabled={loading}
                className="flex-[2] bg-emerald-500 text-white py-5 rounded-3xl font-black text-sm uppercase tracking-widest shadow-xl shadow-emerald-100 hover:scale-[1.02] transition-all disabled:opacity-50"
              >
                {loading ? 'Finalizing...' : 'Start Learning!'}
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};
