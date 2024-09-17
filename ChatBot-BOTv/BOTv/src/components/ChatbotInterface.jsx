import React, { useState, useCallback } from 'react';
import { Send, User, Bot, Settings } from 'lucide-react';
import { BotSettings } from './BotSettings';
import { postData } from '../Api';


const ChatMessage = ({ message, isUser }) => (
  <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
    <div className={`flex items-start ${isUser ? 'flex-row-reverse' : 'flex-row'}`}>
      <div className={`rounded-full p-2 ${isUser ? 'bg-blue-500' : 'bg-gray-300'}`}>
        {isUser ? <User size={24} color="white" /> : <Bot size={24} color="black" />}
      </div>
      <div className={`max-w-xs mx-2 p-3 rounded-lg ${isUser ? 'bg-blue-100' : 'bg-gray-100'}`}>
        <p className="text-sm">{message}</p>
      </div>
    </div>
  </div>
);


 

const ChatbotInterface = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [settings, setSettings] = useState({
    botName: 'AI Assistant',
    contextLength: '500',
    contextData: '',
    outputLength: '50',
    conversationId: '',
    apiKey: '',
  });

  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, { text: input, isUser: true }]);
      // Here you would typically call your AI service API
      postData("http://127.0.0.1:8000/settings/",settings)
      
      setMessages(msgs => [...msgs, { text: `You said: ${input}`, isUser: false }]);
      
      setInput('');
    }
  };

  const handleApplySettings = useCallback((newSettings) => {
    setSettings(newSettings);
  }, []);
  console.log(settings);
  return (
    <div className="flex flex-col h-screen max-w-md mx-auto">
      <div className="bg-white shadow-lg rounded-lg flex flex-col h-full">
        <div className="p-4 bg-blue-500 text-white font-bold rounded-t-lg flex justify-between items-center">
          <span>{settings.botName}</span>
          <button onClick={() => setIsSettingsOpen(true)} className="text-white">
            <Settings size={20} />
          </button>
        </div>
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.map((msg, index) => (
            <ChatMessage key={index} message={msg.text} isUser={msg.isUser} />
          ))}
        </div>
        <div className="p-4 border-t">
          <div className="flex items-center">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onClick={(e) => e.key === 'Enter' && handleSend()}
              className="flex-1 border rounded-l-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Type your message..."
            />
            <button
              onClick={handleSend}
              className="bg-blue-500 text-white rounded-r-lg px-4 py-2 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <Send size={20} />
            </button>
          </div>
        </div>
      </div>
      <BotSettings
        isOpen={isSettingsOpen}
        onClose={() => setIsSettingsOpen(false)}
        settings={settings}
        onApply={handleApplySettings}
      />
    </div>
  );
};

export default ChatbotInterface;