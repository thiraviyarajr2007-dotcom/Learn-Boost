import React, { useEffect, useRef, useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import ReactMarkdown from 'react-markdown';
import { Module, Course } from '../hooks/useEducation';
import { QuizView } from './QuizView';
import { 
  X, 
  Heart, 
  Lightbulb, 
  Zap,
  ChevronRight,
  HelpCircle,
  Info,
  CheckCircle2,
  AlertCircle
} from 'lucide-react';

const FlipCard = ({ question, answer }: { question: string, answer: string }) => {
  const [isFlipped, setIsFlipped] = useState(false);
  return (
    <div 
      className="perspective-1000 w-full h-48 cursor-pointer my-6"
      onClick={() => setIsFlipped(!isFlipped)}
    >
      <motion.div
        className="relative w-full h-full transition-all duration-500 preserve-3d"
        animate={{ rotateY: isFlipped ? 180 : 0 }}
      >
        <div className="absolute inset-0 backface-hidden bg-indigo-50 border-2 border-indigo-200 rounded-2xl flex flex-col items-center justify-center p-6 text-center">
          <HelpCircle className="w-8 h-8 text-indigo-400 mb-4" />
          <p className="text-lg font-black text-indigo-900 uppercase tracking-tight">{question}</p>
          <p className="text-[10px] font-bold text-indigo-400 uppercase mt-4 tracking-widest">Tap to reveal answer</p>
        </div>
        <div className="absolute inset-0 backface-hidden bg-emerald-600 border-2 border-emerald-500 rounded-2xl flex items-center justify-center p-6 text-center rotate-y-180">
          <p className="text-xl font-black text-white italic">"{answer}"</p>
        </div>
      </motion.div>
    </div>
  );
};

const QuickCheck = ({ question, options, correct, rationale }: { question: string, options: string[], correct: string, rationale: string }) => {
  const [selected, setSelected] = useState<string | null>(null);
  const isCorrect = selected === correct;

  return (
    <div className="my-8 bg-slate-50 border-2 border-slate-100 rounded-[32px] p-8">
      <div className="flex items-center gap-3 mb-6">
        <div className="w-8 h-8 bg-amber-400 rounded-lg flex items-center justify-center text-slate-900 shadow-sm">
          <Zap className="w-4 h-4 fill-slate-900" />
        </div>
        <h4 className="text-xs font-black text-slate-400 uppercase tracking-widest">Quick Check-in</h4>
      </div>
      <p className="text-lg font-black text-slate-900 mb-6 leading-tight">{question}</p>
      <div className="space-y-3">
        {options.map((opt, i) => (
          <button
            key={i}
            onClick={() => !selected && setSelected(opt)}
            className={`w-full text-left p-4 rounded-2xl font-bold text-sm transition-all border-2 ${
              selected === opt
                ? isCorrect 
                  ? 'bg-emerald-50 border-emerald-500 text-emerald-900'
                  : 'bg-rose-50 border-rose-500 text-rose-900'
                : selected 
                  ? 'bg-slate-100 border-slate-200 text-slate-400'
                  : 'bg-white border-slate-100 hover:border-indigo-300 text-slate-700'
            }`}
          >
            <div className="flex items-center justify-between">
              <span>{opt}</span>
              {selected === opt && (
                isCorrect ? <CheckCircle2 className="w-5 h-5" /> : <AlertCircle className="w-5 h-5" />
              )}
            </div>
          </button>
        ))}
      </div>
      <AnimatePresence>
        {selected && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            className="mt-6 pt-6 border-t border-slate-200"
          >
            <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">
              {isCorrect ? 'Well Done!' : 'Not Quite...'}
            </p>
            <p className="text-sm font-bold text-slate-600 leading-relaxed italic">"{rationale}"</p>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export const LessonPlayer = ({ module, course, progress, onComplete, onBack }: { 
  module: Module, 
  course: Course, 
  progress?: string,
  onComplete: (status: 'completed' | 'in-progress') => void,
  onBack: () => void 
}) => {
  const [step, setStep] = useState(0);
  const [showQuiz, setShowQuiz] = useState(false);
  const onCompleteRef = useRef(onComplete);
  
  // Split content by paragraphs or headers for screens
  const parts = module.content.split('\n\n').filter(p => !p.includes('[QUIZ_PLACEHOLDER]'));

  useEffect(() => {
    onCompleteRef.current = onComplete;
  }, [onComplete]);

  useEffect(() => {
    if (!progress || progress === 'not-started') {
      onCompleteRef.current('in-progress');
    }
  }, [module.id, progress]);

  const handleNext = () => {
    if (step < parts.length - 1) {
      setStep(s => s + 1);
    } else {
      setShowQuiz(true);
    }
  };

  const renderContent = (content: string) => {
    // Check for custom widgets
    if (content.startsWith(':::card')) {
      const match = content.match(/:::card\s+(.*?)\s+:::\s+(.*?)\s+:::/);
      if (match) return <FlipCard question={match[1]} answer={match[2]} />;
    }

    if (content.startsWith(':::check')) {
      const match = content.match(/:::check\s+(.*?)\s+:::\s+(.*?)\s+:::\s+(.*?)\s+:::/);
      if (match) {
        const question = match[1];
        const options = match[2].split('|').map(o => o.trim());
        const correct = options.find(o => o.startsWith('*'))?.replace('*', '') || options[0];
        const cleanOptions = options.map(o => o.replace('*', ''));
        const rationale = match[3];
        return <QuickCheck question={question} options={cleanOptions} correct={correct} rationale={rationale} />;
      }
    }

    if (content.startsWith(':::tip')) {
      const match = content.match(/:::tip\s+(.*?)\s+:::/);
      if (match) return (
        <div className="my-6 bg-indigo-600 text-white rounded-[24px] p-6 shadow-xl shadow-indigo-200 flex items-start gap-4">
          <Info className="w-6 h-6 shrink-0 mt-1" />
          <p className="text-sm font-bold leading-relaxed">{match[1]}</p>
        </div>
      );
    }

    return <ReactMarkdown>{content}</ReactMarkdown>;
  };

  if (showQuiz) {
    return (
      <div className="max-w-4xl mx-auto py-8">
        <header className="mb-12 flex items-center justify-between">
           <button onClick={() => setShowQuiz(false)} className="px-4 py-2 bg-slate-100 rounded-xl text-[10px] font-black uppercase tracking-widest text-slate-500 hover:bg-slate-200 transition-all">
              Re-read Lesson
           </button>
           <h2 className="text-2xl font-black text-slate-900 tracking-tighter uppercase italic">{module.title} Challenge</h2>
           <div className="flex items-center gap-2">
              <Zap className="w-5 h-5 text-amber-500 fill-amber-500" />
              <span className="text-sm font-black text-slate-900">+50 XP</span>
           </div>
        </header>

        <div className="bg-white rounded-[40px] border-2 border-slate-100 p-10 shadow-xl shadow-indigo-100/30">
          <QuizView
            courseId={course.id}
            moduleId={module.id}
            moduleTitle={module.title}
            onModuleCompleted={() => onComplete('completed')}
          />
          
          <div className="mt-12 pt-8 border-t border-slate-100 flex justify-center gap-4">
             <button 
                onClick={() => {
                  onComplete('completed');
                  onBack();
                }}
                className="bg-emerald-600 text-white px-12 py-5 rounded-3xl font-black text-sm uppercase tracking-widest shadow-xl shadow-emerald-200 hover:scale-105 transition-all"
             >
                Finish & Claim Rewards
             </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto py-12 px-6">
      {/* Duolingo Progress Bar */}
      <div className="flex items-center gap-6 mb-16">
         <button onClick={onBack} className="p-2 hover:bg-slate-100 rounded-full transition-colors">
            <X className="w-6 h-6 text-slate-400" />
         </button>
         <div className="flex-1 h-3 bg-slate-100 rounded-full overflow-hidden shadow-inner">
            <motion.div 
               className="h-full bg-emerald-500 rounded-full"
               initial={{ width: 0 }}
               animate={{ width: `${((step + 1) / (parts.length)) * 100}%` }}
               transition={{ type: "spring", bounce: 0, duration: 0.8 }}
            />
         </div>
         <div className="flex items-center gap-1.5 bg-rose-50 px-3 py-1.5 rounded-full border border-rose-100">
            <Heart className="w-4 h-4 text-rose-500 fill-rose-500" />
            <span className="text-[10px] font-black text-rose-600">5</span>
         </div>
      </div>

      <AnimatePresence mode="wait">
        <motion.div 
          key={step}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          className="bg-white rounded-[48px] border-2 border-slate-100 p-12 shadow-2xl shadow-indigo-100/10 min-h-[450px] flex flex-col"
        >
          <div className="flex-1">
             <div className="flex items-center gap-4 mb-8">
                <div className="w-12 h-12 bg-indigo-600 rounded-2xl flex items-center justify-center text-white shadow-lg">
                   <Lightbulb className="w-6 h-6" />
                </div>
                <div>
                   <h3 className="text-xs font-black text-slate-400 uppercase tracking-widest">Step {step + 1} of {parts.length}</h3>
                   <h2 className="text-2xl font-black text-slate-900 tracking-tight uppercase italic">{module.title}</h2>
                </div>
             </div>
             
             <div className="prose prose-slate max-w-none prose-lg prose-p:font-bold prose-p:leading-relaxed prose-headings:font-black prose-headings:tracking-tighter prose-p:text-slate-700">
                {renderContent(parts[step])}
             </div>
          </div>

          {/* Interactive Footer */}
          <div className="mt-12 flex items-center gap-6 bg-slate-900 p-6 rounded-[32px] border border-white/10 shadow-xl">
             <div className="w-16 h-16 bg-amber-400 rounded-3xl flex items-center justify-center shadow-lg -rotate-6 shrink-0">
                <Lightbulb className="w-8 h-8 text-slate-900" />
             </div>
             <div>
                <p className="text-sm font-black text-indigo-300 italic mb-1 uppercase tracking-tight">Pro Tip from Buddy</p>
                <p className="text-xs font-bold text-white opacity-80 leading-relaxed">"Mastering this concept will unlock harder challenges and more XP! You're almost there!"</p>
             </div>
          </div>
        </motion.div>
      </AnimatePresence>

      <div className="mt-12 flex items-center justify-between">
         <button 
           onClick={() => step > 0 && setStep(s => s - 1)}
           disabled={step === 0}
           className={`px-8 py-5 rounded-3xl font-black text-sm uppercase tracking-widest transition-all ${
             step === 0 ? 'opacity-0' : 'text-slate-400 hover:text-slate-900'
           }`}
         >
            Previous
         </button>
         <button 
           onClick={handleNext}
           className="bg-indigo-600 text-white px-12 py-5 rounded-3xl font-black text-sm uppercase tracking-widest shadow-xl shadow-indigo-200 hover:scale-105 active:scale-95 transition-all text-center min-w-[220px] flex items-center justify-center gap-2 group"
         >
            {step === parts.length - 1 ? 'Start Challenge' : 'Continue'}
            <ChevronRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
         </button>
      </div>
    </div>
  );
};
