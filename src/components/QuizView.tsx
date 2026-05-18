import React, { useState, useEffect, useMemo } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { useEducation, Quiz, QuizAttempt } from '../hooks/useEducation';
import { useAuth } from '../context/AuthContext';
import { 
  Trophy, 
  CheckCircle2, 
  X, 
  XCircle,
  HelpCircle, 
  ArrowRight,
  Zap,
  Star,
  Award,
  Crown,
  Sparkles,
  MousePointer2,
  Gamepad2
} from 'lucide-react';

const getResultBadges = (scorePct: number) => {
  const badges = [
    { label: 'Quiz Cleared', detail: 'Completed', icon: Trophy, color: 'text-amber-600', bg: 'bg-amber-50', border: 'border-amber-100' },
    { label: 'Formula Practice', detail: 'Steps Solved', icon: Award, color: 'text-indigo-600', bg: 'bg-indigo-50', border: 'border-indigo-100' }
  ];

  if (scorePct >= 0.5) {
    badges.push({ label: 'Halfway Strong', detail: '50%+', icon: Star, color: 'text-emerald-600', bg: 'bg-emerald-50', border: 'border-emerald-100' });
  }

  if (scorePct >= 0.85) {
    badges.push({ label: 'Expert Mode', detail: '85%+', icon: Crown, color: 'text-rose-600', bg: 'bg-rose-50', border: 'border-rose-100' });
  }

  return badges;
};

const ThreeDAnswerButton = ({ 
  label, 
  onClick, 
  isSelected, 
  feedback, 
  disabled 
}: { 
  label: string, 
  onClick: () => void, 
  isSelected: boolean, 
  feedback: 'correct' | 'incorrect' | null,
  disabled: boolean
}) => {
  return (
    <motion.button
      whileHover={!disabled ? { y: -4, scale: 1.02 } : {}}
      whileTap={!disabled ? { y: 2, scale: 0.98 } : {}}
      onClick={onClick}
      disabled={disabled}
      className={`relative w-full text-left p-5 rounded-[24px] font-black text-sm uppercase tracking-tight transition-all border-b-[8px] flex items-center justify-between group overflow-hidden ${
        feedback === 'correct'
          ? 'bg-emerald-500 border-emerald-700 text-white shadow-lg shadow-emerald-200'
          : feedback === 'incorrect'
          ? 'bg-rose-500 border-rose-700 text-white shadow-lg shadow-rose-200'
          : isSelected
          ? 'bg-indigo-600 border-indigo-800 text-white shadow-lg shadow-indigo-200'
          : 'bg-white border-slate-200 text-slate-600 hover:border-slate-300 hover:bg-slate-50'
      }`}
    >
      <div className="flex items-center gap-4 relative z-10 flex-row-reverse justify-end">
        <span>{label}</span>
        <div className={`w-8 h-8 rounded-xl flex items-center justify-center border-2 transition-colors ${
          feedback ? 'bg-white/20 border-white/40' : isSelected ? 'bg-white/20 border-white/40' : 'bg-slate-100 border-slate-200 group-hover:bg-white'
        }`}>
          {feedback === 'correct' ? <CheckCircle2 className="w-5 h-5" /> : feedback === 'incorrect' ? <XCircle className="w-5 h-5" /> : <MousePointer2 className="w-4 h-4" />}
        </div>
      </div>
      
      {/* 3D Reflection Effect */}
      <div className="absolute top-0 left-0 w-full h-1 bg-white/20 rounded-t-2xl pointer-events-none" />
      
      {feedback === 'correct' && (
        <motion.div 
          className="absolute inset-0 bg-white/20"
          initial={{ x: '-100%' }}
          animate={{ x: '200%' }}
          transition={{ repeat: Infinity, duration: 1.5, ease: 'linear' }}
        />
      )}
    </motion.button>
  );
};

