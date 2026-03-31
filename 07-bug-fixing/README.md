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

## 🎯 Phased Troubleshooting

To get the most out of this project, we recommend fixing the bugs one by one in the following order:

### **Phase 1: Backend Fix (KeyError)**

* **The Issue**: The dashboard fails to load stats because the backend crashes if the `type` query parameter is missing.
* **Target File**: `backend/app.py`
* ...

### **Phase 2: Logic Fix (JavaScript State)**

* **The Issue**: After clicking "Reset," the "Increment" button performs string concatenation (e.g., `01`, `011`) instead of addition.
* **Target File**: `frontend/app/page.js`
* ...

### **Phase 3: UI Fix (Invisible Overlay)**

* **The Issue**: The "Optimize Now" button is visible but completely unclickable.
* **Target Files**: `frontend/app/page.js` & `frontend/app/globals.css`
* ...

---

## ⚡ Recommended Prompts

Instead of fixing everything at once, try these targeted prompts:

1. **Phase 1**: "In Project 07, the backend in `backend/app.py` is crashing with a KeyError when the Type parameter is missing. Can you fix it safely?"
2. **Phase 2**: "The counter in `frontend/app/page.js` is concatenating strings as '01' after a reset. Can you fix the state logic?"
3. **Phase 3**: "The 'Optimize Now' button is visible but unclickable. Can you check the UI overlay in `page.js` and `globals.css`?"
