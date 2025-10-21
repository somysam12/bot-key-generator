# FIREx Telegram Bot

## Overview
Ye ek Telegram bot hai jo FIREx website (vipowner.online/FIREx) se automatically keys generate karta hai. Bot user ko login karke different durations ke liye keys generate karne ki facility deta hai.

## Features
- Telegram bot se direct key generation
- Multiple duration options (1day, 1week, 1month, 3months)
- Automatic website login
- Flask web server for health checks (Render deployment ke liye)

## Bot Commands
- `/start` - Welcome message aur instructions
- `/login` - FIREx website pe login karo
- `/getkey` - 1 day key generate karo (default)
- `/getkey 1week` - 1 week ki key
- `/getkey 1month` - 1 month ki key
- `/getkey 3months` - 3 months ki key
- `/status` - Login status check karo
- `/help` - Help message

## Architecture
- **Flask App**: Health check endpoints (`/`, `/health`, `/test`) for Render deployment
- **Telegram Bot**: Background thread me polling mode me chalta hai
- **Web Scraping**: requests aur BeautifulSoup use karke website se keys extract karta hai

## Environment Variables (Secrets)
- `BOT_TOKEN` - Telegram bot token (BotFather se)
- `FIREX_USERNAME` - FIREx website username
- `FIREX_PASSWORD` - FIREx website password
- `RENDER` - Set to "true" for Render deployment

## Render Deployment Setup

### Step 1: Render pe Web Service banao
1. Render.com pe login karo
2. "New +" click karke "Web Service" select karo
3. Apna GitHub repository connect karo (ya manual deployment)

### Step 2: Configuration
**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn app:app --bind 0.0.0.0:$PORT
```

### Step 3: Environment Variables Add karo
Render dashboard me Environment section me ye variables add karo:
- `BOT_TOKEN` = Your Telegram bot token
- `FIREX_USERNAME` = ishashwat
- `FIREX_PASSWORD` = 844121
- `RENDER` = true

### Step 4: Deploy karo
"Create Web Service" ya "Deploy" button click karo. Bot automatically start ho jayega!

## How It Works
1. User `/login` command use karta hai
2. Bot FIREx website pe credentials se login karta hai
3. User `/getkey <duration>` command use karta hai
4. Bot website pe key generation request bhejta hai
5. Bot response se key extract karke user ko bhej deta hai

## Technical Stack
- Python 3.11
- python-telegram-bot 13.15
- Flask 2.3.3
- gunicorn 21.2.0
- requests 2.31.0
- beautifulsoup4 4.12.2

## Files
- `app.py` - Main bot code aur Flask server
- `requirements.txt` - Python dependencies
- `Procfile` - Heroku/Render deployment config
- `runtime.txt` - Python version specification

## Last Updated
October 21, 2025
