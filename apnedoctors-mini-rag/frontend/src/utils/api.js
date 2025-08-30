// src/utils/api.js
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

export const analyzeSymptoms = async (symptoms) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/v1/symptoms/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        symptoms,
        patient_age: null,  // Optional: Could be added as user input
        patient_gender: null,  // Optional: Could be added as user input
        medical_history: null,  // Optional: Could be added as user input
      }),
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export const getDisclaimer = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/v1/disclaimer`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};
