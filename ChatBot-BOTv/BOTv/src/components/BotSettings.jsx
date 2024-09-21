import React, { useState, useCallback } from 'react';
import {X, Check } from 'lucide-react';
import WordLimitTextarea from './WordLimitTextarea';
export const BotSettings = ({ isOpen, onClose, settings, onSettingsChange, onApply,hasMemory }) => {
    const [localSettings, setLocalSettings] = useState(settings);
    const [hasChanges, setHasChanges] = useState(false);
  
    const handleLocalChange = (key, value) => {
        setLocalSettings((prev) => ({ ...prev, [key]: value }));
        setHasChanges(true);        
      };
  
    const handleApply = useCallback(() => {
      onApply(localSettings);
      setHasChanges(false);
    }, [localSettings, onApply]);
  
    if (!isOpen) return null;
  
    return (
      <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
        <div className="bg-white p-6 rounded-lg w-96">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-bold">Bot Configurations</h2>
            {hasChanges && (
              <button
                onClick={handleApply}
                className="bg-green-500 text-white px-3 py-1 rounded-md hover:bg-green-600 transition-colors duration-200 flex items-center"
              >
                <Check size={16} className="mr-1" /> Apply
              </button>
            )}
            <button onClick={onClose} className="text-gray-500 hover:text-gray-700">
              <X size={24} />
            </button>
          </div>
          <div className="space-y-4">
            <div>
              <label className="block mb-1">Bot Name</label>
              <input
                type="text"
                value={localSettings.botName}
                onChange={(e) => handleLocalChange('botName', e.target.value)}
                className="w-full border rounded px-2 py-1"
              />
            </div>
            <div>
              <label className="block mb-1">Context Data (words)</label>
              <select
                value={localSettings.contextLength}
                onChange={(e) => handleLocalChange('contextLength', e.target.value)}
                className="w-full border border-gray-300 bg-white rounded-md shadow-sm px-2 py-1 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 hover:border-gray-400 transition duration-150 ease-in-out"
              >
                <option value="500">500 words</option>
                <option disabled={true} value="1500">1500 words (plan)</option>
                <option disabled={true} value="3000">3000 words (plan)</option>
              </select>
            </div>
            <div>
              <label className="block mb-1">Context Data</label>
               
              <WordLimitTextarea
               wordLimitProp={settings.contextLength}
               handleLocalChange={handleLocalChange}
               settings={settings}/>
            </div>
            <div>
              <label className="block mb-1">Output Length (words)</label>
              <select
                value={localSettings.outputLength}
                onChange={(e) => handleLocalChange('outputLength', e.target.value)}
                className="w-full border border-gray-300 bg-white rounded-md shadow-sm px-2 py-1 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 hover:border-gray-400 transition duration-150 ease-in-out"
                >
                <option 
                className="w-full border border-gray-300 bg-white rounded-md shadow-sm px-2 py-1 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 hover:border-gray-400 transition duration-150 ease-in-out"
                value="50">50 words </option>
                <option 
                className="w-full border border-gray-300 bg-white rounded-md shadow-sm px-2 py-1 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 hover:border-gray-400 transition duration-150 ease-in-out"
                disabled={true} value="100">100 words (plan)</option>
                <option 
                disabled={true} value="150">150 words (plan)</option>
                </select>

            </div>
            <div>
              <label className="block mb-1">Conversation ID</label>
              <input
                type="text"
                placeholder="Optional"
                value={hasMemory?settings.conversationId:localSettings.conversationId}
                onChange={(e) => handleLocalChange('conversationId', e.target.value)}
                className="w-full border rounded px-2 py-1"
              />
            </div>
            <div>
              <label className="block mb-1">API Key (plan)</label>
              <input
                type="password"
                placeholder="Optional"
                value={localSettings.apiKey}
                onChange={(e) => handleLocalChange('apiKey', e.target.value)}
                className="w-full border rounded px-2 py-1"
              />
            </div>
          </div>
        </div>
      </div>
    );
  };