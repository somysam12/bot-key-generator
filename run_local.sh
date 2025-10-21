#!/bin/bash

# FIREx Bot - Mac/Linux Local Runner
# This script runs the Telegram bot locally on your Mac/Linux machine

echo "========================================"
echo "FIREx Bot - Local Runner"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed!"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "WARNING: .env file not found!"
    echo "Please copy .env.example to .env and fill in your credentials"
    echo ""
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo ""
    echo "Please edit .env file and add your BOT_TOKEN and credentials"
    echo "Run: nano .env  (or use your preferred editor)"
    exit 1
fi

echo "Checking Python packages..."
pip3 install -r requirements.txt --quiet

echo ""
echo "Starting FIREx Bot..."
echo "Press Ctrl+C to stop"
echo ""

# Load environment variables and run the bot
set -a
source .env
set +a

python3 app.py
