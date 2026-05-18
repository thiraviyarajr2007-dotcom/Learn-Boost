import React, { Component, ErrorInfo, ReactNode } from 'react';
import { AlertTriangle, RotateCcw } from 'lucide-react';

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

export class ErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
    error: null
  };

  public static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Uncaught error:', error, errorInfo);
  }

  public render() {
    if (this.state.hasError) {
      return (
        <div className="min-h-screen bg-slate-50 flex items-center justify-center p-6">
          <div className="max-w-md w-full bg-white rounded-[40px] p-10 shadow-2xl border border-rose-100 text-center">
            <div className="w-20 h-20 bg-rose-50 rounded-3xl flex items-center justify-center mx-auto mb-8">
              <AlertTriangle className="w-10 h-10 text-rose-500" />
            </div>
            <h1 className="text-2xl font-black text-slate-900 mb-4 uppercase italic">Application Error</h1>
            <p className="text-slate-500 text-sm mb-6 leading-relaxed">
              We encountered an issue during rendering. Please try reloading. If this persists, clear your browser cache.
            </p>
            
            <div className="bg-slate-50 p-4 rounded-2xl mb-8 text-left overflow-auto max-h-40 border border-slate-100">
              <p className="text-[10px] font-black text-slate-400 uppercase mb-2">Technical Details:</p>
              <code className="text-[10px] text-rose-600 font-mono break-all">
                {this.state.error?.message || 'Unknown render error'}
              </code>
            </div>

            <button 
              onClick={() => {
                localStorage.clear();
                window.location.reload();
              }}
              className="w-full bg-indigo-600 text-white py-4 rounded-2xl font-black uppercase text-xs tracking-widest hover:bg-indigo-700 transition-all flex items-center justify-center gap-2"
            >
              <RotateCcw className="w-5 h-5" />
              Reload & Clear Cache
            </button>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
