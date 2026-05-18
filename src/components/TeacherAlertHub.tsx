import React, { useState, useEffect } from 'react';
import { useEducation, TeacherAlert } from '../hooks/useEducation';
import { AlertTriangle, MessageCircle, User } from 'lucide-react';

export const TeacherAlertHub = () => {
  const { getTeacherAlerts } = useEducation();
  const [alerts, setAlerts] = useState<TeacherAlert[]>([]);

  useEffect(() => {
    return getTeacherAlerts(setAlerts);
  }, [getTeacherAlerts]);

  return (
    <div className="bg-rose-50 border border-rose-100 rounded-2xl p-6 mb-8 overflow-hidden relative">
      <div className="absolute top-0 right-0 p-4 opacity-5">
        <AlertTriangle className="w-32 h-32 text-rose-500" />
      </div>
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-2">
          <div className="p-2 bg-rose-500 text-white rounded-lg animate-pulse">
            <AlertTriangle className="w-4 h-4" />
          </div>
          <div>
            <h2 className="text-xs font-black uppercase tracking-widest text-rose-700">Priority Intervention Matrix</h2>
            <p className="text-[10px] font-bold text-rose-600/60 uppercase">Real-time identification of learning gaps</p>
          </div>
        </div>
        <span className="text-[10px] font-black text-rose-500 bg-rose-100 px-2 py-1 rounded uppercase">{alerts.length} Pending Actions</span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {alerts.length > 0 ? alerts.map(alert => (
          <div key={alert.id} className="bg-white border border-rose-100 p-4 rounded-xl flex items-start gap-4 shadow-sm group hover:border-rose-300 transition-all">
            <div className={`p-2 rounded-lg shrink-0 ${alert.type === 'question' ? 'bg-indigo-100 text-indigo-600' : alert.severity === 'high' ? 'bg-rose-100 text-rose-600' : 'bg-amber-100 text-amber-600'}`}>
               {alert.type === 'question' ? <MessageCircle className="w-4 h-4" /> : <User className="w-4 h-4" />}
            </div>
            <div className="flex-1 min-w-0">
               <div className="flex items-center justify-between gap-2 mb-1">
                  <p className="text-xs font-black text-slate-900 truncate uppercase">{alert.userName}</p>
                  <span className={`text-[8px] font-black shrink-0 ${alert.type === 'question' ? 'text-indigo-500' : 'text-slate-400'}`}>
                    {alert.type === 'question' ? 'QUESTION' : 'NOW'}
                  </span>
               </div>
               {alert.type === 'question' && (
                 <p className="text-[8px] font-black text-indigo-400 uppercase tracking-widest mb-1 truncate">
                   {alert.grade} • {alert.syllabus} • {alert.subject || alert.courseTitle}
                 </p>
               )}
               <p className="text-[10px] text-slate-500 leading-relaxed line-clamp-2">{alert.message}</p>
               <div className="mt-3 flex gap-2">
                  <button className="flex-1 py-1.5 bg-slate-900 text-white rounded text-[8px] font-black uppercase tracking-widest hover:bg-indigo-600 transition-colors">
                    {alert.type === 'question' ? 'Respond' : 'Intervene'}
                  </button>
                  <button className="flex-1 py-1.5 bg-slate-50 text-slate-400 rounded text-[8px] font-black uppercase tracking-widest hover:bg-slate-100 transition-colors">Dismiss</button>
               </div>
            </div>
          </div>
        )) : (
          <div className="col-span-2 py-12 text-center">
             <p className="text-[10px] font-black text-rose-300 uppercase tracking-[0.3em]">No immediate interventions required</p>
          </div>
        )}
      </div>
    </div>
  );
};
