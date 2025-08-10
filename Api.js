
// Simulated API service 

import axios from 'axios';

const API_KEY = "sk-uOUPzge98Gq7A2U5FcB6sQ";
const LITELLM_BASE_URL = "http://91.108.112.45:4000";

const BACKEND_BASE_URL = "http://127.0.0.1:8000";

export const fetchcases = async () => {
  const response = await axios.get(`${BACKEND_BASE_URL}/api/cases`);
  return response.data;
};


export const fetchAISummary = async (caseData) => {
  const response = await axios.post(
    `${LITELLM_BASE_URL}/chat/completions`,
    {
      model: "gpt-4-turbo",
      messages: [
        {
          role: "user",
          content: `Summarize this surgical case:
          ID: ${caseData.id},
          Patient ID: ${caseData.patientId},
          Diagnosis: ${caseData.diagnosis},
          Procedure: ${caseData.procedure},
          Complications: ${caseData.complications || "None"}`
        }
      ]
    },
    {
      headers: {
        "x-litellm-api-key": API_KEY,
        "Content-Type": "application/json"
      }
    }
  );

  return response.data.choices[0].message.content;
};


