from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class PredictionRecord(Base):
    __tablename__ = "prediction_records"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Patient demographics
    age = Column(Integer, nullable=False)
    sex = Column(String(10), nullable=False)
    
    # Laboratory values
    alanine_aminotransferase = Column(Float, nullable=False)
    aspartate_aminotransferase = Column(Float, nullable=False)
    gamma_glutamyl_transferase = Column(Float, nullable=False)
    alkaline_phosphatase = Column(Float, nullable=False)
    total_bilirubin = Column(Float, nullable=False)
    direct_bilirubin = Column(Float, nullable=False)
    total_proteins = Column(Float, nullable=False)
    albumin = Column(Float, nullable=False)
    albumin_globulin_ratio = Column(Float, nullable=False)
    
    # Prediction results
    prediction = Column(String(20), nullable=False)  # "Positive" or "Negative"
    confidence = Column(Float, nullable=False)
    
    # Metadata
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<PredictionRecord(id={self.id}, prediction='{self.prediction}', confidence={self.confidence})>"
