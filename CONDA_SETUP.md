# Conda Setup Guide for Creative Pathways Explorer

## 🐍 Setting Up with Conda (Isolated Environment)

Follow these steps to set up the project in a completely isolated Conda environment:

---

## Step 1: Open Anaconda Prompt

**Important:** You must use **Anaconda Prompt**, not regular Command Prompt or PowerShell!

Find it in your Start Menu:
- Search for "Anaconda Prompt"
- Or look in: Start → Anaconda3 → Anaconda Prompt

---

## Step 2: Navigate to Backend Directory

In Anaconda Prompt, run:
```bash
cd C:\Users\abhib\Documents\projectsss\capstone_6980\backend
```

---

## Step 3: Run the Setup Script

```bash
setup_conda.bat
```

This will:
1. ✅ Create a new Conda environment called `creative_pathways`
2. ✅ Install Python 3.11 in that environment
3. ✅ Install all required packages (FastAPI, SQLAlchemy, etc.)
4. ✅ Seed the database with 5 sample artists

**This environment is completely isolated from your other projects!**

---

## Step 4: Start the Backend

After setup completes, in Anaconda Prompt:

```bash
conda activate creative_pathways
uvicorn main:app --reload
```

Or simply run:
```bash
start_conda.bat
```

The backend will be available at:
- **API**: http://localhost:8000
- **Docs**: http://localhost:8000/docs

---

## Step 5: Start the Frontend

Open a **new regular terminal** (PowerShell or Command Prompt is fine for this):

```bash
cd C:\Users\abhib\Documents\projectsss\capstone_6980\frontend
npm run dev
```

The frontend will be available at: **http://localhost:5173**

---

## 🎯 Daily Usage

### To Start Backend:
1. Open **Anaconda Prompt**
2. Run:
   ```bash
   conda activate creative_pathways
   cd C:\Users\abhib\Documents\projectsss\capstone_6980\backend
   uvicorn main:app --reload
   ```

### To Start Frontend:
1. Open **regular terminal**
2. Run:
   ```bash
   cd C:\Users\abhib\Documents\projectsss\capstone_6980\frontend
   npm run dev
   ```

---

## 🔍 Verify Conda Environment

To see all your Conda environments:
```bash
conda env list
```

You should see `creative_pathways` in the list.

To check what's installed in the environment:
```bash
conda activate creative_pathways
pip list
```

---

## 🗑️ To Remove the Environment (When Done)

If you ever want to completely remove this project's environment:

```bash
conda deactivate
conda env remove -n creative_pathways
```

This won't affect your other projects at all!

---

## ✅ Benefits of Conda Environment

- ✅ **Completely isolated** from your other project
- ✅ **No package conflicts** - each project has its own packages
- ✅ **Easy to manage** - activate/deactivate as needed
- ✅ **Clean removal** - just delete the environment when done
- ✅ **Reproducible** - same environment on any machine

---

## 🚨 Troubleshooting

**"conda is not recognized"**
- Make sure you're using **Anaconda Prompt**, not regular Command Prompt
- If Anaconda Prompt isn't available, you may need to install Anaconda/Miniconda

**"Environment already exists"**
- Remove it first: `conda env remove -n creative_pathways`
- Then run setup again

**"Permission denied"**
- Run Anaconda Prompt as Administrator
- Right-click → "Run as administrator"

---

## 📝 Manual Setup (Alternative)

If the script doesn't work, you can do it manually in Anaconda Prompt:

```bash
# Create environment
conda create -n creative_pathways python=3.11 -y

# Activate it
conda activate creative_pathways

# Navigate to backend
cd C:\Users\abhib\Documents\projectsss\capstone_6980\backend

# Install dependencies
pip install fastapi uvicorn[standard] sqlalchemy pydantic requests beautifulsoup4 python-multipart python-dotenv

# Seed database
python seed_data.py

# Start server
uvicorn main:app --reload
```

---

## 🎉 You're All Set!

Once both servers are running, visit:
- **Frontend**: http://localhost:5173
- **Backend API Docs**: http://localhost:8000/docs

Follow the **walkthrough.md** for testing the complete application!
