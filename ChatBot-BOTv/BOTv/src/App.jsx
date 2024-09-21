import ChatbotInterface from './components/ChatbotInterface';
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './components/LandingPage';

function App() {
  return (
    <Router>
      <React.StrictMode>
        <Routes>
          <Route path="/chat/:chatId" element={<ChatbotInterface hasMemory={true} />} />
          <Route path="/chat" element={<ChatbotInterface hasMemory={false} />} />
          <Route path="/" element={<LandingPage  />} />

        </Routes>
      </React.StrictMode>
    </Router>
  );
}

export default App;
