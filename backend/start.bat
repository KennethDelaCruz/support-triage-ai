@echo off
REM Start script for Support Triage API (Windows)

echo Starting Support Triage API...

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found. Creating one...
    python -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment.
        echo Make sure Python is installed and in your PATH.
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if dependencies are installed
python -c "import fastapi" 2>nul
if errorlevel 1 (
    echo Dependencies not found. Installing...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Failed to install dependencies.
        exit /b 1
    )
)

REM Start the server
echo.
echo Starting server on http://localhost:8000
echo API docs available at http://localhost:8000/docs
echo.

uvicorn app.main:app --reload --port 8000

