import React, { useState } from 'react';
import { motion } from 'motion/react';
import { useAuth } from '../context/AuthContext';
import { 
  Zap, 
  GraduationCap, 
  Users, 
  ChevronLeft, 
  ArrowRight, 
  Sparkles 
} from 'lucide-react';

export const AuthEntrance = () => {
  const { signInEmail, signUpEmail, signIn } = useAuth();
  const [view, setView] = useState<'splash' | 'login' | 'signup'>('splash');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [role, setRole] = useState<'student' | 'teacher'>('student');
  const [syllabus, setSyllabus] = useState<'CBSE' | 'TN State Board'>('CBSE');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      if (view === 'login') {
        await signInEmail(email, password);
      } else {
        await signUpEmail(email, password, name, role, syllabus);
      }
    } catch (err: any) {
      setError(err.message || 'Authentication failed');
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleSignIn = async (selectedRole: 'student' | 'teacher' = role) => {
    setLoading(true);
    setError('');
    try {
      setRole(selectedRole);
      await signIn(selectedRole);
    } catch (err: any) {
      setError(err.message || 'Google Sign-in failed');
    } finally {
      setLoading(false);
    }
  };

  if (view === 'splash') {
    return (
      <div className="min-h-screen bg-white flex flex-col items-center justify-center p-8">
        <motion.div 
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="flex flex-col items-center text-center max-w-md w-full"
        >
          <div className="w-32 h-32 bg-slate-800 rounded-[40px] flex items-center justify-center shadow-2xl mb-8 rotate-3">
            <div className="w-24 h-24 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-[32px] flex items-center justify-center rotate-6">
              <Zap className="text-white fill-white w-12 h-12" />
            </div>
          </div>
          <h1 className="text-5xl font-black text-slate-900 tracking-tighter mb-4 uppercase italic">Learn Boost</h1>
          <p className="text-slate-400 font-medium mb-12 text-lg">Your interactive gateway to mathematical mastery.</p>
          
          <div className="grid grid-cols-2 gap-4 w-full mb-8">
             <button 
               onClick={() => { setRole('student'); setView('signup'); }}
               className="group relative bg-[#f8fafc] p-6 rounded-[32px] border-2 border-slate-100 hover:border-indigo-300 transition-all text-left overflow-hidden"
             >
                <div className="absolute top-0 right-0 w-24 h-24 bg-indigo-500/5 -mr-12 -mt-12 rounded-full" />
                <GraduationCap className="w-8 h-8 text-indigo-500 mb-4 group-hover:scale-110 transition-transform" />
                <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">Join as</p>
                <p className="text-lg font-black text-slate-900 uppercase italic">Student</p>
             </button>
             <button 
               onClick={() => { setRole('teacher'); setView('signup'); }}
               className="group relative bg-[#f8fafc] p-6 rounded-[32px] border-2 border-slate-100 hover:border-emerald-300 transition-all text-left overflow-hidden"
             >
                <div className="absolute top-0 right-0 w-24 h-24 bg-emerald-500/5 -mr-12 -mt-12 rounded-full" />
                <Users className="w-8 h-8 text-emerald-500 mb-4 group-hover:scale-110 transition-transform" />
                <p className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">Join as</p>
                <p className="text-lg font-black text-slate-900 uppercase italic">Teacher</p>
             </button>
          </div>

          <button 
            onClick={() => setView('login')}
            className="w-full text-slate-400 font-black text-[10px] uppercase tracking-[0.3em] py-4 hover:text-indigo-600 transition-colors"
          >
            I already have an account
          </button>
        </motion.div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#f8fafc] flex items-center justify-center p-6">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-md bg-white rounded-[40px] p-10 shadow-2xl shadow-indigo-100/30 border border-slate-100"
      >
        <button 
           onClick={() => setView('splash')}
           className="mb-8 text-slate-400 hover:text-slate-900 transition-colors flex items-center gap-2 font-black text-[10px] uppercase tracking-widest"
        >
           <ChevronLeft className="w-4 h-4" /> Back
        </button>

        <header className="mb-10">
           <h1 className="text-4xl font-black text-slate-900 tracking-tighter mb-2">{view === 'login' ? 'Welcome Back!' : 'Create Account'}</h1>
           <p className="text-slate-400 font-medium">{view === 'login' ? 'Let\'s pick up where you left off.' : 'Start your mathematical adventure today.'}</p>
        </header>

        {view === 'login' && (
          <div className="space-y-4 mb-8">
            <button 
              onClick={() => handleGoogleSignIn('student')}
              disabled={loading}
              className="w-full bg-white border-2 border-slate-50 flex items-center justify-between px-6 py-4 rounded-2xl hover:bg-slate-50 transition-all shadow-sm group"
            >
              <div className="flex items-center gap-4">
                <svg className="w-5 h-5" viewBox="0 0 24 24">
                  <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z" fill="#4285F4"/>
                  <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                  <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05"/>
                  <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
                </svg>
                <span className="font-black text-slate-600 text-sm">Login as Student</span>
              </div>
              <ArrowRight className="w-4 h-4 text-slate-200 group-hover:text-indigo-500 transition-colors" />
            </button>

            <button 
              onClick={() => handleGoogleSignIn('teacher')}
              disabled={loading}
              className="w-full bg-slate-900 border-2 border-slate-900 flex items-center justify-between px-6 py-4 rounded-2xl hover:bg-slate-800 transition-all shadow-sm group"
            >
              <div className="flex items-center gap-4">
                <div className="w-5 h-5 flex items-center justify-center">
                  <Sparkles className="w-4 h-4 text-emerald-400" />
                </div>
                <span className="font-black text-white text-sm">Login as Teacher</span>
              </div>
              <ArrowRight className="w-4 h-4 text-slate-500 group-hover:text-emerald-400 transition-colors" />
            </button>
          </div>
        )}

        {view === 'login' && (
          <div className="flex items-center gap-4 mb-8">
            <div className="flex-1 h-px bg-slate-100" />
            <span className="text-[10px] font-black text-slate-300 uppercase tracking-widest">or email</span>
            <div className="flex-1 h-px bg-slate-100" />
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-6">
          {view === 'signup' && (
            <div className="space-y-2">
              <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest ml-1">Full Name</label>
              <input 
                type="text" 
                placeholder="Math Explorer"
                className="w-full bg-slate-50 border-2 border-slate-50 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-indigo-100 transition-all font-bold placeholder:text-slate-300"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
              />
            </div>
          )}

          <div className="space-y-2">
            <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest ml-1">Email Address</label>
            <input 
              type="email" 
              placeholder="hello@math.com"
              className="w-full bg-slate-50 border-2 border-slate-50 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-indigo-100 transition-all font-bold placeholder:text-slate-300"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="space-y-2">
            <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest ml-1">Password</label>
            <input 
              type="password" 
              placeholder="Password"
              className="w-full bg-slate-50 border-2 border-slate-50 rounded-2xl px-6 py-4 text-sm focus:outline-none focus:border-indigo-100 transition-all font-bold placeholder:text-slate-300"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          {view === 'signup' && (
            <>
              <div className="space-y-2">
                <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest ml-1">Who are you?</label>
                <div className="grid grid-cols-2 gap-4">
                  {['student', 'teacher'].map(r => (
                    <button 
                      key={r}
                      type="button"
                      onClick={() => setRole(r as any)}
                      className={`py-4 rounded-2xl font-black text-[10px] uppercase tracking-widest border-2 transition-all ${
                        role === r ? 'border-[#2e5b82] bg-indigo-50 text-[#2e5b82]' : 'border-slate-50 bg-slate-50 text-slate-400'
                      }`}
                    >
                      {r}
                    </button>
                  ))}
                </div>
              </div>

              <div className="space-y-2">
                <label className="text-[10px] font-black text-slate-500 uppercase tracking-widest ml-1">Learning Stream</label>
                <div className="grid grid-cols-1 gap-3">
                  {['CBSE', 'TN State Board'].map(s => (
                    <button 
                      key={s}
                      type="button"
                      onClick={() => setSyllabus(s as any)}
                      className={`py-4 rounded-2xl text-[10px] font-black uppercase tracking-widest border-2 transition-all flex items-center justify-center gap-3 ${
                        syllabus === s ? 'border-indigo-600 bg-indigo-50 text-indigo-700' : 'border-slate-50 text-slate-400 bg-slate-50'
                      }`}
                    >
                      {s === 'CBSE' ? 'CBSE' : 'TN'} {s}
                    </button>
                  ))}
                </div>
              </div>
            </>
          )}

          {error && <p className="text-rose-500 text-[10px] font-black uppercase tracking-widest bg-rose-50 p-4 rounded-xl border border-rose-100">{error}</p>}

          <button 
            type="submit" 
            disabled={loading}
            className="w-full duo-button-indigo disabled:opacity-50"
          >
            {loading ? 'Processing...' : (view === 'login' ? 'Login' : 'Create Account')}
          </button>
        </form>

        <div className="mt-8 text-center">
           <button 
             onClick={() => setView(view === 'login' ? 'signup' : 'login')}
             className="text-[10px] font-black text-slate-400 uppercase tracking-widest hover:text-indigo-600 transition-colors"
           >
             {view === 'login' ? 'Don\'t have an account? Sign Up' : 'Already have an account? Login'}
           </button>
        </div>
      </motion.div>
    </div>
  );
};
