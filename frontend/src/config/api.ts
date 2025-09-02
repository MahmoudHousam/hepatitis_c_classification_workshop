// API Configuration for Hepatitis C Classification
export const API_CONFIG = {
  BASE_URL: "http://localhost:8000",
  ENDPOINTS: {
    PREDICT: "/predict",
  },
};

// Helper function to get full API URL
export const getApiUrl = (endpoint: string): string => {
  return `${API_CONFIG.BASE_URL}${endpoint}`;
};
