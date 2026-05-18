import React from 'react';
import { motion } from 'motion/react';
import { Zap } from 'lucide-react';

export const LearnBoostMascot = ({ mood = 'happy' }: { mood?: 'happy' | 'excited' | 'thinking' }) => (
  <motion.div 
    animate={{ 
      y: [0, -10, 0],
      rotateX: [0, 5, 0],
      rotateY: [0, -5, 0]
    }}
    transition={{ repeat: Infinity, duration: 4, ease: "easeInOut" }}
    className="relative w-28 h-28 perspective-1000"
  >
    {/* 3D Depth Layers */}
    <div className="absolute inset-0 bg-slate-900 rounded-[32%] translate-y-2 blur-sm opacity-20" />
    <div className="absolute inset-0 bg-indigo-700 rounded-[28%] rotate-6 shadow-2xl translate-z-[-10px]" />
    <motion.div 
      className="absolute inset-0 bg-slate-800 rounded-[24%] -rotate-3 border-2 border-slate-700 flex flex-col items-center justify-center shadow-xl preserve-3d"
      style={{ transform: 'translateZ(10px)' }}
    >
      {/* Face */}
      <div className="flex gap-5 mb-3">
        <motion.div 
          animate={mood === 'happy' ? { scaleY: [1, 0.1, 1], y: [0, -1, 0] } : mood === 'thinking' ? { x: [-1, 1, -1] } : { scale: [1, 1.3, 1] }}
          transition={{ repeat: Infinity, duration: mood === 'happy' ? 4 : 2 }}
          className="w-3 h-3 bg-emerald-400 rounded-full shadow-[0_0_10px_rgba(52,211,153,0.5)]" 
        />
        <motion.div 
          animate={mood === 'happy' ? { scaleY: [1, 0.1, 1], y: [0, -1, 0] } : mood === 'thinking' ? { x: [-1, 1, -1] } : { scale: [1, 1.3, 1] }}
          transition={{ repeat: Infinity, duration: mood === 'happy' ? 4 : 2 }}
          className="w-3 h-3 bg-emerald-400 rounded-full shadow-[0_0_10px_rgba(52,211,153,0.5)]" 
        />
      </div>
      <motion.div 
        animate={mood === 'excited' ? { scaleX: [1, 1.2, 1] } : {}}
        className={`w-8 h-4 border-b-4 border-emerald-400 ${mood === 'happy' || mood === 'excited' ? 'rounded-full' : 'w-4 h-0.5 bg-emerald-400 rounded-none'}`} 
      />
      
      {/* 3D Reflection */}
      <div className="absolute top-2 left-4 w-12 h-4 bg-white/5 rounded-full blur-md" />
    </motion.div>
    
    <motion.div 
      animate={{ scale: [1, 1.2, 1], rotate: [0, 360] }}
      transition={{ repeat: Infinity, duration: 5, ease: "linear" }}
      className="absolute -top-3 -right-3 bg-indigo-500 w-10 h-10 rounded-2xl flex items-center justify-center shadow-lg border-2 border-white z-20"
    >
      <Zap className="w-5 h-5 text-white fill-white" />
    </motion.div>
    
    {mood === 'thinking' && (
      <motion.div 
        initial={{ opacity: 0, scale: 0 }}
        animate={{ opacity: 1, scale: 1 }}
        className="absolute -top-12 left-0 bg-white p-2 rounded-xl border-2 border-slate-100 shadow-lg text-xs font-black text-indigo-500"
      >
        Hmm...
      </motion.div>
    )}
  </motion.div>
);
