import os
import json
from google import genai
from google.genai import types

def analyze_request(request_text):
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # Fallback if API Key is not set
    if not api_key:
        print("[AI Manager] Warning: GEMINI_API_KEY missing. Using fallback mock.")
        return {
            "tasks": ["Wall Hacking", "Tiling"],
            "materials": ["Tiles", "Grout"],
            "complexity": 4,
            "has_safety_hazard": True
        }

    client = genai.Client(api_key=api_key)
    prompt = f"Analyze this renovation request: '{request_text}'"

    # Enforce JSON output schema
    schema = {
        "type": "OBJECT",
        "properties": {
            "tasks": {"type": "ARRAY", "items": {"type": "STRING"}},
            "materials": {"type": "ARRAY", "items": {"type": "STRING"}},
            "complexity": {"type": "INTEGER"},
            "has_safety_hazard": {"type": "BOOLEAN"}
        },
        "required": ["tasks", "materials", "complexity", "has_safety_hazard"]
    }

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=schema
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"[AI Manager] Error calling API ({e}). Using fallback.")
        return {
            "tasks": ["General Renovation"],
            "materials": ["Standard Materials"],
            "complexity": 1,
            "has_safety_hazard": False
        }