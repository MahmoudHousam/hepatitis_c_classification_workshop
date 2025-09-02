// API Configuration for Hepatitis C Classification
const API_URL = import.meta.env.VITE_API_URL;
export const API_CONFIG = {
  BASE_URL: API_URL,
  ENDPOINTS: {
    PREDICT: "/predict",
  },
};

// Helper function to get full API URL
export const getApiUrl = (endpoint: string): string => {
  return `${API_CONFIG.BASE_URL}${endpoint}`;
};
