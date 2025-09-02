from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PredictionRequest(BaseModel):
    """Schema for prediction request"""
    age: int = Field(..., ge=0, le=120, description="Patient age in years")
    sex: str = Field(..., pattern="^(Male|Female)$", description="Patient sex (Male or Female)")
    
    # Laboratory values with reasonable ranges
    alanine_aminotransferase: float = Field(..., ge=0, le=1000, description="ALT level in U/L")
    aspartate_aminotransferase: float = Field(..., ge=0, le=1000, description="AST level in U/L")
    gamma_glutamyl_transferase: float = Field(..., ge=0, le=1000, description="GGT level in U/L")
    alkaline_phosphatase: float = Field(..., ge=0, le=1000, description="ALP level in U/L")
    total_bilirubin: float = Field(..., ge=0, le=50, description="Total bilirubin in mg/dL")
    direct_bilirubin: float = Field(..., ge=0, le=20, description="Direct bilirubin in mg/dL")
    total_proteins: float = Field(..., ge=0, le=20, description="Total proteins in g/dL")
    albumin: float = Field(..., ge=0, le=10, description="Albumin in g/dL")
    albumin_globulin_ratio: float = Field(..., ge=0, le=5, description="Albumin/Globulin ratio")

class PredictionResponse(BaseModel):
    """Schema for prediction response"""
    prediction: str = Field(..., description="Prediction result (Positive or Negative)")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score (0-1)")
    record_id: int = Field(..., description="Database record ID")
    timestamp: datetime = Field(..., description="Timestamp of prediction")

class ModelInfo(BaseModel):
    """Schema for model information"""
    name: str = Field(..., description="Model name")
    accuracy: float = Field(..., ge=0, le=1, description="Model accuracy score")
    date_trained: str = Field(..., description="Date when model was trained")
    version: str = Field(..., description="Model version")
    description: str = Field(..., description="Model description")

class PredictionRecordResponse(BaseModel):
    """Schema for prediction record response"""
    id: int
    age: int
    sex: str
    alanine_aminotransferase: float
    aspartate_aminotransferase: float
    gamma_glutamyl_transferase: float
    alkaline_phosphatase: float
    total_bilirubin: float
    direct_bilirubin: float
    total_proteins: float
    albumin: float
    albumin_globulin_ratio: float
    prediction: str
    confidence: float
    timestamp: datetime
    
    class Config:
        from_attributes = True
