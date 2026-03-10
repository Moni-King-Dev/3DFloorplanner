import google.generativeai as genai
import PIL.Image
import os
import time

# --- 1. SETUP: We ask for the key directly to avoid .env errors ---
api_key = input("🔑 Paste your Google API Key here and press Enter: ").strip()
genai.configure(api_key=api_key)

# --- 2. CONFIGURATION: List of every model we might try ---
# We prioritize the "Flash" models because they are usually free and fast.
MODEL_LIST = [
    "gemini-1.5-flash",
    "gemini-1.5-flash-latest",
    "gemini-1.5-pro",
    "gemini-2.0-flash-exp",
    "models/gemini-1.5-flash",
    "models/gemini-1.5-pro"
]

def scan_image():
    # Ask for the image file
    img_path = input("📂 Enter the image filename (e.g., floorplan.png): ").strip()
    
    if not os.path.exists(img_path):
        print(f"❌ Error: File '{img_path}' not found!")
        return

    print(f"👀 Loading {img_path}...")
    img = PIL.Image.open(img_path)

    prompt = """
    Analyze this floor plan image strictly. 
    Imagine a coordinate system where Top-Left is (0,0) and Bottom-Right is (100,100).
    
    1. Identify all WALLS. Return start and end coordinates.
    2. Identify ROOMS. Return the center coordinate and the room name.
    
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
    """

    # --- 3. THE LOOP: Try every model until one works ---
    success = False
    for model_name in MODEL_LIST:
        print(f"🔄 Attempting to connect to: {model_name}...")
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content([prompt, img])
            
            # If we get here without error, it worked!
            print(f"✅ SUCCESS! Connected to {model_name}")
            
            # Clean the text
            clean_text = response.text.replace("```json", "").replace("```", "").strip()
            
            # Print the result
            print("\n" + "="*40)
            print("       YOUR JSON BLUEPRINT")
            print("="*40)
            print(clean_text)
            print("="*40)
            
            # Save it to a file
            with open("blueprint.json", "w") as f:
                f.write(clean_text)
            print("💾 Saved data to 'blueprint.json'")
            
            success = True
            break # Stop the loop, we are done
            
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg:
                print(f"⚠️  Quota Exceeded for {model_name}. (You are clicking too fast!)")
                time.sleep(2) # Wait a bit before trying next
            elif "404" in error_msg:
                print(f"❌ {model_name} not found. Trying next...")
            else:
                print(f"❌ Error with {model_name}: {e}")

    if not success:
        print("\n❌ ALL MODELS FAILED. Please check your API Key or Internet Connection.")

# --- RUN IT ---
if __name__ == "__main__":
    scan_image()