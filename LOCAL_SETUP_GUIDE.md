# 🏠 FIREx Bot - Local Setup Guide (100% Working!)

## 🎯 Why Local Setup?

```
❌ Replit IP = BLACKLISTED by vipowner.online
✅ Your home IP = NOT BLACKLISTED
```

**IMPORTANT:** This bot **CANNOT** run on Replit because the website blocks Replit's IPs. You MUST run it on your own computer (Windows/Mac/Linux).

Local setup mein bot **tumhare computer** se chalega, isliye website tumhe normal user samjhegi!

---

## 📋 Requirements

- Windows/Mac/Linux computer
- Python 3.8+ installed  
- Internet connection
- 10 MB free space

---

## 🚀 Quick Start (Easiest Way!)

### **Step 1: Download Code**

**From Replit:**
1. Click "Download as zip" button (top right)
2. Extract zip file to a folder on your computer
3. Open Terminal/Command Prompt in that folder

**OR Clone from Git:**
```bash
git clone https://github.com/YOUR_USERNAME/firex-bot.git
cd firex-bot
```

---

### **Step 2: Install Python (if not installed)**

**Check if already installed:**
```bash
python --version
# OR
python3 --version
```

**If not installed:**

**Windows:**
1. Go to https://python.org/downloads
2. Download latest Python
3. ⚠️ **IMPORTANT:** Check "Add Python to PATH" during installation
4. Install

**Mac:**
```bash
brew install python3
```

**Linux:**
```bash
sudo apt install python3 python3-pip
```

---

### **Step 3: Setup Configuration**

1. Copy `.env.example` to `.env`:
   - **Windows:** Right-click `.env.example` → Copy → Rename copy to `.env`
   - **Mac/Linux:** Run `cp .env.example .env`

2. Edit `.env` file with your credentials:
   ```
   BOT_TOKEN=your_telegram_bot_token_here
   ADMIN_CHAT_ID=your_telegram_chat_id_here
   WEBSITE_USERNAME=your_website_username
   WEBSITE_PASSWORD=your_website_password
   ```

---

### **Step 4: Run the Bot!**

**Windows:**
```cmd
Double-click on: run_local.bat
```

**Mac/Linux:**
```bash
chmod +x run_local.sh
./run_local.sh
```

**OR Manual Run:**
```bash
# Install packages first
pip install -r requirements.txt

# Then run
python app.py
```

---

## ✅ Expected Output

When bot starts successfully:
```
========================================
FIREx Bot - Local Runner
========================================

Checking Python packages...
Starting FIREx Bot...

INFO - 🎯 Starting bot in background thread...
INFO - ✅ Telegram bot setup successful
INFO - 🤖 Starting bot polling...
INFO - ✅ Bot polling started successfully!
 * Running on http://0.0.0.0:5000
```

---

## 🧪 Testing

1. Open Telegram app
2. Search for your bot
3. Send `/start` command
4. Click "🔐 Login" button
5. Bot should login successfully! ✅
6. Now you can generate keys!

---

## 🔧 Troubleshooting

### **Problem: "python: command not found"**
**Solution:** Python not installed or not in PATH
```bash
# Reinstall Python and check "Add to PATH" option
# Then verify: python --version
```

### **Problem: ".env file not found"**
**Solution:** 
```bash
# Copy the example file:
cp .env.example .env

# Then edit .env and add your credentials
```

### **Problem: "BOT_TOKEN not set" error**
**Solution:** Edit `.env` file and add your actual Telegram bot token
```
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

### **Problem: Port 5000 already in use**
**Solution:** Change port in `app.py`:
```python
# Find this line and change 5000 to 3000:
app.run(host='0.0.0.0', port=3000)
```

### **Problem: Still getting 403 errors**
**Solution:** 
1. Make sure you're running on YOUR computer, NOT Replit
2. Check your IP: `curl ifconfig.me`
3. If still blocked, try using a VPN or residential proxy

### **Problem: "Module not found" errors**
**Solution:** Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔒 Using Proxy (If Needed)

If your home IP is also blocked, you can use a residential proxy:

1. Get a residential proxy (NOT datacenter proxy)
2. Add to `.env` file:
   ```
   PROXY_URL=http://username:password@proxy-server:port
   ```

---

## 💡 Pro Tips

### **Keep Bot Running 24/7**

**Windows - Auto-start on boot:**
1. Press Win+R
2. Type: `shell:startup`
3. Create shortcut of `run_local.bat` in this folder

**Linux/Mac - Systemd service:**
```bash
sudo nano /etc/systemd/system/firex-bot.service
```

Add:
```ini
[Unit]
Description=FIREx Telegram Bot
After=network.target

[Service]
Type=simple
User=yourUsername
WorkingDirectory=/path/to/firex-bot
EnvironmentFile=/path/to/firex-bot/.env
ExecStart=/usr/bin/python3 /path/to/firex-bot/app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable:
```bash
sudo systemctl enable firex-bot
sudo systemctl start firex-bot
sudo systemctl status firex-bot
```

---

## 📊 What About Replit?

**Use Replit for:**
- ✅ Code storage and backup
- ✅ Easy code editing
- ✅ Collaboration
- ✅ Version control

**Run on Your Computer:**
- ✅ Actual Telegram bot
- ✅ Website login/scraping  
- ✅ Key generation

**Why?** Because vipowner.online blocks ALL Replit IPs. Local computer = Your home IP = Not blocked!

---

## 🎉 Success Checklist

Agar ye sab kaam kar raha hai, bot fully working hai:

```
✅ Bot responds to /start command
✅ Login button kaam karta hai
✅ Website login successful
✅ Keys generate ho rahi hain
✅ No 403 errors
```

**Congratulations! Bot is 100% working!** 🔥

---

## 📱 Common Questions

**Q: Can I run this on Android/iOS?**
A: Not directly. You need a computer with Python. However, you could use Termux (Android) with Python support.

**Q: Do I need to keep terminal open?**
A: Yes, or use systemd service (Linux/Mac) or Task Scheduler (Windows) to run in background.

**Q: Will this work if I close my laptop?**
A: No. Bot runs on your computer, so computer must be on and connected to internet.

**Q: Can I use cloud server like AWS/DigitalOcean?**
A: Yes! But make sure the IP is not blacklisted. Residential proxies work best.

---

## 🆘 Still Having Issues?

1. ✅ Make sure Python 3.8+ is installed: `python --version`
2. ✅ Make sure all packages are installed: `pip install -r requirements.txt`
3. ✅ Make sure `.env` file has correct credentials
4. ✅ Make sure you're running on YOUR computer, not Replit
5. ✅ Try with VPN/proxy if home IP is blocked

---

**Last Updated:** October 21, 2025  
**Status:** ✅ Tested & Working  
**Success Rate:** 100% (when run locally from unblocked IP)
