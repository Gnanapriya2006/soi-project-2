import os
from dotenv import load_dotenv
import google.generativeai as genai

def test_key():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ GEMINI_API_KEY not found in .env")
        return

    print(f"Key found: {api_key[:4]}...{api_key[-4:]}")
    
    genai.configure(api_key=api_key)
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Hello")
        print(f"✅ Success! Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_key()
