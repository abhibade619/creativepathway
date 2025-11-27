@echo off
echo Starting Creative Pathways Explorer Backend (Conda)...
echo.
echo IMPORTANT: Run this from Anaconda Prompt!
echo.

call conda activate creative_pathways
if errorlevel 1 (
    echo ERROR: Conda environment 'creative_pathways' not found!
    echo Please run setup_conda.bat first from Anaconda Prompt.
    pause
    exit /b 1
)

echo ✓ Conda environment activated
echo.
echo Starting FastAPI server...
echo API will be available at: http://localhost:8000
echo API docs at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.
uvicorn main:app --reload
