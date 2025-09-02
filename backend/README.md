# Hepatitis C Classification Backend

This is the backend API for the Hepatitis C Classification Workshop project, built with FastAPI and PostgreSQL.

## Features

- **Prediction Endpoint**: `/predict` - Accepts patient data and returns hepatitis C predictions
- **Model Info**: `/model-info` - Returns metadata about the ML model
- **Database Storage**: Stores all predictions and patient data in PostgreSQL
- **CORS Support**: Configured for frontend integration
- **Input Validation**: Comprehensive data validation using Pydantic schemas

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the backend directory with your database credentials:

```bash
# Database Configuration (Update with your Render PostgreSQL credentials)
DATABASE_URL=postgresql://username:password@host.render.com:5432/database_name

# Model Configuration
MODEL_NAME=Hepatitis C Classification Model
MODEL_ACCURACY=0.85
MODEL_DATE_TRAINED=2024-01-15
MODEL_VERSION=1.0.0

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True
```

### 3. Run the Application

```bash
# Option 1: Using the startup script
python start.py

# Option 2: Using uvicorn directly
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints

### GET `/`

- **Description**: Root endpoint
- **Response**: Welcome message

### GET `/model-info`

- **Description**: Get information about the ML model
- **Response**: Model metadata (name, accuracy, date trained, version)

### POST `/predict`

- **Description**: Make a prediction based on patient data
- **Request Body**: Patient demographics and laboratory values
- **Response**: Prediction result, confidence score, and record ID

### GET `/predictions`

- **Description**: Get recent predictions from the database
- **Query Parameters**: `limit` (default: 100)
- **Response**: List of prediction records

### GET `/health`

- **Description**: Health check endpoint
- **Response**: API status and timestamp

## Database Schema

The `prediction_records` table stores:

- Patient demographics (age, sex)
- Laboratory values (ALT, AST, GGT, ALP, bilirubin, proteins, albumin)
- Prediction results (prediction, confidence)
- Metadata (timestamp)

## Development

### Current Status

- ✅ FastAPI application structure
- ✅ Database models and schemas
- ✅ Mock prediction endpoint
- ✅ PostgreSQL integration
- ✅ CORS configuration
- ✅ Input validation

### Next Steps

- [ ] Integrate actual ML model
- [ ] Add authentication
- [ ] Implement rate limiting
- [ ] Add logging and monitoring
- [ ] Deploy to production

## Testing

Test the API endpoints using curl or any API client:

```bash
# Test model info
curl http://localhost:8000/model-info

# Test prediction (replace with actual data)
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 45,
    "sex": "Male",
    "alanine_aminotransferase": 25.5,
    "aspartate_aminotransferase": 28.0,
    "gamma_glutamyl_transferase": 35.2,
    "alkaline_phosphatase": 85.0,
    "total_bilirubin": 0.8,
    "direct_bilirubin": 0.3,
    "total_proteins": 7.2,
    "albumin": 4.1,
    "albumin_globulin_ratio": 1.2
  }'
```
