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
