# 🔥 FIREx Telegram Bot - Pyrogram Style Session

## 🚀 Quick Start

### 1️⃣ Ek Baar Session Banao (Pyrogram jaisa!)

Terminal mein ye command chalao:

```bash
python create_session.py
```

Script aapse puchega:
- **Username**: FIREx website username
- **Password**: FIREx website password

Login successful hone ke baad `firex_session.pkl` file ban jayegi! ✅

### 2️⃣ Bot Chalao

Bot already chal raha hai! Workflow "FIREx Bot" dekho.

Session file ban jane ke baad bot automatically use karega - **baar-baar login nahi karna padega!**

## 📋 Bot Commands

- `/start` - Welcome message
- `/login` - Manual login (agar session expire ho gaya ho)
- `/getkey` - Key generate karo
- `/status` - Login status check karo
- `/help` - Help message

## 🎯 Session Features (Pyrogram Style!)

✅ **Ek Baar Login** - `create_session.py` chalao, credentials do, done!
✅ **Auto Load** - Bot restart hone pe automatic session load hota hai
✅ **Auto Validation** - Session expire hua to automatic detect karta hai
✅ **Same IP** - Session saved hai to bot hamesha wohi use karega
✅ **No 403 Errors** - Proper browser-like headers use karta hai

## 🔐 Environment Variables

Bot ko ye secrets chahiye (already set hain):
- `BOT_TOKEN` - Telegram bot token
- `FIREX_USERNAME` - FIREx username (optional, agar /login command use karna ho)
- `FIREX_PASSWORD` - FIREx password (optional, agar /login command use karna ho)

**Note:** Agar aapne `create_session.py` se session bana liya hai, to bot automatically wohi use karega!

## 📁 Important Files

- `app.py` - Main bot code + Flask server
- `create_session.py` - Session creator (Pyrogram jaisa)
- `firex_session.pkl` - Saved session file (auto-generated)
- `requirements.txt` - Python dependencies

## 🛠️ Technical Details

- **Python**: 3.11
- **Framework**: python-telegram-bot 13.15
- **Web Server**: Flask + Gunicorn
- **Session**: Pickle-based persistence (like Pyrogram)

## 📝 Kaise Kaam Karta Hai?

1. User `create_session.py` chalata hai aur credentials deta hai
2. Script FIREx website pe login karta hai
3. Session cookies save ho jati hain `firex_session.pkl` mein
4. Bot start hone pe automatically session load karta hai
5. Session valid hai ya nahi check karta hai
6. User ab directly keys generate kar sakta hai!

## 🎉 Ready!

Ab aapka bot bilkul Pyrogram jaisa kaam karega - ek baar session bana lo, phir hamesha wohi use karo!
