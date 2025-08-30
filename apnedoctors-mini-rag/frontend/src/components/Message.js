// src/components/Message.js
import React from 'react';

const Message = ({ type, content }) => {
  if (type === 'user') {
    return (
      <div className="flex justify-end mb-4">
        <div className="bg-blue-600 text-white rounded-lg px-4 py-2 max-w-[80%]">
          <p>{content}</p>
        </div>
      </div>
    );
  }

  if (type === 'error') {
    return (
      <div className="flex justify-start mb-4">
        <div className="bg-red-100 text-red-700 rounded-lg px-4 py-2 max-w-[80%]">
          <p>{content}</p>
        </div>
      </div>
    );
  }

  // Bot message with medical response
  const {
    possible_conditions,
    urgency,
    suggestions,
    clarifying_questions,
    disclaimer
  } = content;

  return (
    <div className="flex justify-start mb-4">
      <div className="bg-white border border-gray-200 rounded-lg px-4 py-2 max-w-[80%] shadow-sm">
        {/* Conditions */}
        <div className="mb-4">
          <h3 className="font-semibold text-gray-900 mb-2">Possible Conditions:</h3>
          <ul className="space-y-2">
            {possible_conditions.map((condition, idx) => (
              <li key={idx} className="flex items-start">
                <div className="flex-1">
                  <p className="font-medium text-gray-800">{condition.name}</p>
                  <p className="text-sm text-gray-600">{condition.description}</p>
                  <div className="mt-1 flex items-center">
                    <div className="text-xs text-gray-500">
                      Confidence: {Math.round(condition.probability * 100)}%
                    </div>
                  </div>
                </div>
              </li>
            ))}
          </ul>
        </div>

        {/* Urgency Level */}
        <div className="mb-4">
          <h3 className="font-semibold text-gray-900 mb-2">Urgency Level:</h3>
          <div className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium
            ${urgency === 'HIGH' ? 'bg-red-100 text-red-800' :
              urgency === 'MODERATE' ? 'bg-yellow-100 text-yellow-800' :
                'bg-green-100 text-green-800'}`}>
            {urgency}
          </div>
        </div>

        {/* Suggestions */}
        <div className="mb-4">
          <h3 className="font-semibold text-gray-900 mb-2">Recommended Steps:</h3>
          <ul className="list-disc pl-5 space-y-1">
            {suggestions.map((suggestion, idx) => (
              <li key={idx} className="text-gray-700">{suggestion}</li>
            ))}
          </ul>
        </div>

        {/* Clarifying Questions */}
        {clarifying_questions && clarifying_questions.length > 0 && (
          <div className="mb-4">
            <h3 className="font-semibold text-gray-900 mb-2">Follow-up Questions:</h3>
            <ul className="list-disc pl-5 space-y-1">
              {clarifying_questions.map((question, idx) => (
                <li key={idx} className="text-gray-700">{question}</li>
              ))}
            </ul>
          </div>
        )}

        {/* Disclaimer */}
        <div className="mt-4 text-xs text-gray-500 border-t pt-2">
          <p>{disclaimer}</p>
        </div>
      </div>
    </div>
  );
};

export default Message;
