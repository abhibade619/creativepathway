# Quick Commands for Conda Environment

## You are here: (creative_pathways) environment is ACTIVE ✅

### Step 1: Install Dependencies
```bash
pip install fastapi uvicorn[standard] sqlalchemy pydantic requests beautifulsoup4 python-multipart python-dotenv
```

### Step 2: Seed Database
```bash
python seed_data.py
```

### Step 3: Start Backend Server
```bash
uvicorn main:app --reload
```

### Step 4: Start Frontend (in NEW terminal)
```bash
cd C:\Users\abhib\Documents\projectsss\capstone_6980\frontend
npm run dev
```

---

## Or use the script:
```bash
install_deps.bat
```
