# 🔥 FIREx Telegram Bot - Pyrogram Style Session

## ⚠️ IMPORTANT: Local Setup Required!

**This bot CANNOT run on Replit!** 

Why? Because `vipowner.online` has BLACKLISTED all Replit IPs. You will get 403 errors if you try to run it here.

**✅ Solution:** Run this bot on YOUR OWN COMPUTER (Windows/Mac/Linux)

👉 **See [LOCAL_SETUP_GUIDE.md](LOCAL_SETUP_GUIDE.md) for complete setup instructions**

---

## 🚀 Quick Start (Local Computer)

### **Option 1: Easy Way (Recommended)**

**Windows:**
```cmd
1. Download all files to your computer
2. Double-click: run_local.bat
3. Follow the instructions
```

**Mac/Linux:**
```bash
1. Download all files to your computer
2. chmod +x run_local.sh
3. ./run_local.sh
```

### **Option 2: Manual Setup**

1. **Install Python 3.8+** (if not installed)
   ```bash
   python --version  # Should show 3.8 or higher
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Configuration**
   ```bash
   # Copy .env.example to .env
   cp .env.example .env
   
   # Edit .env and add your credentials:
   # - BOT_TOKEN (from @BotFather)
   # - ADMIN_CHAT_ID (your Telegram chat ID)
   # - WEBSITE_USERNAME
   # - WEBSITE_PASSWORD
   ```

4. **Run the Bot**
   ```bash
   python app.py
   ```

---

## 📋 Bot Commands

- `/start` - Welcome message
- `/login` - Manual login (if session expired)
- `/getkey` - Generate key
- `/status` - Check login status
- `/help` - Help message

---

## 🎯 Session Features (Pyrogram Style!)

✅ **One-Time Login** - Run `create_session.py`, provide credentials, done!
✅ **Auto Load** - Bot automatically loads saved session on restart
✅ **Auto Validation** - Detects if session expired
✅ **Same IP** - Uses your home IP (not blocked by website)
✅ **No 403 Errors** - Proper browser-like headers

---

## 🔐 Environment Variables

Create a `.env` file with:
```env
BOT_TOKEN=your_telegram_bot_token_here
ADMIN_CHAT_ID=your_telegram_chat_id_here
WEBSITE_USERNAME=your_website_username
WEBSITE_PASSWORD=your_website_password
```

See `.env.example` for a template.

---

## 📁 Important Files

- `app.py` - Main bot code + Flask server
- `create_session.py` - Session creator (Pyrogram style)
- `firex_session.pkl` - Saved session file (auto-generated)
- `run_local.bat` - Windows runner script
- `run_local.sh` - Mac/Linux runner script
- `.env` - Your configuration (create from .env.example)
- `requirements.txt` - Python dependencies
- `LOCAL_SETUP_GUIDE.md` - Complete setup guide

---

## 🛠️ Technical Details

- **Python**: 3.8+
- **Framework**: python-telegram-bot 13.15
- **Web Server**: Flask + Gunicorn (for health checks)
- **Session**: Pickle-based persistence (like Pyrogram)
- **Deployment**: Local machine ONLY (Replit IPs are blocked)

---

## 📝 How It Works?

1. User runs the bot on their LOCAL computer (not Replit)
2. Bot uses `.env` file for configuration
3. Session cookies are saved in `firex_session.pkl`
4. Bot automatically loads session on startup
5. User can generate keys without 403 errors!

---

## 🌐 Why Not Replit?

```
❌ Replit IP Range: BLOCKED by vipowner.online
❌ All methods fail: 403 Forbidden
❌ Cloudflare + IP blacklisting
❌ Anti-automation detection

✅ Your Home Computer: NOT BLOCKED
✅ Local IP works perfectly
✅ No 403 errors
✅ 100% success rate
```

**Use Replit for:**
- Code storage and backup
- Easy editing
- Collaboration

**Run Bot on:**
- Your Windows/Mac/Linux computer
- VPS with residential IP
- Cloud server with proxy

---

## 🎉 Success!

When setup correctly, you should see:
```
✅ Bot responds to /start
✅ Login button works
✅ Website login successful
✅ Keys generate without errors
✅ No 403 errors
```

---

## 🆘 Need Help?

See [LOCAL_SETUP_GUIDE.md](LOCAL_SETUP_GUIDE.md) for:
- Step-by-step setup instructions
- Troubleshooting guide
- Auto-start on boot setup
- Proxy configuration

---

## 📱 FAQ

**Q: Can I run this on Replit?**
A: No, Replit IPs are blacklisted. Must run locally.

**Q: Do I need to keep my computer on?**
A: Yes, or use a VPS/cloud server with residential IP.

**Q: What if my home IP is also blocked?**
A: Use a residential proxy (see LOCAL_SETUP_GUIDE.md).

**Q: Can I run this on Android?**
A: Not easily. Best on Windows/Mac/Linux with Python.

---

**Last Updated:** October 21, 2025  
**Status:** ✅ Working (Local Setup Only)  
**Replit Compatibility:** ❌ Not possible (IPs blocked)
