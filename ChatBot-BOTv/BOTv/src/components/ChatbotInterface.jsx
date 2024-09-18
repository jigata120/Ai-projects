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
   
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [prompt, setPrompt] = useState('');
  const [wordCountPrompt, setWordCountPrompt] = useState(0);
  const [settings, setSettings] = useState({
    botName: 'AI Assistant',
    contextLength: '500',
    contextData: '',
    outputLength: '50',
    conversationId: '',
    apiKey: '',
  });
  const promptWordLimit = 100;

  const handleSend = async () => {
    if (prompt.trim()) {
      const localMessages = [...messages, { text: prompt, isUser: true }];
      setMessages(localMessages);
  
      const data = {
        chatbot: { settings },
        ui_messages: localMessages,
      };
  
      try {
        const response = await postData("http://127.0.0.1:8000/settings/", data);
   
        setMessages(messages => [...messages, { text: response.response, isUser: false }]);
      } catch (error) {
        console.error('Failed to send request:', error);
      }
 
      setPrompt('');
    }
  };

  const handleApplySettings = useCallback((newSettings) => {
    setSettings(newSettings);
  }, []);

  const validateAndTrimContent = (content, promptWordLimit) => {
    const words = content.trim().split(/\s+/);
    if (words.length > promptWordLimit) {
      return words.slice(0, promptWordLimit).join(' ');
    }
    return content;
  };

  const handlePromptChange = (event) => {
    const newValue = event.target.value;
    const trimmedValue = validateAndTrimContent(newValue, promptWordLimit);
    setPrompt(trimmedValue);
    setWordCountPrompt(trimmedValue.trim().split(/\s+/).length);
  };
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
        <div className="p-4 pb-0 border-t">
          <div className="flex items-center">
            <input
              type="text"
              value={prompt}
              onChange={handlePromptChange}
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
          <div className="ml-2  text-sm text-gray-600">
            { promptWordLimit -wordCountPrompt} words remaining
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