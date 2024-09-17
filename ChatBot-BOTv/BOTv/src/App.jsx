import { useState } from 'react'
 
 
import ChatbotInterface from './components/ChatbotInterface'
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <React.StrictMode>
        <ChatbotInterface />
    </React.StrictMode>,
    </>
  )
}

export default App
