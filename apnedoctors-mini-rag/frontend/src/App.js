import React, { useState } from 'react';

function App() {
  const [symptoms, setSymptoms] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeSymptoms = async () => {
    if (!symptoms.trim()) return;
    
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          symptoms: symptoms,
        }),
      });
      
      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          {/* Header */}
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-blue-600 mb-4">
              🏥 ApneDoctors Mini-RAG
            </h1>
            <p className="text-xl text-gray-700">
              AI-Powered Medical Symptom Checker
            </p>
          </div>

          {/* Input Section */}
          <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Describe your symptoms:
            </label>
            <textarea
              value={symptoms}
              onChange={(e) => setSymptoms(e.target.value)}
              placeholder="e.g., I have been experiencing fever, headache, and body aches for 2 days"
              className="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              rows={4}
            />
            <button
              onClick={analyzeSymptoms}
              disabled={loading || !symptoms.trim()}
              className="mt-4 w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:bg-gray-300 transition-colors"
            >
              {loading ? 'Analyzing...' : 'Analyze Symptoms'}
            </button>
          </div>

          {/* Response Section */}
          {response && (
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-lg font-semibold mb-4">Analysis Results:</h3>
              
              {/* Urgency Level */}
              <div className={`p-4 rounded-lg mb-4 ${
                response.urgency === 'high' ? 'bg-red-50 text-red-800' :
                response.urgency === 'moderate' ? 'bg-orange-50 text-orange-800' :
                'bg-green-50 text-green-800'
              }`}>
                <div className="font-semibold">
                  {response.urgency.toUpperCase()} Urgency
                </div>
              </div>

              {/* Possible Conditions */}
              <div className="mb-4">
                <h4 className="font-semibold mb-2">Possible Conditions:</h4>
                {response.possible_conditions.map((condition, idx) => (
                  <div key={idx} className="border-l-4 border-blue-200 pl-4 py-2">
                    <div className="flex justify-between">
                      <h5 className="font-medium">{condition.name}</h5>
                      <span className="text-sm text-gray-500">
                        {Math.round(condition.probability * 100)}% match
                      </span>
                    </div>
                    <p className="text-gray-600 text-sm">{condition.description}</p>
                  </div>
                ))}
              </div>

              {/* Suggestions */}
              <div className="mb-4">
                <h4 className="font-semibold mb-2">Recommendations:</h4>
                <ul className="list-disc list-inside space-y-1">
                  {response.suggestions.map((suggestion, idx) => (
                    <li key={idx} className="text-gray-700">{suggestion}</li>
                  ))}
                </ul>
              </div>

              {/* Disclaimer */}
              <div className="bg-yellow-50 border border-yellow-200 rounded-md p-4 mt-4">
                <p className="text-xs text-gray-600">
                  <strong>Medical Disclaimer:</strong> This information is for educational purposes only and should not replace professional medical advice. Always consult with a healthcare provider for proper diagnosis and treatment.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
