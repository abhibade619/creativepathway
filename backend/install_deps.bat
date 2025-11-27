@echo off
echo Installing dependencies in active Conda environment...
echo.
pip install fastapi uvicorn[standard] sqlalchemy pydantic requests beautifulsoup4 python-multipart python-dotenv
echo.
echo Dependencies installed!
echo.
echo Now seeding database...
python seed_data.py
echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the server, run:
echo uvicorn main:app --reload
echo.
pause
