from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Hepatitis C Classification API")


# CORS configuration for development and production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # Development
        "http://localhost:5173",  # Vite dev server
        "http://localhost:3000",  # React dev server
        # "https://domain.com",  # Production domain
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=[
        "Content-Type",
        "Authorization", 
        "Accept",
        "Origin",
        "X-Requested-With",
        "Cache-Control",
        "Pragma"
    ],
    expose_headers=["Content-Length", "Content-Type"],
    max_age=600, 
)


@app.post("/predict")
async def predict(request: dict):
    try:
        if not request:
            return {
                "error": "No data received",
                "status": "error"
            }, 400
    
        # TODO: Replace this with your actual ML model
        prediction = "Positive" if random.random() > 0.5 else "Negative"
        confidence = round(random.uniform(0.6, 0.95), 3)
        
        return {
            "prediction": prediction,
            "confidence": confidence,
            "message": f"Prediction: {prediction} (Confidence: {confidence})",
            "status": "success",
            "timestamp": "2024-01-15T12:00:00Z"  # Add timestamp for tracking
        }
        
    except Exception as e:

        return {
            "error": "Prediction failed",
            "message": str(e),
            "status": "error"
        }, 500

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
