import requests
import json

def test_predict_endpoint():
    print("Testing /predict endpoint...")
    print("=" * 40)
    
    # Test data matching the frontend form
    test_data = {
        "mrn": "12345",
        "gender": "Male",
        "albumin": "4.2",
        "alkalinePhosphatase": "85",
        "alanineTransaminase": "25",
        "aspartateTransaminase": "28",
        "bilirubin": "0.8",
        "cholinesterase": "8.5",
        "cholesterol": "4.2",
        "creatinine": "85",
        "gammaGlutamylTransferase": "35",
        "protein": "7.2"
    }
    
    try:
        response = requests.post(
            "http://localhost:8000/predict",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("Success!")
            print(f"Prediction: {data.get('prediction', 'N/A')}")
            print(f"Confidence: {data.get('confidence', 'N/A')}")
            print(f"Message: {data.get('message', 'N/A')}")
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Connection failed. Make sure the backend is running on http://localhost:8000")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test_predict_endpoint()
