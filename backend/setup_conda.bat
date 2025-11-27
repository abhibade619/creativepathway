@echo off
echo ========================================
echo Creative Pathways Explorer - Conda Setup
echo ========================================
echo.
echo IMPORTANT: Run this script from Anaconda Prompt, not regular Command Prompt!
echo.
echo If you see "conda is not recognized", please:
echo 1. Open "Anaconda Prompt" from Start Menu
echo 2. Navigate to this folder: cd C:\Users\abhib\Documents\projectsss\capstone_6980\backend
echo 3. Run this script again: setup_conda.bat
echo.
pause

echo Step 1: Creating Conda environment 'creative_pathways'...
conda create -n creative_pathways python=3.11 -y
if errorlevel 1 (
    echo.
    echo ERROR: Failed to create conda environment
    echo Make sure you're running this from Anaconda Prompt!
    pause
    exit /b 1
)
echo ✓ Conda environment created

echo.
echo Step 2: Activating environment...
call conda activate creative_pathways
if errorlevel 1 (
    echo ERROR: Failed to activate environment
    pause
    exit /b 1
)
echo ✓ Environment activated

echo.
echo Step 3: Installing dependencies...
pip install fastapi==0.104.1 uvicorn[standard]==0.24.0 sqlalchemy==2.0.23 pydantic==2.5.0 requests==2.31.0 beautifulsoup4==4.12.2 python-multipart==0.0.6 python-dotenv==1.0.0
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed

echo.
echo Step 4: Seeding database with sample artists...
python seed_data.py
if errorlevel 1 (
    echo ERROR: Failed to seed database
    pause
    exit /b 1
)
echo ✓ Database seeded with 5 artists!

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Your isolated Conda environment 'creative_pathways' is ready!
echo.
echo To start the backend server:
echo   1. Open Anaconda Prompt
echo   2. Run: conda activate creative_pathways
echo   3. Run: cd C:\Users\abhib\Documents\projectsss\capstone_6980\backend
echo   4. Run: uvicorn main:app --reload
echo.
echo Or simply run: start_conda.bat
echo.
pause
