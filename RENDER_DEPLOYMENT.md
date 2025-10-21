# Render Deployment Guide - FIREx Telegram Bot

## 📋 Pre-requisites
1. GitHub account
2. Render.com account (free signup)
3. Telegram Bot Token (BotFather se prapt karein)
4. FIREx website credentials

## 🚀 Step-by-Step Deployment

### Step 1: GitHub Repository Setup
1. Apne code ko GitHub repository me push karein
2. Ya directly Render pe manual deployment use karein

### Step 2: Render Web Service Create karein

1. **Render Dashboard pe jaayein**
   - https://render.com/ pe login karein
   - "New +" button click karein
   - "Web Service" select karein

2. **Repository Connect karein**
   - Apna GitHub repository select karein
   - Ya "Public Git repository" option use karein aur repository URL dalein

3. **Service Configuration**
   ```
   Name: firex-telegram-bot (ya koi bhi naam)
   Region: Singapore (ya nearest region)
   Branch: main
   Runtime: Python 3
   ```

4. **Build & Start Commands**
   ```
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app --bind 0.0.0.0:$PORT
   ```

5. **Instance Type**
   - Free tier select karein (ya paid plan as needed)

### Step 3: Environment Variables Set karein

Render dashboard me **Environment** section me jaake ye variables add karein:

| Variable Name | Value | Description |
|--------------|--------|-------------|
| `BOT_TOKEN` | Your bot token | BotFather se mila hua token |
| `FIREX_USERNAME` | ishashwat | FIREx website username |
| `FIREX_PASSWORD` | 844121 | FIREx website password |
| `RENDER` | true | Render environment flag |

**Important:** Sabhi values ko carefully enter karein, koi space na rahe.

### Step 4: Deploy karein

1. "Create Web Service" button click karein
2. Render automatically build aur deploy karega
3. Deployment logs dekhein - ensure koi error na ho
4. Service URL mil jayega (e.g., `https://firex-telegram-bot.onrender.com`)

### Step 5: Verify Deployment

1. **Health Check**
   - Browser me apna service URL kholein
   - Aapko "🤖 FIREx Bot is running!" message dikhna chahiye

2. **Endpoints Test karein**
   ```
   https://your-service.onrender.com/
   https://your-service.onrender.com/health
   https://your-service.onrender.com/test
   ```

3. **Telegram Bot Test karein**
   - Telegram me apne bot ko search karein
   - `/start` command bhejein
   - Commands use karke verify karein

## 🤖 Bot Usage

### Available Commands
```
/start    - Welcome message aur instructions
/login    - FIREx website pe login karein
/getkey   - 1 day key generate karein (default)
/getkey 1week    - 1 week key
/getkey 1month   - 1 month key  
/getkey 3months  - 3 months key
/status   - Login status check karein
/help     - Help message
```

### Example Usage Flow
```
1. User: /start
   Bot: Welcome message with commands

2. User: /login
   Bot: Login ho raha hai...
   Bot: ✅ Login successful!

3. User: /getkey 1week
   Bot: 1week key generate ho rahi hai...
   Bot: 🎉 Key Successfully Generated!
        🔑 Key: XXXX-XXXX-XXXX-XXXX
        ⏰ Duration: 1week
```

## 🔧 Troubleshooting

### Bot Respond nahi kar raha
1. Render dashboard me logs check karein
2. Environment variables sahi se set hain ya nahi verify karein
3. Service running hai ya nahi check karein

### Login Fail ho raha hai
1. FIREX_USERNAME aur FIREX_PASSWORD correct hain verify karein
2. Website https://vipowner.online/FIREx/ accessible hai check karein

### Key Generate nahi ho rahi
1. Pehle `/login` command use karein
2. Website structure change hua to code update karni hogi

## 📊 Monitoring

### Render Dashboard Features
- **Logs**: Real-time application logs
- **Metrics**: CPU, Memory usage
- **Events**: Deployment history
- **Shell**: Direct server access

### Health Check Endpoints
- `/` - Basic status
- `/health` - Health check
- `/test` - Server active test

## 💰 Cost Information

### Free Tier Limits
- 750 hours/month free
- Service spins down after 15 minutes of inactivity
- Cold start: 30-60 seconds

### Paid Plans
- Starter: $7/month - Always on, no spin down
- Standard: $25/month - More resources

**Recommendation**: Free tier se start karein, traffic badhe to upgrade karein.

## 🔄 Updates & Maintenance

### Code Update karne ke liye
1. GitHub repository me code push karein
2. Render automatically detect karke deploy karega
3. Ya manually "Deploy latest commit" button use karein

### Environment Variables Update
1. Render dashboard > Environment tab
2. Variables update karein
3. Service automatically restart hoga

## 📝 Important Files

```
app.py              - Main bot code aur Flask server
requirements.txt    - Python dependencies
Procfile           - Deployment configuration
runtime.txt        - Python version
replit.md          - Project documentation
```

## 🛡️ Security Best Practices

1. **Secrets**: Kabhi bhi tokens/passwords code me hardcode na karein
2. **Environment Variables**: Sab sensitive data environment variables me rakhein
3. **HTTPS**: Render automatically SSL certificate provide karta hai
4. **Logs**: Sensitive data logs me print na karein

## 📞 Support

### Issues Face kar rahe hain?
1. Render logs carefully padhein
2. Error messages note karein
3. Configuration recheck karein

### Helpful Links
- Render Docs: https://render.com/docs
- Python Telegram Bot Docs: https://python-telegram-bot.readthedocs.io/
- FIREx Website: https://vipowner.online/FIREx/

---

**Note**: Ye bot production-ready hai. Render pe deploy karne ke baad 24/7 automatically keys generate karega jab bhi user request karega.

Good Luck! 🚀
