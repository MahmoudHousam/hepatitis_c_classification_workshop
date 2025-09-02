#!/usr/bin/env python3
"""
Startup script for the Hepatitis C Classification API
"""
import uvicorn
from config import settings

if __name__ == "__main__":
    print(f"Starting Hepatitis C Classification API on {settings.API_HOST}:{settings.API_PORT}")
    print(f"Debug mode: {settings.DEBUG}")
    print(f"Database: {settings.DATABASE_URL.split('@')[1] if '@' in settings.DATABASE_URL else 'Not configured'}")
    
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level="info" if settings.DEBUG else "warning"
    )
