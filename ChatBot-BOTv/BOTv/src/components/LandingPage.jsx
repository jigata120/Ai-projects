import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { postData } from '../Api';


const LandingPage = () => {
  const [email, setEmail] = useState('');
  const navigate = useNavigate();

  const handleQuickChat = () => { 
    navigate('/chat');

  };

  const handleRequestId = async(e) => {
    e.preventDefault();
 
    const data = {email:email}
    alert(`Conversation ID senting to ${email}.Loading...`);
    const response = await postData("http://127.0.0.1:8000/conversationIdRequest/", data);
  
    if (response){
      alert(`Conversation ID sent to ${email} successfully.`);
    }else{
      alert(`Conversation ID sent to ${email} is not successful`);
      
    }
    
     

  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-100 to-white p-8">
      <div className="max-w-6xl mx-auto">
        <header className="text-center mb-16">
          <h1 className="text-4xl font-bold text-blue-600 mb-4">Custom AI Assistant</h1>
          <p className="text-xl text-gray-600">Transform your data into an intelligent chatbot</p>
        </header>

        <div className="flex flex-col md:flex-row gap-12 items-center">
          <div className="flex-1">
            <h2 className="text-3xl font-semibold mb-6">Create Your Own AI Assistant</h2>
            <ul className="space-y-4">
              <li className="flex items-start">
                <span className="mr-4 text-blue-500 font-bold text-xl">➤</span>
                <span>Upload your business data or any relevant information</span>
              </li>
              <li className="flex items-start">
                <span className="mr-4 text-blue-500 font-bold text-xl">➤</span>
                <span>Our AI processes and learns from your data</span>
              </li>
              <li className="flex items-start">
                <span className="mr-4 text-blue-500 font-bold text-xl">➤</span>
                <span>Deploy your custom chatbot assistant instantly (beta)</span>
              </li>
            </ul>
          </div>
          <div className="flex flex-col bg-white rounded-3xl">
            <div className="px-6 py-8 sm:p-10 sm:pb-6">
              <div className="grid items-center justify-center w-full grid-cols-1 text-left">
                <div>
                  <h2
                    className="text-lg font-medium tracking-tighter text-gray-600 lg:text-3xl"
                  >
                    Default pack
                  </h2>
                  <p className="mt-2 text-sm text-gray-500">Controll your cost.</p>
                </div>
                <div className="mt-6">
                  <p>
                    <span className="text-5xl font-light tracking-tight text-black">
                      $0
                    </span>
                    <span className="text-base font-medium text-gray-500"> and pay as you go </span>
                  </p>
                </div>
              </div>
            </div>
            <div className="flex px-6 pb-8 sm:px-8">
              <a
                aria-describedby="tier-company"
                className="flex items-center justify-center w-full px-6 py-2.5 text-center text-white duration-200 bg-black border-2 border-black rounded-full nline-flex hover:bg-transparent hover:border-black hover:text-black focus:outline-none focus-visible:outline-black text-sm focus-visible:ring-black"
                 
              >
                Get started
              </a>
            </div>
          </div>
          {/* <div class="flex gap-4"> */}
          <div className="flex flex-col bg-white rounded-3xl">
            <div className="px-6 py-8 sm:p-10 sm:pb-6">
              <div className="grid items-center justify-center w-full grid-cols-1 text-left">
                <div>
                  <h2
                    className="text-lg font-medium tracking-tighter text-gray-600 lg:text-3xl"
                  >
                    Initial Starter
                  </h2>
                  <p className="mt-2 text-sm text-gray-500">For small businesses. </p>
                </div>
                <div className="mt-6">
                  <p>
                    <span className="text-5xl font-light tracking-tight text-black">
                      $5
                    </span>
                    <span className="text-base font-medium text-gray-500">/mo and pay as you go </span>
                  </p>
                </div>
              </div>
            </div>
            <div className="flex px-6 pb-8 sm:px-8">
              <a
                aria-describedby="tier-company"
                className="flex items-center justify-center w-full px-6 py-2.5 text-center text-white duration-200 bg-black border-2 border-black rounded-full nline-flex hover:bg-transparent hover:border-black hover:text-black focus:outline-none focus-visible:outline-black text-sm focus-visible:ring-black"
                 
              >
                Get started
              </a>
            </div>
          </div>
          <div className="flex flex-col bg-white rounded-3xl">
            <div className="px-6 py-8 sm:p-10 sm:pb-6">
              <div className="grid items-center justify-center w-full grid-cols-1 text-left">
                <div>
                  <h2
                    className="text-lg font-medium tracking-tighter text-gray-600 lg:text-3xl"
                  >
                    MaxPack
                  </h2>
                  <p className="mt-2 text-sm text-gray-500">Suitable to grow steadily.</p>
                </div>
                <div className="mt-6">
                  <p>
                    <span className="text-5xl font-light tracking-tight text-black">
                      $15
                    </span>
                    <span className="text-base font-medium text-gray-500">/mo and pay as you go </span>
                  </p>
                </div>
              </div>
            </div>
            <div className="flex px-6 pb-8 sm:px-8">
              <a
                aria-describedby="tier-company"
                className="flex items-center justify-center w-full px-6 py-2.5 text-center text-white duration-200 bg-black border-2 border-black rounded-full nline-flex hover:bg-transparent hover:border-black hover:text-black focus:outline-none focus-visible:outline-black text-sm focus-visible:ring-black"
                
              >
                Get started
              </a>
            </div>
          </div>
          
           


          <div className="flex-1 w-full max-w-md bg-white rounded-lg shadow-md p-6">
            <h3 className="text-2xl font-semibold mb-4">Get Started Now</h3>
            <button 
              onClick={handleQuickChat}
              className="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded mb-4 transition duration-300"
            >
              Start a Free Quick Chat
            </button>
            <form onSubmit={handleRequestId} className="space-y-4">
              <input
                type="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <button 
                type="submit"
                className="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300"
              >
                Request Conversation ID
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
