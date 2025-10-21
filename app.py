import os
import logging
from flask import Flask
import requests
from bs4 import BeautifulSoup
import re
import threading

# Flask app for Render health checks
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 FIREx Bot is running!", 200

@app.route('/health')
def health():
    return "✅ Healthy", 200

@app.route('/start-bot')
def start_bot():
    return "Bot is ready! Use Telegram to interact.", 200

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class FirexKeyBot:
    def __init__(self):
        self.session = None
        self.logged_in = False
        self.bot = None
        
    def setup_bot(self):
        """Setup telegram bot"""
        try:
            from telegram.ext import Updater, CommandHandler, CallbackContext
            from telegram import Update
            
            BOT_TOKEN = os.getenv('BOT_TOKEN')
            if not BOT_TOKEN:
                logger.error("❌ BOT_TOKEN not set!")
                return False
            
            self.updater = Updater(BOT_TOKEN, use_context=True)
            self.dispatcher = self.updater.dispatcher
            
            # Register handlers
            self.dispatcher.add_handler(CommandHandler("start", self.start))
            self.dispatcher.add_handler(CommandHandler("login", self.login))
            self.dispatcher.add_handler(CommandHandler("getkey", self.get_key))
            self.dispatcher.add_handler(CommandHandler("status", self.status))
            self.dispatcher.add_handler(CommandHandler("help", self.help_command))
            
            logger.info("✅ Telegram bot setup successful")
            return True
            
        except ImportError as e:
            logger.error(f"❌ Telegram import error: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Bot setup error: {e}")
            return False
    
    def start(self, update, context):
        """Send welcome message"""
        from telegram import Update
        user = update.effective_user
        welcome_text = f"""
🔥 Namaste {user.first_name}! FIREx Key Generator Bot 🔥

Available Commands:
/login - Website pe login karein
/getkey - 1 day key generate karein  
/getkey 1week - 1 week key
/getkey 1month - 1 month key
/status - Login status check karein
/help - Help message

Pehle /login command use karein
        """
        update.message.reply_text(welcome_text)
    
    def help_command(self, update, context):
        """Help message"""
        help_text = """
📋 **How to use this bot:**

1. First use `/login` to login to FIREx website
2. Then use `/getkey` to generate keys
3. You can specify duration:
   - `/getkey` (default 1 day)
   - `/getkey 1week` 
   - `/getkey 1month`
   - `/getkey 3months`

🔧 **Need help?** Contact admin.
        """
        update.message.reply_text(help_text)
    
    def status(self, update, context):
        """Check login status"""
        if self.logged_in and self.session:
            update.message.reply_text("✅ Bot logged in hai aur ready hai!")
        else:
            update.message.reply_text("❌ Bot logged in nahi hai. `/login` use karein.")
    
    def login(self, update, context):
        """Login to FIREx website"""
        update.message.reply_text("🔄 FIREx mein login ho raha hai...")
        
        try:
            self.session = requests.Session()
            
            # Modern headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://vipowner.online',
                'Referer': 'https://vipowner.online/FIREx/login',
            }
            
            self.session.headers.update(headers)
            
            # Login credentials
            login_data = {
                'username': os.getenv('FIREX_USERNAME', 'ishashwat'),
                'password': os.getenv('FIREX_PASSWORD', '844121')
            }
            
            # Login request
            login_url = "https://vipowner.online/FIREx/login"
            response = self.session.post(
                login_url, 
                data=login_data, 
                allow_redirects=True,
                timeout=30
            )
            
            # Check login success
            if response.status_code == 200:
                if "logout" in response.text.lower() or "dashboard" in response.text.lower():
                    self.logged_in = True
                    update.message.reply_text("✅ Login successful! Ab aap `/getkey` use kar sakte hain.")
                    logger.info("FIREx login successful")
                else:
                    update.message.reply_text("❌ Login failed. Please check credentials.")
            else:
                update.message.reply_text(f"❌ Login failed. HTTP Status: {response.status_code}")
                
        except requests.exceptions.Timeout:
            update.message.reply_text("❌ Login timeout. Website slow hai, please try again.")
        except requests.exceptions.ConnectionError:
            update.message.reply_text("❌ Connection error. Internet check karein.")
        except Exception as e:
            update.message.reply_text(f"❌ Login error: {str(e)}")
    
    def get_key(self, update, context):
        """Generate key with specified duration"""
        if not self.logged_in or not self.session:
            update.message.reply_text("❌ Pehle `/login` command use karein.")
            return
        
        # Duration handling
        duration_map = {
            '1day': '1day',
            '1week': '1week', 
            '1month': '1month',
            '3months': '3months'
        }
        
        duration = "1day"  # default
        
        if context.args:
            duration_arg = context.args[0].lower()
            duration = duration_map.get(duration_arg, "1day")
        
        update.message.reply_text(f"🔄 {duration} key generate ho rahi hai...")
        
        try:
            # Key generation
            key_url = "https://vipowner.online/FIREx/keys/generate"
            
            key_data = {
                'duration': duration
            }
            
            response = self.session.post(
                key_url, 
                data=key_data,
                timeout=30
            )
            
            if response.status_code == 200:
                generated_key = self._extract_key_from_response(response)
                
                if generated_key:
                    message = f"""
🎉 **Key Successfully Generated!**

🔑 **Key:** `{generated_key}`
⏰ **Duration:** {duration}

✅ **Enjoy!**
                    """
                    update.message.reply_text(message, parse_mode='Markdown')
                    logger.info(f"Key generated successfully: {duration}")
                else:
                    update.message.reply_text(
                        "⚠️ Key generate hui lekin extract nahi ho payi. "
                        "Kripya manually website check karein."
                    )
            else:
                update.message.reply_text(f"❌ Key generation failed. Status: {response.status_code}")
                
        except requests.exceptions.Timeout:
            update.message.reply_text("❌ Key generation timeout. Please try again.")
        except Exception as e:
            update.message.reply_text(f"❌ Error: {str(e)}")
    
    def _extract_key_from_response(self, response):
        """Extract key from response using multiple methods"""
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Method 1: Input fields
            input_fields = soup.find_all('input', {'type': 'text'})
            for field in input_fields:
                value = field.get('value', '').strip()
                if value and self._looks_like_key(value):
                    return value
            
            # Method 2: Code blocks
            key_elements = soup.find_all(['code', 'pre'])
            for element in key_elements:
                text = element.get_text().strip()
                if self._looks_like_key(text):
                    return text
            
            # Method 3: Regex patterns
            text_content = soup.get_text()
            key_patterns = [
                r'[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}',
                r'[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}',
                r'[A-Za-z0-9]{16,32}',
            ]
            
            for pattern in key_patterns:
                matches = re.findall(pattern, text_content)
                if matches:
                    return matches[0]
                    
            return None
            
        except Exception as e:
            logger.error(f"Key extraction error: {e}")
            return None
    
    def _looks_like_key(self, text):
        """Check if text looks like a key"""
        if not text or len(text) < 8:
            return False
        
        has_upper = bool(re.search(r'[A-Z]', text))
        has_digits = bool(re.search(r'\d', text))
        has_dashes = '-' in text
        
        return (has_upper or has_digits) and (len(text) >= 8)
    
    def run_polling(self):
        """Start bot with polling"""
        try:
            if self.setup_bot():
                logger.info("🤖 Starting bot polling...")
                self.updater.start_polling()
                self.updater.idle()
            else:
                logger.error("❌ Failed to setup bot")
        except Exception as e:
            logger.error(f"❌ Bot polling error: {e}")

# Global bot instance
firex_bot = FirexKeyBot()

def start_bot_background():
    """Start bot in background thread"""
    try:
        firex_bot.run_polling()
    except Exception as e:
        logger.error(f"Background bot error: {e}")

@app.route('/test-bot')
def test_bot():
    """Test bot setup"""
    try:
        if firex_bot.setup_bot():
            return "✅ Bot setup successful!", 200
        else:
            return "❌ Bot setup failed!", 500
    except Exception as e:
        return f"❌ Bot test error: {str(e)}", 500

# Start bot when app starts
if os.getenv('RENDER', '').lower() == 'true':
    logger.info("🚀 Starting bot in background thread...")
    bot_thread = threading.Thread(target=start_bot_background)
    bot_thread.daemon = True
    bot_thread.start()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
