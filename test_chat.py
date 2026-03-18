import requests
import json
import time

def test_chat():
    print("Testing /api/chat endpoint...")
    
    url = 'http://127.0.0.1:5001/api/chat'
    
    # Mock context from a successful scan
    context = {
        "isAuthentic": False,
        "confidence": 35.5,
        "details": {
            "ocr": True,
            "signature": False,  # Suspicious
            "metadata": True,
            "watermark": False,  # Missing
            "fontConsistency": False, # Inconsistent
            "pixelAnomalies": True    # Anomalies found
        }
    }
    
    payload = {
        "message": "Why is this document considered fake?",
        "context": context
    }
    
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if 'response' in data:
                print("\n✅ Chat API Test Passed!")
                print("AI Response Preview:", data['response'][:100] + "...")
                return True
            else:
                print("❌ API returned 200 but missing 'response' field.")
                print("Response:", data)
        else:
            print("❌ API Request Failed.")
            print("Error:", response.text)
            
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        print("Ensure the Flask server is running on port 5001.")

    return False

if __name__ == "__main__":
    if test_chat():
        print("\nChat system is operational.")
    else:
        print("\nChat system check failed.")
