# FIREx Telegram Bot

## Overview
Ye ek Telegram bot hai jo FIREx website (vipowner.online/FIREx) se automatically keys generate karta hai. Bot user ko login karke different durations ke liye keys generate karne ki facility deta hai.

## Features
- Telegram bot se direct key generation with inline keyboard buttons
- Multiple duration options (1day, 1week, 1month, 3months)
- Automatic website login with improved headers to avoid 403 errors
- **Session persistence** (Pyrogram jaise) - Ek baar login, phir automatic!
- Flask web server for health checks (Render deployment ke liye)
- User-friendly inline buttons for all commands
- Secure credential management (environment variables required)

## Bot Commands
- `/start` - Welcome message aur inline buttons
- `/login` - FIREx website pe login karo
- `/getkey` - Key generate karo (with inline buttons for duration selection)
- `/status` - Login status check karo (with inline buttons)
- `/help` - Help message (with inline buttons)

## Inline Buttons
- **Login Button** - Direct login karne ke liye
- **Duration Buttons** - 1 Day, 1 Week, 1 Month, 3 Months keys ke liye
- **Status Button** - Quick status check
- **Help Button** - Help information

## Architecture
- **Flask App**: Health check endpoints (`/`, `/health`, `/test`) for Render deployment
- **Telegram Bot**: Background thread me polling mode me chalta hai
- **Web Scraping**: requests aur BeautifulSoup use karke website se keys extract karta hai

## Environment Variables (Secrets) - REQUIRED
- `BOT_TOKEN` - Telegram bot token (BotFather se) - **REQUIRED**
- `FIREX_USERNAME` - FIREx website username - **REQUIRED**
- `FIREX_PASSWORD` - FIREx website password - **REQUIRED**
- `RENDER` - Set to "true" for Render deployment (optional)

**Important**: Credentials ab hardcoded nahi hain security ke liye. Environment variables set karna zaroori hai!

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

## Recent Updates (October 21, 2025)

### Security Improvements
- Removed hardcoded credentials from source code
- Made environment variables mandatory for security

### Feature Additions
- Added inline keyboard buttons for all bot commands
- Improved user experience with clickable buttons
- Better navigation between different bot features

### Bug Fixes
- Fixed 403 error by improving HTTP headers
- Removed Brotli encoding (unsupported by requests library)
- Added better browser-like headers (Chrome 120 User-Agent)
- Added Referer, Accept-Language, and other realistic headers
- Pre-visit to main page before login to get cookies

### Session Persistence (Pyrogram Style)
- **Session Save**: Login successful hone ke baad session cookies automatically save ho jati hain `firex_session.pkl` file mein
- **Session Load**: Bot restart hone pe automatically saved session load hota hai
- **Session Validation**: Loaded session check hota hai ki valid hai ya nahi
- **Auto Cleanup**: Agar session expire ho gaya to automatic delete ho jata hai
- **Benefits**: 
  - Baar-baar login nahi karna padta
  - Bot restart ke baad bhi session maintained rehta hai
  - Stale sessions automatically clean ho jate hain

## Last Updated
October 21, 2025
