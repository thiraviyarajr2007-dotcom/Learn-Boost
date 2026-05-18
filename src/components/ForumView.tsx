import React, { useState, useEffect } from 'react';
import { useEducation } from '../hooks/useEducation';
import { 
  Plus, 
  Search as SearchIcon, 
  MessageSquare, 
  User, 
  ChevronRight, 
  Send 
} from 'lucide-react';

export const ForumView = ({ courseId }: { courseId: string }) => {
  const { getForumPosts, createForumPost, getForumReplies, addForumReply } = useEducation();
  const [posts, setPosts] = useState<any[]>([]);
  const [selectedPost, setSelectedPost] = useState<any>(null);
  const [replies, setReplies] = useState<any[]>([]);
  const [newPostTitle, setNewPostTitle] = useState('');
  const [newPostContent, setNewPostContent] = useState('');
  const [newReply, setNewReply] = useState('');
  const [isPosting, setIsPosting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    return getForumPosts(courseId, setPosts);
  }, [courseId, getForumPosts]);

  const filteredPosts = posts.filter(p => 
    p.title.toLowerCase().includes(searchTerm.toLowerCase()) || 
    p.content.toLowerCase().includes(searchTerm.toLowerCase())
  );

  useEffect(() => {
    if (selectedPost) {
      return getForumReplies(courseId, selectedPost.id, setReplies);
    }
  }, [selectedPost, courseId, getForumReplies]);

  const handleCreatePost = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newPostTitle.trim() || !newPostContent.trim()) return;
    setIsPosting(true);
    setError(null);
    try {
      await createForumPost(courseId, newPostTitle, newPostContent, 'question');
      setNewPostTitle('');
      setNewPostContent('');
      setIsPosting(false);
    } catch (err) {
      console.error('Failed to create post:', err);
      setError('Could not create thread. Please try again.');
      setIsPosting(false);
    }
  };

  const handleAddReply = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newReply.trim() || !selectedPost) return;
    setError(null);
    try {
      await addForumReply(courseId, selectedPost.id, newReply);
      setNewReply('');
    } catch (err) {
      console.error('Failed to add reply:', err);
      setError('Could not post reply. Please try again.');
    }
  };

  return (
    <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 min-h-[500px]">
      <div className="lg:col-span-4 border-r border-slate-100 pr-4 space-y-4">
        <div className="space-y-4 mb-6">
           <div className="flex items-center justify-between">
              <h3 className="text-xs font-black uppercase tracking-widest text-slate-400">Discussion Threads</h3>
              <button 
                onClick={() => setIsPosting(true)}
                className="p-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
              >
                <Plus className="w-4 h-4" />
              </button>
           </div>
           <div className="relative">
              <SearchIcon className="absolute left-3 top-1/2 -translate-y-1/2 w-3 h-3 text-slate-400" />
              <input 
                type="text" 
                placeholder="Search threads..." 
                className="w-full pl-8 pr-4 py-2 bg-slate-50 border border-slate-100 rounded-lg text-[10px] focus:outline-none focus:ring-1 focus:ring-indigo-500 transition-all font-medium"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
           </div>
        </div>

        {error && (
          <div className="p-3 mb-4 bg-rose-50 border border-rose-200 text-rose-600 rounded-lg text-[10px] font-bold text-center">
            {error}
          </div>
        )}

        {isPosting && (
          <form onSubmit={handleCreatePost} className="bg-white p-4 rounded-xl border-2 border-indigo-100 shadow-sm space-y-3 mb-6">
             <input 
               type="text" 
               placeholder="Thread Title" 
               className="w-full text-xs font-bold border-b border-slate-100 pb-2 focus:outline-none focus:border-indigo-500"
               value={newPostTitle}
               onChange={(e) => setNewPostTitle(e.target.value)}
             />
             <textarea 
               placeholder="What's on your mind?" 
               className="w-full text-xs min-h-[80px] focus:outline-none resize-none"
               value={newPostContent}
               onChange={(e) => setNewPostContent(e.target.value)}
             />
             <div className="flex justify-end gap-2">
                <button type="button" onClick={() => setIsPosting(false)} className="text-[10px] font-black uppercase text-slate-400">Cancel</button>
                <button type="submit" className="bg-slate-900 text-white px-3 py-1 rounded text-[10px] font-black uppercase">Post Thread</button>
             </div>
          </form>
        )}

        <div className="space-y-2 overflow-y-auto max-h-[600px] pr-2 custom-scrollbar">
           {filteredPosts.map(post => (
             <button 
               key={post.id}
               onClick={() => setSelectedPost(post)}
               className={`w-full text-left p-4 rounded-xl border transition-all ${
                 selectedPost?.id === post.id ? 'bg-indigo-50 border-indigo-200' : 'bg-white border-slate-100 hover:border-slate-300'
               }`}
             >
                <h4 className="text-xs font-black text-slate-900 mb-1 uppercase italic">{post.title}</h4>
                <div className="flex items-center gap-2">
                   <div className="w-4 h-4 bg-slate-100 rounded-full flex items-center justify-center">
                      <User className="w-2 h-2 text-slate-400" />
                   </div>
                   <span className="text-[8px] font-bold text-slate-400 uppercase tracking-tighter">By Student • {post.replyCount || 0} Replies</span>
                </div>
             </button>
           ))}
        </div>
      </div>

      <div className="lg:col-span-8">
         {selectedPost ? (
           <div className="flex flex-col h-full bg-white rounded-2xl border border-slate-100 overflow-hidden">
              <header className="p-6 border-b border-slate-50 bg-slate-50/50">
                 <div className="flex items-center gap-2 mb-2">
                    <span className="text-[8px] font-black bg-indigo-600 text-white px-2 py-0.5 rounded-full uppercase tracking-widest">Question</span>
                    <span className="text-[8px] font-bold text-slate-400 uppercase">#{selectedPost.id.substring(0,6)}</span>
                 </div>
                 <h2 className="text-xl font-black text-slate-900 uppercase italic">{selectedPost.title}</h2>
                 <p className="mt-4 text-sm text-slate-600 leading-relaxed font-medium">{selectedPost.content}</p>
              </header>

              <div className="flex-1 overflow-y-auto p-6 space-y-6 custom-scrollbar">
                 <h3 className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Responses</h3>
                 {replies.map(reply => (
                   <div key={reply.id} className="flex gap-4">
                      <div className="w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center shrink-0">
                         <User className="w-4 h-4 text-slate-400" />
                      </div>
                      <div className="flex-1 bg-slate-50 rounded-2xl rounded-tl-none p-4">
                         <p className="text-xs text-slate-700 font-medium leading-relaxed">{reply.content}</p>
                         <div className="mt-2 flex items-center gap-2">
                            <span className="text-[8px] font-black text-slate-400 uppercase">{reply.userName || 'Anonymous'}</span>
                            <div className="w-1 h-1 bg-slate-200 rounded-full" />
                            <span className="text-[8px] font-bold text-slate-300 uppercase">2h ago</span>
                         </div>
                      </div>
                   </div>
                 ))}
              </div>

              <footer className="p-4 bg-white border-t border-slate-100">
                 <form onSubmit={handleAddReply} className="relative">
                    <input 
                      type="text" 
                      placeholder="Add to the conversation..." 
                      className="w-full pl-6 pr-12 py-4 bg-slate-50 border-2 border-slate-50 rounded-2xl text-xs focus:outline-none focus:border-indigo-100 transition-all font-medium"
                      value={newReply}
                      onChange={(e) => setNewReply(e.target.value)}
                    />
                    <button type="submit" className="absolute right-3 top-1/2 -translate-y-1/2 p-2 text-indigo-600 hover:text-indigo-800 transition-colors">
                       <Send className="w-4 h-4" />
                    </button>
                 </form>
              </footer>
           </div>
         ) : (
           <div className="h-full flex flex-col items-center justify-center text-slate-300 opacity-50 bg-slate-50/30 rounded-2xl border-2 border-dashed border-slate-100">
              <MessageSquare className="w-16 h-16 mb-4" />
              <p className="text-[10px] font-black uppercase tracking-[0.3em]">Select a thread to engage</p>
           </div>
         )}
      </div>
    </div>
  );
};
