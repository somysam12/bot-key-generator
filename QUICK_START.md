# 🔥 FIREx Bot - Quick Start Guide

## ⚡ Fast Setup (3 Steps)

Website has strong anti-bot protection, isliye **manual session extraction** sabse reliable hai!

### Step 1: Session Banao (Manual Method - 100% Works!)

```bash
python extract_session_manual.py
```

**Kya karna hai:**

1. Browser mein **https://vipowner.online/FIREx/** kholo
2. **Login** karo (username: ishashwat, password: 844121)
3. **F12** dabao (Developer Tools)
4. **Console** tab pe jao
5. Type karo: `document.cookie`
6. Output **copy** karo
7. Script mein **paste** karo

**Done!** ✅ Session ban gaya!

### Step 2: Bot Chalo

Bot already chal raha hai! Workflow "FIREx Bot" check karo.

### Step 3: Test Karo

Telegram pe apne bot ko `/start` command bhejo!

---

## 🎯 Why Manual Method?

Website uses:
- ❌ Cloudflare protection
- ❌ Anti-bot detection  
- ❌ IP filtering
- ❌ TLS fingerprinting

**Manual login** se ye sab bypass ho jata hai!

---

## 📋 Bot Commands

- `/start` - Welcome message
- `/login` - Manual login (agar session expire ho)
- `/getkey` - Key generate karo
- `/status` - Login status check
- `/help` - Help

---

## ✅ Session Features

- **Auto-load**: Bot startup pe automatic load hoga
- **Validation**: Expire hua to detect karega
- **Persistent**: Bot restart ke baad bhi valid
- **Same IP**: Saved cookies se same session

---

## 🔧 Troubleshooting

**Session expire ho gaya?**
```bash
python extract_session_manual.py
```
Phir se cookies extract karo!

**Bot offline hai?**
Check workflow logs - bot running hona chahiye.

---

**💡 Pro Tip:** Ek baar session ban gaya to bot hamesha wohi use karega. Baar-baar extract nahi karna padega!
