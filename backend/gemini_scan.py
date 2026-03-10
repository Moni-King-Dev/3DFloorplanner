import requests
import json
import os
import base64
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def _detect_mime_type(image_path: str) -> str:
    """
    Try to detect the image MIME type using Pillow.
    Falls back to 'image/jpeg' if detection fails.
    """
    try:
        with Image.open(image_path) as img:
            fmt = (img.format or "").upper()
    except Exception:
        return "image/jpeg"

    mapping = {
        "JPEG": "image/jpeg",
        "JPG": "image/jpeg",
        "PNG": "image/png",
        "WEBP": "image/webp",
        "GIF": "image/gif",
        "BMP": "image/bmp",
        "TIFF": "image/tiff",
        "HEIC": "image/heic",
    }
    return mapping.get(fmt, "image/jpeg")


def scan_floorplan(image_path):
    print(f"👀 AI is looking at: {image_path}")

    # 1. Encode image
    try:
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        return {"error": f"Failed to read file: {e}"}

    # 2. Detect MIME type so we send correct metadata to Gemini
    mime_type = _detect_mime_type(image_path)

    # 3. Use 'gemini-2.0-flash-exp' which your account confirmed it has
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={api_key}"

    # 4. Payload
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{
            "parts": [
                {"text": """
                Analyze this floor plan image strictly. 
                Imagine a coordinate system where Top-Left is (0,0) and Bottom-Right is (100,100).
                
                Identify all WALLS. Return start and end coordinates.
                Identify ROOMS. Return the center coordinate and the room name.
                
                Output MUST be valid JSON only. No markdown.
                Structure:
                {
                    "walls": [
                        {"start": {"x": 10, "y": 10}, "end": {"x": 10, "y": 50}, "thickness": 2}
                    ],
                    "rooms": [
                        {"name": "Kitchen", "center": {"x": 20, "y": 20}}
                    ]
                }
                """},
                {
                    "inline_data": {
                        "mime_type": mime_type,
                        "data": base64_image,
                    }
                }
            ]
        }]
    }

    try:
        print("🚀 Sending to Gemini 2.0 Flash...")
        response = requests.post(url, headers=headers, json=data)
        
        # Error Handling
        if response.status_code != 200:
            print(f"❌ Google Error: {response.text}")
            return {"error": f"Google Error {response.status_code}", "details": response.text}

        # Parse Success
        result = response.json()
        text_content = result['candidates'][0]['content']['parts'][0]['text']
        clean_text = text_content.replace("```json", "").replace("```", "").strip()
        
        return json.loads(clean_text)

    except Exception as e:
        print(f"❌ Python Error: {e}")
        return {"error": str(e)}