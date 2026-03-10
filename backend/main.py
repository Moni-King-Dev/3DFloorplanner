from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from gemini_scan import scan_floorplan
import shutil
import os
import uuid
import uvicorn

app = FastAPI()

# Allow connections from anywhere (fixes Fetch errors)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure upload directory exists
upload_dir = os.path.join(os.getcwd(), "uploads")
os.makedirs(upload_dir, exist_ok=True)

@app.get("/")
def home():
    return {"status": "Online", "message": "Backend is running!"}

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    try:
        # 1. Save file
        file_extension = file.filename.split(".")[-1]
        unique_filename = os.path.join(upload_dir, f"{uuid.uuid4()}.{file_extension}")
        
        print(f"📥 Receiving file: {unique_filename}")
        
        with open(unique_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # 2. Send to Gemini
        print("🚀 Sending to Gemini...")
        blueprint_data = scan_floorplan(unique_filename)
        
        if "error" in blueprint_data:
             raise HTTPException(status_code=500, detail=blueprint_data["error"])

        print("✅ Analysis Complete!")
        return blueprint_data

    except Exception as e:
        print(f"❌ Critical Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Force run on 127.0.0.1 port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)