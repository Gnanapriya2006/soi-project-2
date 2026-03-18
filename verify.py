import requests
import io

def test_upload():
    url = 'http://127.0.0.1:5001/api/scan'
    files = {'file': ('test.pdf', io.BytesIO(b'%PDF-1.4 test document'), 'application/pdf')}
    
    try:
        response = requests.post(url, files=files)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Response JSON:", response.json())
        else:
            print("Error:", response.text)
    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == '__main__':
    test_upload()
