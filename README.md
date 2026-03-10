# 🏠 3DFloorplanner

**3DFloorplanner** is an AI-assisted floor plan analyzer that converts 2D floor plan images into structured digital blueprints.

In this first phase, users upload a **floor plan image**, and the backend (powered by **FastAPI** and **Google Gemini API**) analyzes it to generate a structured **JSON blueprint** containing walls and rooms.

This blueprint can later be consumed by a **Three.js frontend** to render an interactive **3D environment** where users can explore the generated space.

---

# 🚀 Features

### 📤 Floor Plan Upload
A lightweight **HTML frontend** allows users to upload a floor plan image to the backend for analysis.

### 🤖 AI-Powered Analysis
The **FastAPI backend**:

- Receives the uploaded floor plan image
- Sends the image to the **Gemini Vision API**
- Extracts spatial information
- Returns a clean **JSON blueprint** containing walls and rooms

### 🧱 Structured Blueprint Output
The output is a structured **JSON format** designed for easy integration with **3D rendering engines** such as **Three.js**.

### 🔌 Pluggable 3D Rendering
The blueprint schema is designed to be consumed by a **Three.js client** to generate a navigable **3D floor plan**.

---

# 📁 Project Structure

```
3DFloorplanner
│
├── frontend
│   └── index.html        # Simple upload interface
│
├── backend
│   ├── main.py           # FastAPI application (API endpoints)
│   ├── gemini_scan.py    # Gemini API integration and response parsing
│   ├── check_models.py   # Utility to list available Gemini models
│   └── run_scan.py       # CLI helper to scan a floor plan image
│
└── requirements.txt      # Backend dependencies
```

---

# ⚙️ Prerequisites

Make sure you have the following installed:

- 🐍 **Python 3.10+**
- 🔑 **Google Gemini API Key**
- Access to the **Generative Language API**

---

# 🛠️ Setup

### 1️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Windows PowerShell:

```bash
copy .env.example .env
```

Edit the `.env` file and add your API key:

```env
GOOGLE_API_KEY=your_real_key_here
```

⚠️ **Important:**  
`.env` is ignored by Git and should **never be committed**.

---

# ▶️ Running the Backend

Navigate to the **backend directory** and start the server:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The backend will:

- Automatically create an **uploads/** directory
- Start a local API server

Available endpoints:

| Endpoint | Method | Description |
|--------|--------|--------|
| `/` | GET | Health check |
| `/analyze` | POST | Upload floor plan image and receive JSON blueprint |

---

# 🌐 Running the Frontend

Open the frontend file in your browser:

```
frontend/index.html
```

The frontend will:

1. Check backend status at  
   `http://127.0.0.1:8000/`

2. Allow you to **upload a floor plan image**

3. Send a request to  
   `POST http://127.0.0.1:8000/analyze`

4. Display the **generated JSON blueprint**

---

# 🧩 Example Blueprint Output

The backend returns a structured JSON blueprint like this:

```json
{
  "walls": [
    {
      "start": { "x": 10, "y": 10 },
      "end": { "x": 10, "y": 50 },
      "thickness": 2
    }
  ],
  "rooms": [
    {
      "name": "Kitchen",
      "center": { "x": 20, "y": 20 }
    }
  ]
}
```

A **Three.js frontend** can use this data to:

- Generate **3D wall meshes**
- Place **room labels**
- Enable **interactive navigation**

---

# 🔮 Future Improvements

Planned features for upcoming versions:

- 🧠 Better AI extraction for complex floor plans
- 🧱 Automatic wall segmentation
- 🪑 Furniture detection and placement
- 🌍 Full **Three.js 3D viewer**
- 🏢 Multi-floor building support

---

# 📜 License

This project is currently **unlicensed**.  
You can add a license such as **MIT** or **Apache 2.0** in future versions.
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

