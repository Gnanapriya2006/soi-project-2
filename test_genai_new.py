import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def test_chat():
    try:
        client = genai.Client(api_key=api_key)
        model_id = 'gemini-2.5-flash'
        print(f"DEBUG: Using model ID: {model_id}")
        response = client.models.generate_content(
            model=model_id,
            contents='Hello, can you hear me? Respond with "Yes, I can hear you."'
        )
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_chat()