const getWarmupItems = (quiz: Quiz) =>
  quiz.questions
    .filter(question => question.type === 'mcq' && question.options?.length)
    .slice(0, 4)
    .map((question, index) => {
      const formulaMatch = question.text.match(/^Which formula is best for (.+?) sums in/i);
      const exampleMatch = question.text.match(/^Which example sum matches (.+?)\?/i);
      const concept = formulaMatch?.[1] || exampleMatch?.[1] || question.text.replace(/\?$/, '');

      return {
        id: question.id,
        prompt: exampleMatch
          ? `Pick the worked example for ${concept}.`
          : `Pick the formula used to solve ${concept} sums.`,
        answer: question.correctAnswer,
        order: index + 1
      };
    })
    .filter((item, index, items) => items.findIndex(other => other.prompt === item.prompt && other.answer === item.answer) === index);

const shuffleBySeed = <T,>(_items: T[], _seed: string) => {
  const items = [..._items];
  for (let i = items.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [items[i], items[j]] = [items[j], items[i]];
  }
  return items;
};

export const QuizView = ({
  courseId,
  moduleId,
  moduleTitle,
  onModuleCompleted
}: {
  courseId: string,
  moduleId: string,
  moduleTitle?: string,
  onModuleCompleted?: () => void
}) => {
  const { profile } = useAuth();
  const { getQuizzes, submitQuizAttempt, getAttempts } = useEducation();
  const [quizzes, setQuizzes] = useState<Quiz[]>([]);
  const [selectedQuiz, setSelectedQuiz] = useState<Quiz | null>(null);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [showResult, setShowResult] = useState(false);
  const [attempts, setAttempts] = useState<QuizAttempt[]>([]);
  const [submittedAttempt, setSubmittedAttempt] = useState<QuizAttempt | null>(null);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [timeLeft, setTimeLeft] = useState<number | null>(null);
  const [feedback, setFeedback] = useState<{ questionId: string; selected: string; isCorrect: boolean } | null>(null);
  const [showWarmupGame, setShowWarmupGame] = useState(false);
  const [warmupMatches, setWarmupMatches] = useState<Record<string, string>>({});
  const [selectedWarmupPrompt, setSelectedWarmupPrompt] = useState<string | null>(null);

  const warmupItems = useMemo(() => selectedQuiz ? getWarmupItems(selectedQuiz) : [], [selectedQuiz]);

  const answerChoices = useMemo(() => {
    if (!selectedQuiz) return [];
    return shuffleBySeed(
      warmupItems.map(item => item.answer).filter((answer, index, answers) => answers.indexOf(answer) === index),
      selectedQuiz.id
    );
  }, [warmupItems, selectedQuiz?.id]);

  useEffect(() => {
    return getQuizzes(courseId, moduleId, setQuizzes);
  }, [courseId, moduleId, getQuizzes]);

  useEffect(() => {
    if (selectedQuiz && profile) {
      return getAttempts(profile.uid, selectedQuiz.id, courseId, setAttempts);
    }
  }, [selectedQuiz, profile, courseId, getAttempts]);

  const handleStartQuiz = (quiz: Quiz) => {
    setSelectedQuiz(quiz);
    setAnswers({});
    setFeedback(null);
    setSubmittedAttempt(null);
    setShowResult(false);
    setCurrentQuestionIndex(0);
    setWarmupMatches({});
    setSelectedWarmupPrompt(null);
    const hasWarmupGame = getWarmupItems(quiz).length > 0;
    setShowWarmupGame(hasWarmupGame);
    setTimeLeft(hasWarmupGame ? null : quiz.timerPerQuestion || null);
  };

  const startTimedQuiz = () => {
    if (!selectedQuiz) return;
    setShowWarmupGame(false);
    setCurrentQuestionIndex(0);
    setFeedback(null);
    setSelectedWarmupPrompt(null);
    setTimeLeft(selectedQuiz.timerPerQuestion || null);
  };

  const handleNextQuestion = () => {
    if (!selectedQuiz) return;

    if (currentQuestionIndex < selectedQuiz.questions.length - 1) {
      setCurrentQuestionIndex(prev => prev + 1);
      setFeedback(null);
      if (selectedQuiz.timerPerQuestion) {
        setTimeLeft(selectedQuiz.timerPerQuestion);
      }
    } else {
      handleSubmit();
    }
  };

  useEffect(() => {
    if (timeLeft === null || showWarmupGame || showResult || !selectedQuiz || !selectedQuiz.timerPerQuestion) return;

    if (timeLeft <= 0) {
      handleNextQuestion();
      return;
    }

    const timer = setTimeout(() => {
      setTimeLeft(prev => (prev !== null && prev > 0 ? prev - 1 : 0));
    }, 1000);

    return () => clearTimeout(timer);
  }, [timeLeft, showResult, selectedQuiz]);

  const handleSubmit = async () => {
    if (!selectedQuiz || isSubmitting) return;
    setIsSubmitting(true);
    setError(null);
    try {
      const attempt = await submitQuizAttempt(courseId, selectedQuiz.id, answers, selectedQuiz.questions, selectedQuiz.moduleId, moduleTitle || selectedQuiz.title);
      if (attempt) {
        setSubmittedAttempt(attempt);
        setAttempts(prev => [attempt, ...prev.filter(item => item.id !== attempt.id)]);
      }
      onModuleCompleted?.();
      setShowResult(true);
    } catch (err) {
      console.error('Quiz submission failed:', err);
      setError('Oops! We couldn\'t save your quiz results. Please check your connection and try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const isCorrectAnswer = (question: Quiz['questions'][number], value: string) =>
    value.toLowerCase().trim() === question.correctAnswer.toLowerCase().trim();

  const handleObjectiveAnswer = (question: Quiz['questions'][number], value: string) => {
    if (feedback) return;
    const isCorrect = isCorrectAnswer(question, value);
    setAnswers(prev => ({ ...prev, [question.id]: value }));
    setFeedback({ questionId: question.id, selected: value, isCorrect });
  };

  if (selectedQuiz && showWarmupGame && !showResult) {
    const matchedCount = warmupItems.filter(item => warmupMatches[item.id] === item.answer).length;
    const gameComplete = warmupItems.length > 0 && matchedCount === warmupItems.length;

    return (
      <div className="max-w-4xl mx-auto py-12">
        <div className="flex items-center justify-between mb-10">
          <button onClick={() => setSelectedQuiz(null)} className="p-3 bg-white border-2 border-slate-100 rounded-2xl text-slate-400 hover:text-slate-900 transition-all shadow-sm">
            <X className="w-6 h-6" />
          </button>
          <div className="text-right">
            <p className="text-[10px] font-black text-indigo-500 uppercase tracking-[0.3em]">Warm-up Game</p>
            <p className="text-xs font-black text-slate-400 uppercase">{matchedCount} / {warmupItems.length} matched</p>
          </div>
        </div>

        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-[48px] border-b-[12px] border-slate-200 shadow-2xl p-10"
        >
          <div className="flex items-start gap-5 mb-8">
            <div className="w-16 h-16 rounded-3xl bg-indigo-600 text-white flex items-center justify-center shadow-xl shadow-indigo-100">
              <Gamepad2 className="w-8 h-8" />
            </div>
            <div>
              <p className="text-[10px] font-black text-slate-400 uppercase tracking-[0.25em] mb-2">Match The Following</p>
              <h2 className="text-3xl font-black text-slate-900 uppercase italic tracking-tight">Formula Game Before Quiz</h2>
              <p className="text-sm font-bold text-slate-500 mt-2">Match each sum or formula prompt with the correct formula/example. The quiz timer starts after this game.</p>
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-[1fr_0.9fr] gap-6">
            <div className="space-y-4">
              {warmupItems.map((item) => {
                const selected = warmupMatches[item.id];
                const isCorrect = selected === item.answer;

                return (
                  <button
                    key={item.id}
                    onClick={() => setSelectedWarmupPrompt(item.id)}
                    className={`w-full text-left p-5 rounded-3xl border-2 transition-all ${
                      isCorrect
                        ? 'bg-emerald-50 border-emerald-200'
                        : selectedWarmupPrompt === item.id
                          ? 'bg-indigo-50 border-indigo-300'
                          : selected
                            ? 'bg-rose-50 border-rose-200'
                            : 'bg-slate-50 border-slate-100'
                    }`}
                  >
                    <div className="flex items-start gap-4">
                      <div className={`w-10 h-10 rounded-2xl flex items-center justify-center font-black shrink-0 ${isCorrect ? 'bg-emerald-500 text-white' : 'bg-white text-slate-400'}`}>
                        {isCorrect ? <CheckCircle2 className="w-5 h-5" /> : item.order}
                      </div>
                      <div className="min-w-0">
                        <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">Prompt</p>
                        <p className="text-sm font-black text-slate-900 leading-snug">{item.prompt}</p>
                        {selected && (
                          <p className={`text-xs font-bold mt-3 ${isCorrect ? 'text-emerald-700' : 'text-rose-700'}`}>
                            {isCorrect ? 'Matched correctly' : 'Try a different answer card'}
                          </p>
                        )}
                      </div>
                    </div>
                  </button>
                );
              })}
            </div>

            <div className="bg-slate-900 rounded-[32px] p-5 space-y-3">
              <p className="text-[10px] font-black text-indigo-300 uppercase tracking-[0.25em] mb-3">Answer Cards</p>
              {answerChoices.map((answer) => (
                <button
                  key={answer}
                  onClick={() => {
                    const targetItem = warmupItems.find(item => item.id === selectedWarmupPrompt) || warmupItems.find(item => warmupMatches[item.id] !== item.answer);
                    if (!targetItem) return;
                    setWarmupMatches(prev => ({ ...prev, [targetItem.id]: answer }));
                    setSelectedWarmupPrompt(null);
                  }}
                  className="w-full text-left p-4 rounded-2xl bg-white/10 hover:bg-white/15 text-white border border-white/10 text-xs font-black leading-snug break-words"
                >
                  {answer}
                </button>
              ))}
              <button
                onClick={() => {
                  setWarmupMatches({});
                  setSelectedWarmupPrompt(null);
                }}
                className="w-full mt-4 p-3 rounded-2xl bg-white text-slate-500 text-[10px] font-black uppercase tracking-widest"
              >
                Reset Matches
              </button>
            </div>
          </div>

          <div className="flex gap-3">
            <button
              onClick={() => {
                // reveal correct matches
                setWarmupMatches(Object.fromEntries(warmupItems.map(item => [item.id, item.answer])));
                setSelectedWarmupPrompt(null);
              }}
              className="px-6 py-3 bg-indigo-600 text-white rounded-3xl font-black uppercase text-sm tracking-[0.3em] transition-all shadow-md hover:scale-105"
            >
              Reveal Answers
            </button>

            <button
              onClick={startTimedQuiz}
              disabled={!gameComplete}
              className="px-6 py-3 bg-slate-900 text-white rounded-3xl font-black uppercase text-sm tracking-[0.3em] transition-all shadow-2xl shadow-slate-900/30 border-b-[8px] border-slate-950 disabled:opacity-40 disabled:border-b-[4px] flex-1"
            >
              Start Timed Quiz
            </button>
          </div>
        </motion.div>
      </div>
    );
  }

  if (selectedQuiz && !showResult) {
    const q = selectedQuiz.questions[currentQuestionIndex];
    
    return (
      <div className="max-w-3xl mx-auto py-12 relative perspective-1000">
        <div className="flex items-center justify-between mb-12">
           <button onClick={() => setSelectedQuiz(null)} className="p-3 bg-white border-2 border-slate-100 rounded-2xl text-slate-400 hover:text-slate-900 transition-all hover:scale-110 active:scale-95 shadow-sm">
              <X className="w-6 h-6" />
           </button>
           <div className="flex-1 mx-8 h-4 bg-slate-100 rounded-full overflow-hidden shadow-inner p-1">
              <motion.div 
                className="h-full bg-gradient-to-r from-indigo-600 to-indigo-400 rounded-full"
                initial={{ width: 0 }}
                animate={{ width: `${((currentQuestionIndex + 1) / selectedQuiz.questions.length) * 100}%` }}
              />
           </div>
           {timeLeft !== null && (
             <motion.div 
              animate={timeLeft < 10 ? { scale: [1, 1.1, 1], rotate: [0, 5, -5, 0] } : {}}
              transition={{ repeat: Infinity, duration: 1 }}
              className={`w-14 h-14 rounded-2xl border-4 flex items-center justify-center font-black text-sm shadow-lg ${timeLeft < 10 ? 'border-rose-500 bg-rose-50 text-rose-500' : 'border-indigo-100 bg-indigo-50 text-indigo-600'}`}
             >
                {timeLeft}s
             </motion.div>
           )}
        </div>

        <div className="space-y-8 preserve-3d">
           <AnimatePresence mode="wait">
             <motion.div 
               key={q.id}
               initial={{ opacity: 0, rotateY: 90, scale: 0.8 }}
               animate={{ opacity: 1, rotateY: 0, scale: 1 }}
               exit={{ opacity: 0, rotateY: -90, scale: 0.8 }}
               transition={{ type: 'spring', damping: 20, stiffness: 100 }}
               className="bg-white p-10 rounded-[48px] border-b-[12px] border-slate-200 shadow-2xl relative"
             >
                <div className="absolute -top-4 -right-4 w-12 h-12 bg-amber-400 rounded-2xl rotate-12 shadow-lg flex items-center justify-center text-white">
                  <Star className="w-6 h-6 fill-white" />
                </div>
                
                <div className="flex justify-between items-center mb-8">
                   <div className="flex flex-col">
                     <span className="text-[10px] font-black text-slate-300 uppercase tracking-[0.2em] mb-1">Challenge Part</span>
                     <span className="text-xl font-black text-slate-900 tracking-tighter italic">{currentQuestionIndex + 1} / {selectedQuiz.questions.length}</span>
                   </div>
                   <div className="px-4 py-2 bg-indigo-600 text-white rounded-2xl font-black text-xs uppercase tracking-widest shadow-lg shadow-indigo-200">
                     +{q.points} XP
                   </div>
                </div>
                
                <h2 className="text-2xl font-black text-slate-900 mb-10 leading-tight uppercase italic underline decoration-[8px] decoration-indigo-50 underline-offset-4">{q.text}</h2>
                
                <div className="space-y-4">
                  {q.type === 'mcq' && q.options?.map((opt: string) => (
                    <ThreeDAnswerButton 
                      key={opt}
                      label={opt}
                      onClick={() => handleObjectiveAnswer(q, opt)}
                      isSelected={answers[q.id] === opt}
                      feedback={feedback?.questionId === q.id && feedback.selected === opt ? (feedback.isCorrect ? 'correct' : 'incorrect') : null}
                      disabled={!!feedback}
                    />
                  ))}
                  
                  {q.type === 'tf' && (
                    <div className="flex gap-4">
                       {['true', 'false'].map(opt => (
                         <ThreeDAnswerButton 
                            key={opt}
                            label={opt}
                            onClick={() => handleObjectiveAnswer(q, opt)}
                            isSelected={answers[q.id] === opt}
                            feedback={feedback?.questionId === q.id && feedback.selected === opt ? (feedback.isCorrect ? 'correct' : 'incorrect') : null}
                            disabled={!!feedback}
                          />
                       ))}
                    </div>
                  )}

                  {q.type === 'sa' && (
                    <div className="relative group">
                      <textarea 
                        placeholder="Type your brilliant response..."
                        className="w-full min-h-[120px] bg-slate-50 border-b-[6px] border-slate-200 rounded-3xl p-6 text-sm font-bold focus:outline-none focus:border-indigo-400 focus:bg-white transition-all resize-none shadow-inner"
                        value={answers[q.id] || ''}
                        onChange={(e) => setAnswers({...answers, [q.id]: e.target.value})}
                      />
                      <div className="absolute bottom-4 right-4 text-indigo-200 group-focus-within:text-indigo-400 transition-colors">
                        <MousePointer2 className="w-5 h-5" />
                      </div>
                    </div>
                  )}
                </div>

                <AnimatePresence>
                  {feedback?.questionId === q.id && (
                    <motion.div
                      initial={{ opacity: 0, height: 0, scale: 0.9 }}
                      animate={{ opacity: 1, height: 'auto', scale: 1 }}
                      className={`mt-8 p-6 rounded-[32px] border-b-[6px] flex items-start gap-4 ${
                        feedback.isCorrect
                          ? 'bg-emerald-50 border-emerald-200 text-emerald-900'
                          : 'bg-rose-50 border-rose-200 text-rose-900'
                      }`}
                    >
                      <div className={`w-12 h-12 rounded-2xl flex items-center justify-center shrink-0 shadow-sm ${
                        feedback.isCorrect ? 'bg-emerald-500' : 'bg-rose-500'
                      }`}>
                        {feedback.isCorrect ? <Sparkles className="w-6 h-6 text-white" /> : <XCircle className="w-6 h-6 text-white" />}
                      </div>
                      <div>
                        <p className="text-[10px] font-black uppercase tracking-[0.2em] mb-1">
                          {feedback.isCorrect ? 'Brilliant Move!' : 'Learning Moment!'}
                        </p>
                        {!feedback.isCorrect && (
                          <p className="text-sm font-black mb-1">Correct Answer: <span className="underline decoration-2 underline-offset-2">{q.correctAnswer}</span></p>
                        )}
                        {q.rationale && <p className="text-xs font-bold opacity-80 leading-relaxed italic">"{q.rationale}"</p>}
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
             </motion.div>
           </AnimatePresence>
        </div>

        <motion.button 
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          onClick={handleNextQuestion}
          disabled={isSubmitting || !answers[q.id]?.trim()}
          className="w-full mt-12 bg-slate-900 text-white py-6 rounded-3xl font-black uppercase text-sm tracking-[0.3em] transition-all shadow-2xl shadow-slate-900/40 active:translate-y-2 border-b-[8px] border-slate-950 disabled:opacity-50 disabled:translate-y-0 disabled:border-b-[4px] flex items-center justify-center gap-3 group"
        >
          {isSubmitting ? 'Saving Progress...' : (
            <>
              {currentQuestionIndex === selectedQuiz.questions.length - 1 ? 'Claim Victory' : 'Continue Quest'}
              <ArrowRight className="w-5 h-5 group-hover:translate-x-2 transition-transform" />
            </>
          )}
        </motion.button>
        {error && (
          <motion.div 
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-6 p-4 bg-rose-50 border border-rose-200 text-rose-700 rounded-2xl text-xs font-bold text-center"
          >
            {error}
          </motion.div>
        )}
      </div>
    );
  }

  if (showResult) {
    const lastAttempt = submittedAttempt || [...attempts].sort((a,b) => (b.timestamp?.seconds || 0) - (a.timestamp?.seconds || 0))[0];
    const scorePct = lastAttempt ? lastAttempt.score / lastAttempt.totalPossible : 0;
    const resultBadges = getResultBadges(scorePct);
    
    return (
      <div className="max-w-3xl mx-auto py-20 text-center perspective-1000">
         <motion.div 
           initial={{ rotateX: -90, opacity: 0 }}
           animate={{ rotateX: 0, opacity: 1 }}
           className="bg-white rounded-[64px] border-b-[16px] border-slate-200 p-16 shadow-2xl relative"
         >
            <div className="absolute -top-12 left-1/2 -translate-x-1/2 w-32 h-32 bg-amber-400 rounded-[40px] flex items-center justify-center shadow-2xl border-b-[12px] border-amber-600">
               <Trophy className="w-16 h-16 text-white" />
            </div>
            
            <div className="mt-16 mb-12">
               <h2 className="text-5xl font-black text-slate-900 tracking-tighter uppercase italic mb-4">Quest Cleared!</h2>
               <p className="text-slate-400 font-black uppercase text-xs tracking-[0.4em] italic mb-12">Rewards are waiting in your profile</p>
               
               <div className="flex items-center justify-center gap-8 mb-12">
                  <div className="bg-indigo-50 p-8 rounded-[40px] border-b-[8px] border-indigo-100">
                     <p className="text-[10px] font-black text-indigo-400 uppercase tracking-widest mb-1">Final Score</p>
                     <p className="text-6xl font-black text-indigo-600 tracking-tighter">{lastAttempt?.score}<span className="text-2xl text-indigo-300">/</span>{lastAttempt?.totalPossible}</p>
                  </div>
                  <div className="bg-amber-50 p-8 rounded-[40px] border-b-[8px] border-amber-100">
                     <p className="text-[10px] font-black text-amber-400 uppercase tracking-widest mb-1">XP Earned</p>
                     <p className="text-6xl font-black text-amber-600 tracking-tighter">+{Math.round((lastAttempt?.score || 0) * 2.5)}</p>
                  </div>
               </div>
               
               <div className="grid grid-cols-3 gap-4 mb-12">
                  {[
                    { label: 'Accuracy', value: `${Math.round(scorePct * 100)}%`, color: 'text-emerald-500' },
                    { label: 'Speed', value: 'Fast', color: 'text-indigo-500' },
                    { label: 'Rank', value: '#1', color: 'text-amber-500' }
                  ].map(stat => (
                    <div key={stat.label} className="bg-slate-50 p-4 rounded-3xl border-b-4 border-slate-100">
                       <p className="text-[8px] font-black text-slate-400 uppercase tracking-widest mb-1">{stat.label}</p>
                       <p className={`text-lg font-black ${stat.color} uppercase italic`}>{stat.value}</p>
                    </div>
                  ))}
               </div>

               <div className="mb-12 text-left">
                  <p className="text-[10px] font-black text-slate-400 uppercase tracking-[0.3em] mb-4 text-center">Badges Unlocked After Quiz</p>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    {resultBadges.map((badge) => {
                      const Icon = badge.icon;
                      return (
                        <div key={badge.label} className={`${badge.bg} ${badge.border} border p-4 rounded-3xl flex items-center gap-4`}>
                          <div className={`w-12 h-12 rounded-2xl bg-white flex items-center justify-center ${badge.color} shadow-sm`}>
                            <Icon className="w-6 h-6 fill-current" />
                          </div>
                          <div>
                            <p className={`text-sm font-black uppercase italic ${badge.color}`}>{badge.label}</p>
                            <p className="text-[9px] font-black text-slate-400 uppercase tracking-widest">{badge.detail}</p>
                          </div>
                        </div>
                      );
                    })}
                  </div>
               </div>
            </div>

            <button 
              onClick={() => setSelectedQuiz(null)} 
              className="w-full bg-slate-900 text-white py-6 rounded-3xl font-black uppercase text-sm tracking-[0.3em] shadow-xl border-b-[8px] border-slate-950 hover:scale-105 active:translate-y-2 transition-all"
            >
               Collect & Continue
            </button>
         </motion.div>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 py-8 perspective-1000">
      {quizzes.length > 0 ? quizzes.map(quiz => {
        const myAttempt = attempts.find(a => a.quizId === quiz.id);
        return (
          <motion.button 
            key={quiz.id}
            whileHover={{ y: -8, rotateX: 5, rotateY: -5 }}
            onClick={() => handleStartQuiz(quiz)}
            className={`p-8 rounded-[40px] border-b-[12px] transition-all text-left bg-white shadow-xl flex flex-col group relative overflow-hidden ${
              myAttempt ? 'border-emerald-500' : 'border-slate-100 hover:border-indigo-300'
            }`}
          >
            <div className="absolute top-0 right-0 w-32 h-32 bg-slate-50 rounded-full -mr-16 -mt-16 opacity-50 group-hover:scale-150 transition-transform duration-700" />
            
            <div className="flex justify-between items-start mb-8 relative z-10">
               <div className={`p-4 rounded-2xl shadow-sm ${myAttempt ? 'bg-emerald-500 text-white shadow-emerald-200' : 'bg-indigo-600 text-white shadow-indigo-200'}`}>
                  <HelpCircle className="w-6 h-6" />
               </div>
               {myAttempt && (
                 <div className="bg-emerald-50 px-3 py-1.5 rounded-full border border-emerald-100 flex items-center gap-1">
                   <Award className="w-3.5 h-3.5 text-emerald-600" />
                   <span className="text-[10px] font-black text-emerald-700 uppercase">Cleared</span>
                 </div>
               )}
            </div>
            
            <h3 className="font-black text-slate-900 leading-tight mb-2 uppercase italic text-lg relative z-10 group-hover:text-indigo-600 transition-colors">{quiz.title}</h3>
            <div className="flex items-center gap-3 mb-8 relative z-10">
               <div className="flex items-center gap-1 text-slate-400">
                  <Zap className="w-3.5 h-3.5 fill-slate-300" />
                  <span className="text-[10px] font-black uppercase tracking-tighter">{quiz.questions.length} Steps</span>
               </div>
               <div className="w-1 h-1 bg-slate-200 rounded-full" />
               <div className="flex items-center gap-1 text-slate-400">
                  <Star className="w-3.5 h-3.5 fill-slate-300" />
                  <span className="text-[10px] font-black uppercase tracking-tighter">{quiz.totalPoints} XP</span>
               </div>
            </div>

            <div className="mt-auto pt-6 border-t border-slate-50 flex items-center justify-between relative z-10">
               <span className="text-[9px] font-black text-indigo-500 uppercase tracking-widest">{myAttempt ? 'Retake Challenge' : 'Begin Quest'}</span>
               <div className={`w-10 h-10 rounded-xl flex items-center justify-center transition-all ${myAttempt ? 'bg-emerald-50 text-emerald-600' : 'bg-indigo-50 text-indigo-600 group-hover:bg-indigo-600 group-hover:text-white group-hover:scale-110'}`}>
                  <ArrowRight className="w-5 h-5" />
               </div>
            </div>
            
            {myAttempt && (
              <div className="absolute bottom-4 right-12 text-emerald-100 opacity-20 pointer-events-none">
                <CheckCircle2 className="w-24 h-24" />
              </div>
            )}
          </motion.button>
        );
      }) : (
        <div className="col-span-full py-24 text-center">
           <div className="w-24 h-24 bg-slate-100 rounded-[32px] flex items-center justify-center mx-auto mb-6">
              <HelpCircle className="w-12 h-12 text-slate-300 opacity-50" />
           </div>
           <p className="text-[10px] font-black text-slate-400 uppercase tracking-[0.4em]">Ancient Vault Empty</p>
           <p className="text-sm font-bold text-slate-300 mt-2">No challenges have been forged for this module yet.</p>
        </div>
      )}
    </div>
  );
};
