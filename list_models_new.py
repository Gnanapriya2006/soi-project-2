import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def list_models():
    try:
        client = genai.Client(api_key=api_key)
        print("Available models:")
        with open("models_full.txt", "w") as f:
            for model in client.models.list():
                f.write(f"{model.name}\n")
        print("Model list saved to models_full.txt")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_models()
