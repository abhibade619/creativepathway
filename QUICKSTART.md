# Quick Start Guide - Creative Pathways Explorer

## 🚨 Python Environment Issue Detected

Your Python installation appears to have some configuration issues. Here are **3 ways** to get the project running:

---

## ✅ Option 1: Use the Setup Script (Recommended)

I've created an automated setup script that should handle the environment properly:

```bash
cd C:\Users\abhib\Documents\projectsss\capstone_6980\backend
setup.bat
```

This will:
1. Create a virtual environment
2. Install all dependencies
3. Seed the database
4. Give you instructions to start the server

Then to start the backend:
```bash
start.bat
```

---

## ✅ Option 2: Manual Setup with Virtual Environment

If the script doesn't work, try this manual approach:

### Step 1: Create Virtual Environment
```bash
cd C:\Users\abhib\Documents\projectsss\capstone_6980\backend
python -m venv venv
```

### Step 2: Activate Virtual Environment
```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
python -m pip install --upgrade pip
pip install fastapi uvicorn[standard] sqlalchemy pydantic requests beautifulsoup4 python-multipart python-dotenv
```

### Step 4: Seed Database
```bash
python seed_data.py
```

### Step 5: Start Backend
```bash
uvicorn main:app --reload
```

---

## ✅ Option 3: Reinstall Python (If all else fails)

If you continue to have issues:

1. **Download Python 3.11** from https://www.python.org/downloads/
2. **During installation**, make sure to check:
   - ✅ "Add Python to PATH"
   - ✅ "Install pip"
3. **Restart your terminal**
4. **Try Option 2 again**

---

## 🎯 Starting the Frontend

The frontend should work without issues:

```bash
cd C:\Users\abhib\Documents\projectsss\capstone_6980\frontend
npm run dev
```

Or use the start script:
```bash
start.bat
```

---

## 🔍 Verify Everything Works

Once both servers are running:

1. **Backend**: Open http://localhost:8000/docs
   - You should see the FastAPI interactive documentation
   - Try the `/health` endpoint

2. **Frontend**: Open http://localhost:5173
   - You should see the Creative Pathways Explorer home page
   - Click "Artists" to see the 5 sample artists

---

## 📞 Need Help?

If you're still having issues:

1. Check if Python is in your PATH: `python --version`
2. Check if pip works: `pip --version`
3. Try using `py` instead of `python`: `py -m pip install ...`
4. Check Windows environment variables for Python paths

---

## 🎉 Once It's Running

Follow the walkthrough.md for:
- Testing the complete user flow
- Understanding the matching algorithm
- Generating personalized roadmaps
- Demo video script
