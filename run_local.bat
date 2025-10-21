@echo off
REM FIREx Bot - Windows Local Runner
REM This script runs the Telegram bot locally on your Windows machine

echo ========================================
echo FIREx Bot - Local Runner
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist .env (
    echo WARNING: .env file not found!
    echo Please copy .env.example to .env and fill in your credentials
    echo.
    echo Creating .env from .env.example...
    copy .env.example .env
    echo.
    echo Please edit .env file and add your BOT_TOKEN and credentials
    pause
    exit /b 1
)

echo Checking Python packages...
echo This may take 1-2 minutes for first time...
pip install -r requirements.txt

echo.
echo Starting FIREx Bot...
echo Press Ctrl+C to stop
echo.

python app.py

pause
