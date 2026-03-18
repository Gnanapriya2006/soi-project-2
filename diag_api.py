import os
import google.generativeai as genai
from dotenv import load_dotenv
import sys

def diag():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("FAIL: GEMINI_API_KEY not found")
        return

    print(f"DEBUG: Key found: {api_key[:8]}...")
    
    try:
        genai.configure(api_key=api_key)
        print("DEBUG: genai configured")
        
        print("DEBUG: Listing models...")
        models = genai.list_models()
        available = [m.name for m in models]
        print(f"DEBUG: Available models: {available[:5]}...")
        
        model_to_use = 'gemini-1.5-flash'
        print(f"DEBUG: Using model: {model_to_use}")
        model = genai.GenerativeModel(model_to_use)
        
        print("DEBUG: Sending request...")
        response = model.generate_content("Say 'Gemini is working'")
        
        if response:
            print(f"DEBUG: Response object received: {type(response)}")
            try:
                print(f"SUCCESS: Response text: {response.text}")
            except Exception as e:
                print(f"FAIL: Error extracting text from response: {e}")
                if hasattr(response, 'candidate'):
                    print(f"DEBUG: Candidate info: {response.candidate}")
                if hasattr(response, 'prompt_feedback'):
                    print(f"DEBUG: Prompt feedback: {response.prompt_feedback}")
        else:
            print("FAIL: No response object")
            
    except Exception as e:
        print(f"FAIL: General error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    diag()
