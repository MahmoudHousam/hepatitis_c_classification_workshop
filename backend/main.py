from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random

# Import database models and utilities
from database import engine, SessionLocal, get_db
from models import Base, PredictionRecord
from schemas import PredictionRequest, PredictionResponse, ModelInfo
from config import settings

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hepatitis C Classification API",
    description="API for predicting hepatitis C based on patient data",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return {"message": "Hepatitis C Classification API"}

@app.get("/model-info", response_model=ModelInfo)
async def get_model_info():
    """Get information about the ML model"""
    return ModelInfo(
        name=settings.MODEL_NAME,
        accuracy=settings.MODEL_ACCURACY,
        date_trained=settings.MODEL_DATE_TRAINED,
        version=settings.MODEL_VERSION,
        description="Machine learning model for hepatitis C classification based on patient biomarkers and clinical data"
    )

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest, db: SessionLocal = Depends(get_db)):
    """Make a prediction based on patient data"""
    try:
        # For now, return a mock prediction
        # In the future, this will use the actual ML model
        prediction_result = "Positive" if random.random() > 0.5 else "Negative"
        confidence = round(random.uniform(0.6, 0.95), 3)
        
        # Create prediction record
        prediction_record = PredictionRecord(
            age=request.age,
            sex=request.sex,
            alanine_aminotransferase=request.alanine_aminotransferase,
            aspartate_aminotransferase=request.aspartate_aminotransferase,
            gamma_glutamyl_transferase=request.gamma_glutamyl_transferase,
            alkaline_phosphatase=request.alkaline_phosphatase,
            total_bilirubin=request.total_bilirubin,
            direct_bilirubin=request.direct_bilirubin,
            total_proteins=request.total_proteins,
            albumin=request.albumin,
            albumin_globulin_ratio=request.albumin_globulin_ratio,
            prediction=prediction_result,
            confidence=confidence,
            timestamp=datetime.utcnow()
        )
        
        # Save to database
        db.add(prediction_record)
        db.commit()
        db.refresh(prediction_record)
        
        return PredictionResponse(
            prediction=prediction_result,
            confidence=confidence,
            record_id=prediction_record.id,
            timestamp=prediction_record.timestamp
        )
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.get("/predictions")
async def get_predictions(db: SessionLocal = Depends(get_db), limit: int = 100):
    """Get recent predictions from the database"""
    predictions = db.query(PredictionRecord).order_by(PredictionRecord.timestamp.desc()).limit(limit).all()
    return predictions

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)
