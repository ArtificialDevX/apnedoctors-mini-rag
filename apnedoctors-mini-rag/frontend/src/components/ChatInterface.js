// src/components/ChatInterface.js
import React, { useState, useRef, useEffect } from 'react';
import SymptomInput from './SymptomInput';
import Message from './Message';
import LoadingDots from './LoadingDots';
import { analyzeSymptoms } from '../utils/api';

const ChatInterface = () => {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (symptomText) => {
    if (!symptomText.trim()) return;

    // Add user message
    const userMessage = {
      type: 'user',
      content: symptomText,
    };
    setMessages(prev => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await analyzeSymptoms(symptomText);
      
      // Format bot response
      const botMessage = {
        type: 'bot',
        content: response,
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error:', error);
      const errorMessage = {
        type: 'error',
        content: 'Sorry, there was an error processing your request. Please try again.',
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-[calc(100vh-12rem)]">
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg, idx) => (
          <Message key={idx} {...msg} />
        ))}
        {loading && <LoadingDots />}
        <div ref={messagesEndRef} />
      </div>
      <div className="p-4 border-t">
        <SymptomInput onSubmit={handleSubmit} disabled={loading} />
      </div>
    </div>
  );
};

export default ChatInterface;
