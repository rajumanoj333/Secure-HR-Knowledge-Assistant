import React, { useState } from 'react';
import axios from 'axios';
import { Send, User, Bot, Lock } from 'lucide-react';

function App() {
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState<{ role: 'user' | 'bot'; content: string }[]>([]);
  const [loading, setLoading] = useState(false);
  const [userId, setUserId] = useState('bob'); // Default mock user

  const handleSend = async () => {
    if (!query.trim()) return;

    const newMessages = [...messages, { role: 'user' as const, content: query }];
    setMessages(newMessages);
    setQuery('');
    setLoading(true);

    try {
      const response = await axios.post('http://localhost:8000/chat', {
        query,
        user_id: userId,
      });

      setMessages([...newMessages, { role: 'bot', content: response.data.response }]);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages([...newMessages, { role: 'bot', content: 'Error: Could not connect to backend.' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100 font-sans">
      <header className="bg-white shadow-sm p-4 flex justify-between items-center">
        <h1 className="text-xl font-bold text-blue-600 flex items-center gap-2">
          <Lock className="w-6 h-6" /> Secure HR Assistant
        </h1>
        <div className="flex items-center gap-2">
          <span className="text-sm text-gray-600">Acting as:</span>
          <select 
            value={userId} 
            onChange={(e) => setUserId(e.target.value)}
            className="border rounded p-1 text-sm bg-gray-50"
          >
            <option value="alice">Alice (HR Manager)</option>
            <option value="bob">Bob (Employee)</option>
          </select>
        </div>
      </header>

      <main className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[70%] p-3 rounded-lg flex gap-3 ${
              msg.role === 'user' ? 'bg-blue-600 text-white' : 'bg-white border text-gray-800'
            }`}>
              {msg.role === 'bot' ? <Bot className="w-5 h-5 shrink-0" /> : <User className="w-5 h-5 shrink-0" />}
              <p>{msg.content}</p>
            </div>
          </div>
        ))}
        {loading && (
          <div className="flex justify-start">
            <div className="bg-white border p-3 rounded-lg animate-pulse text-gray-400">
              Assistant is thinking...
            </div>
          </div>
        )}
      </main>

      <footer className="p-4 bg-white border-t">
        <div className="max-w-4xl mx-auto flex gap-2">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
            placeholder="Ask an HR question..."
            className="flex-1 border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={handleSend}
            disabled={loading}
            className="bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700 disabled:opacity-50"
          >
            <Send className="w-5 h-5" />
          </button>
        </div>
      </footer>
    </div>
  );
}

export default App;
