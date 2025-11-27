@echo off
echo ========================================
echo Creative Pathways Explorer - Backend Setup
echo ========================================
echo.

echo Step 1: Creating virtual environment...
C:\Users\abhib\AppData\Local\Programs\Python\Python311\python.exe -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment created

echo.
echo Step 2: Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment activated

echo.
echo Step 3: Installing dependencies...
python -m pip install --upgrade pip
python -m pip install fastapi==0.104.1 uvicorn[standard]==0.24.0 sqlalchemy==2.0.23 pydantic==2.5.0 requests==2.31.0 beautifulsoup4==4.12.2 python-multipart==0.0.6 python-dotenv==1.0.0
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed

echo.
echo Step 4: Seeding database...
python seed_data.py
if errorlevel 1 (
    echo ERROR: Failed to seed database
    pause
    exit /b 1
)
echo ✓ Database seeded

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the backend server:
echo   1. Run: venv\Scripts\activate.bat
echo   2. Run: uvicorn main:app --reload
echo.
echo The API will be available at: http://localhost:8000
echo API docs will be at: http://localhost:8000/docs
echo.
pause
