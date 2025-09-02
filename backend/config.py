import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    # Database settings
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://username:password@localhost:5432/hepatitis_c_db"
    )
    
    # Model settings
    MODEL_NAME: str = os.getenv("MODEL_NAME", "Hepatitis C Classification Model")
    MODEL_ACCURACY: float = float(os.getenv("MODEL_ACCURACY", "0.85"))
    MODEL_DATE_TRAINED: str = os.getenv("MODEL_DATE_TRAINED", "2024-01-15")
    MODEL_VERSION: str = os.getenv("MODEL_VERSION", "1.0.0")
    
    # API settings
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # CORS settings
    ALLOWED_ORIGINS: list = [
        "http://localhost:5173",  # Vite dev server
        "http://localhost:3000",  # React dev server
        "http://localhost:8080",  # Alternative dev server
    ]
    
    # Add production origins here when deploying
    # ALLOWED_ORIGINS.extend([
    #     "https://yourdomain.com",
    #     "https://app.yourdomain.com"
    # ])

# Create global settings instance
settings = Settings()
