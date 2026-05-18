import React, { useState, useEffect } from 'react';
import { useEducation } from '../hooks/useEducation';
import { Check, FileText } from 'lucide-react';

export const TeacherReview = ({ courseId }: { courseId: string }) => {
  const { getTeacherReviews, gradeAttempt } = useEducation();
  const [reviews, setReviews] = useState<any[]>([]);
  const [selectedReview, setSelectedReview] = useState<any>(null);
  const [feedback, setFeedback] = useState('');
  const [bonusPoints, setBonusPoints] = useState(0);

  useEffect(() => {
    return getTeacherReviews(courseId, setReviews);
  }, [courseId, getTeacherReviews]);

  const handleGrade = async () => {
    if (!selectedReview) return;
    await gradeAttempt(selectedReview.userId, selectedReview.id, bonusPoints, feedback);
    setSelectedReview(null);
    setFeedback('');
    setBonusPoints(0);
  };

  if (reviews.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-20 text-slate-300 gap-4">
         <Check className="w-12 h-12 opacity-20" />
         <p className="text-[10px] font-black uppercase tracking-[0.3em]">All logic gates verified</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
       <div className="lg:col-span-4 space-y-2">
          <h3 className="text-[10px] font-black uppercase text-slate-400 mb-4">Pending Verifications</h3>
          {reviews.map(rev => (
            <button 
              key={rev.id} 
              onClick={() => setSelectedReview(rev)}
              className={`w-full text-left p-4 rounded-xl border transition-all ${
                selectedReview?.id === rev.id ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white border-slate-100 hover:border-slate-300'
              }`}
            >
               <p className="text-[10px] font-black uppercase opacity-60 mb-1">Student UID: {rev.userId.substring(0, 8)}</p>
               <p className="text-xs font-bold truncate">Quiz ID: {rev.quizId}</p>
            </button>
          ))}
       </div>

       <div className="lg:col-span-8">
          {selectedReview ? (
            <div className="bg-white rounded-2xl border border-slate-200 p-8 space-y-6">
               <header className="flex justify-between items-center pb-6 border-b border-slate-100">
                  <div>
                    <h2 className="text-lg font-black text-slate-900 uppercase">Attempt Review</h2>
                    <p className="text-xs text-slate-400">Current Auto-Score: {selectedReview.score}/{selectedReview.totalPossible}</p>
                  </div>
                  <div className="bg-amber-50 text-amber-600 px-3 py-1 rounded-full text-[10px] font-black">PENDING MANUAL REVIEW</div>
               </header>

               <div className="space-y-4">
                  <h4 className="text-[10px] font-black uppercase text-slate-400">Student Responses</h4>
                  {Object.entries(selectedReview.answers || {}).map(([qId, ans]: [string, any]) => (
                    <div key={qId} className="p-4 bg-slate-50 rounded-xl border border-slate-100">
                       <p className="text-[10px] font-bold text-slate-400 uppercase mb-1">Question {qId}</p>
                       <p className="text-sm text-slate-700">{String(ans)}</p>
                    </div>
                  ))}
               </div>

               <div className="space-y-4 pt-6 border-t border-slate-100">
                  <div>
                    <label className="text-[10px] font-black uppercase text-slate-400 block mb-2">Subjective Points Awarded</label>
                    <input 
                      type="number" 
                      className="w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-3 text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500"
                      value={bonusPoints}
                      onChange={(e) => setBonusPoints(Number(e.target.value))}
                    />
                  </div>
                  <div>
                    <label className="text-[10px] font-black uppercase text-slate-400 block mb-2">Pedagogical Feedback</label>
                    <textarea 
                      className="w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-3 text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500 min-h-[100px] resize-none"
                      placeholder="Guidance for the student..."
                      value={feedback}
                      onChange={(e) => setFeedback(e.target.value)}
                    />
                  </div>
                  <button 
                    onClick={handleGrade}
                    className="w-full bg-slate-950 text-white py-4 rounded-xl font-black uppercase text-[10px] tracking-widest hover:bg-indigo-600 transition-all"
                  >
                    Commit Verification
                  </button>
               </div>
            </div>
          ) : (
            <div className="h-full flex flex-col items-center justify-center text-slate-300 opacity-50">
               <FileText className="w-12 h-12 mb-4" />
               <p className="text-[10px] font-black uppercase">Awaiting Selection</p>
            </div>
          )}
       </div>
    </div>
  );
};
