🏠 3DFloorplanner

3DFloorplanner is an AI-assisted floor plan analyzer.

In this first phase, you upload a floor plan image, and the backend (powered by FastAPI and Google's Gemini API) converts it into a structured JSON "blueprint" of walls and rooms.

This JSON is intended to be used by a Three.js frontend to render an interactive 3D view where users can move around the generated space.

✨ Features
📤 Floor Plan Upload (Frontend)

A simple HTML frontend where users can upload a floor plan image.

🤖 AI-Powered Analysis (Backend)

A FastAPI service that:

Receives the uploaded image

Sends it to the Gemini API

Returns a clean JSON blueprint with walls and rooms

🧩 Pluggable 3D Rendering

The JSON schema is designed to be consumed by a Three.js client for full 3D navigation.

📁 Project Structure
frontend/index.html

Minimal upload UI for sending a floor plan image to the backend and viewing the JSON response.

backend/main.py

FastAPI app exposing:

GET / → Health check

POST /analyze → Accepts an image and returns the analyzed JSON blueprint

backend/gemini_scan.py

Logic for calling the Gemini API and parsing its response into the expected JSON structure.

backend/check_models.py

Utility to list which Gemini models your API key can use.

backend/run_scan.py

CLI helper to scan a single image and save the blueprint to blueprint.json.

requirements.txt

Python dependencies for the backend.

⚙️ Prerequisites

🐍 Python 3.10+ (recommended)

🔑 A Google Gemini API key with access to the Generative Language API

🛠️ Setup
1️⃣ Create and Activate a Virtual Environment
python -m venv .venv

Activate it:

Windows

.venv\Scripts\activate

macOS / Linux

source .venv/bin/activate
2️⃣ Install Backend Dependencies
pip install -r requirements.txt
3️⃣ Configure Environment Variables

Copy .env.example to .env:

Linux / macOS

cp .env.example .env

Windows PowerShell

copy .env.example .env

Then edit .env and set:

GOOGLE_API_KEY=your_real_key_here

⚠️ Important:
.env is ignored by git and should never be committed.

🚀 Running the Backend

From the backend directory, run:

uvicorn main:app --reload --host 127.0.0.1 --port 8000

The backend will:

📁 Create an uploads/ folder (if it does not exist)

🌐 Expose the following endpoints:

GET /
→ Returns a simple JSON status

POST /analyze
→ Accepts form field file with the uploaded image

🌐 Running the Frontend

Simply open:

frontend/index.html

in a browser (double-click or via a simple static server).

The frontend will:

✅ Check backend status at
http://127.0.0.1:8000/

📂 Allow you to select an image file

📤 Send a POST request to
http://127.0.0.1:8000/analyze

📄 Display the returned JSON blueprint in a <pre> block

🧱 Notes for the Future 3D Viewer

The JSON blueprint returned from POST /analyze follows this structure:

{
  "walls": [
    { "start": { "x": 10, "y": 10 }, "end": { "x": 10, "y": 50 }, "thickness": 2 }
  ],
  "rooms": [
    { "name": "Kitchen", "center": { "x": 20, "y": 20 } }
  ]
}

A Three.js frontend can use this data to:

🧱 Build wall meshes based on the walls list

🏷️ Place room labels or volumes based on the rooms list

📜 License

You can choose and add a license later (for example MIT or Apache 2.0).

For now, the project is unlicensed.```

2. **Install backend dependencies**:

```bash
pip install -r requirements.txt
```

3. **Configure environment variables**:

Copy `.env.example` to `.env` and fill in your Gemini API key:

```bash
cp .env.example .env  # On Windows PowerShell: copy .env.example .env
```

Then edit `.env` and set:

```text
GOOGLE_API_KEY=your_real_key_here
```

> **Important**: `.env` is ignored by git and should never be committed.

---

### Running the backend

From the `backend` directory:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The backend will:

- Create an `uploads/` folder (if it does not exist).
- Expose:
  - `GET /` – Simple JSON status.
  - `POST /analyze` – Accepts form field `file` with the uploaded image.

---

### Running the frontend

Simply open `frontend/index.html` in a browser (double-click or via a simple static server).  
It will:

- Check the backend status at `http://127.0.0.1:8000/`.
- Allow you to select an image file.
- Send a `POST` request to `http://127.0.0.1:8000/analyze`.
- Display the returned JSON blueprint in a `<pre>` block.

---

### Notes for the future 3D viewer

- The JSON blueprint returned from `POST /analyze` follows this structure:

```json
{
  "walls": [
    { "start": { "x": 10, "y": 10 }, "end": { "x": 10, "y": 50 }, "thickness": 2 }
  ],
  "rooms": [
    { "name": "Kitchen", "center": { "x": 20, "y": 20 } }
  ]
}
```

- A Three.js frontend can use this data to:
  - Build wall meshes based on the `walls` list.
  - Place room labels/volumes based on the `rooms` list.

---

### License

For now, the project is unlicensed.

