import google.generativeai as genai
import PIL.Image
import os
import time

# --- 1. SETUP ---
print('\n--- AI ARCHITECT SCANNER ---')
api_key = input('?? Paste your Google API Key here and press Enter: ').strip()
genai.configure(api_key=api_key)

# --- 2. MODEL LIST ---
MODEL_LIST = [
    'gemini-2.0-flash-exp',
    'gemini-1.5-flash',
    'gemini-1.5-flash-latest',
    'gemini-1.5-pro',
    'models/gemini-1.5-flash'
]

def scan_image():
    # Ask for image
    img_path = input('?? Enter the image filename (e.g., image.png): ').strip()
    
    # Remove quotes if user added them
    img_path = img_path.replace('"', '').replace("'", "")

    if not os.path.exists(img_path):
        print(f'? Error: File {img_path} not found inside ai-architect folder!')
        return

    print(f'?? Loading {img_path}...')
    try:
        img = PIL.Image.open(img_path)
    except Exception as e:
        print(f'? Could not open image: {e}')
        return

    prompt = 'Analyze this floor plan. Output valid JSON with walls (start/end) and rooms.'

    # --- 3. CONNECTION LOOP ---
    for model_name in MODEL_LIST:
        print(f'?? Trying model: {model_name}...')
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content([prompt, img])
            
            clean_text = response.text.replace('`json', '').replace('`', '').strip()
            
            print('\n' + '='*40)
            print('       ? SUCCESS! JSON BELOW')
            print('='*40)
            print(clean_text)
            
            # Save to file
            with open('blueprint.json', 'w') as f:
                f.write(clean_text)
            print('\n?? Saved to blueprint.json')
            return

        except Exception as e:
            if '429' in str(e):
                print('?? Quota limit. Waiting 2 seconds...')
                time.sleep(2)
            else:
                print(f'? {model_name} failed. Trying next...')

    print('\n? ALL MODELS FAILED. Check your API Key.')

if __name__ == '__main__':
    scan_image()
