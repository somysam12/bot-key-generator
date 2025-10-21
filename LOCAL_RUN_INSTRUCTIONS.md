# FIREx Bot - Local Setup Instructions (Hindi)

## Pehle Yeh Check Karein

1. **Purane bot processes band karein:**
   - Task Manager kholen (Ctrl+Shift+Esc)
   - Sabhi `python.exe` processes ko End Task karein
   - Ya terminal mein: `taskkill /F /IM python.exe`

2. **Environment variables set karein:**
   
   `.env` file banayein project folder mein:
   ```
   BOT_TOKEN=aapka_telegram_bot_token
   FIREX_USERNAME=aapka_firex_username
   FIREX_PASSWORD=aapka_firex_password
   PORT=5000
   ```

## Bot Chalane ka Tarika

### Option 1: Python Command
```bash
python app.py
```

### Option 2: Batch File (Windows)
```bash
run_local.bat
```

## Important Notes

- ✅ Ab **sirf ek bot instance** chalega - duplicate issue fix ho gaya
- ✅ Flask debug mode off hai - auto-restart nahi hoga
- ✅ Signal error fix ho gaya
- ⚠️ **Bas ek baar `python app.py` run karein** - do baar na chalayein

## Agar Error Aaye

**"Conflict: terminated by other getUpdates"** 
- Matlab koi aur bot instance chal raha hai
- Solution: 
  1. Sabhi Python processes band karein
  2. 30 second wait karein
  3. Phir se bot start karein

**"Bot credentials not configured"**
- `.env` file check karein
- Ensure karo ki `FIREX_USERNAME` aur `FIREX_PASSWORD` sahi hai

## Test Karne ka Tarika

1. Bot start karo: `python app.py`
2. Telegram pe bot ko `/start` bhejo
3. Login button dabao
4. Agar "✅ Login successful!" aaye toh sab theek hai!

## Proxy Setup (Optional)

Agar website block kar rahi hai:
1. `.env` file mein add karein:
   ```
   PROXY_URL=http://username:password@proxy-server:port
   ```
2. Residential proxy use karein (datacenter proxy block ho sakta hai)
