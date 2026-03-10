import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Load the Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

print(f"🔑 checking key ending in: ...{str(api_key)[-5:]}")
genai.configure(api_key=api_key)

print("\n📡 Asking Google: 'What models can I use?'...")

try:
    # 2. List all available models
    count = 0
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"   ✅ AVAILABLE: {m.name}")
            count += 1
    
    if count == 0:
        print("\n❌ NO MODELS FOUND. Your API Key is valid, but has no access to Generative AI.")
        print("   -> Go to https://aistudio.google.com/app/apikey and ensure 'Generative Language API' is enabled.")
    else:
        print(f"\n✨ Success! You have access to {count} models.")

except Exception as e:
    print(f"\n❌ FATAL ERROR: {e}")
    print("   -> This usually means the API Key is invalid or copied with spaces.")
