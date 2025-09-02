#!/usr/bin/env python3
"""
Simple test script for the Hepatitis C Classification API
"""
import requests
import json
from datetime import datetime

# API base URL
BASE_URL = "http://localhost:8000"

def test_root():
    """Test the root endpoint"""
    print("Testing root endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

def test_model_info():
    """Test the model info endpoint"""
    print("Testing model info endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/model-info")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Model: {data['name']}")
            print(f"Accuracy: {data['accuracy']}")
            print(f"Version: {data['version']}")
        else:
            print(f"Response: {response.text}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

def test_prediction():
    """Test the prediction endpoint"""
    print("Testing prediction endpoint...")
    
    # Sample patient data
    patient_data = {
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
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json=patient_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Prediction: {data['prediction']}")
            print(f"Confidence: {data['confidence']}")
            print(f"Record ID: {data['record_id']}")
        else:
            print(f"Response: {response.text}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

def test_predictions():
    """Test the predictions endpoint"""
    print("Testing predictions endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/predictions?limit=5")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data)} predictions")
            if data:
                latest = data[0]
                print(f"Latest prediction: {latest['prediction']} (confidence: {latest['confidence']})")
        else:
            print(f"Response: {response.text}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

def test_health():
    """Test the health endpoint"""
    print("Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Status: {data['status']}")
            print(f"Timestamp: {data['timestamp']}")
        else:
            print(f"Response: {response.text}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

def main():
    """Run all tests"""
    print("=" * 50)
    print("Hepatitis C Classification API Tests")
    print("=" * 50)
    print()
    
    test_root()
    test_model_info()
    test_prediction()
    test_predictions()
    test_health()
    
    print("=" * 50)
    print("Tests completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
