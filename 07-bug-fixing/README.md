# Project 07: Bug-Fixing (Full Stack)

This project is a modern analytics dashboard built with **Next.js (React)** and **Flask (Python)**. It contains several intentional bugs that you need to find and fix using Antigravity.

## 🛠️ Setup

### Backend (Flask)

1. Go to `backend/`.
2. Create/activate venv: `python3 -m venv venv && source venv/bin/activate`.
3. Install: `pip install -r requirements.txt`.
4. Run: `python app.py`.

### Frontend (Next.js)

1. Go to `frontend/`.
2. Install: `npm install`.
3. Run: `npm run dev`.

---

## 🎯 The Mission

There are **3 critical bugs** in this application:

1. **Server-Side Crash**: The dashboard fails to load stats when the query parameter is missing in the backend.
2. **JavaScript Magic**: The "Reset" button seems to break the calculator logic, causing numbers to join like strings instead of adding up.
3. **UI Interaction**: The "Optimize Now" button is clearly visible, but it's impossible to click!

### Sample Prompt to Start

> "I'm working on Project 07 (Bug-Fixing). The dashboard isn't loading backend stats, the Counter reset logic is broken, and the UI buttons aren't clickable. Can you analyze the codebase and help me fix these three issues?"
