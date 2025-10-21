import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from bs4 import BeautifulSoup
import time
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FirexKeyBot:
    def __init__(self, token):
        self.updater = Updater(token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.session = None
        self.logged_in = False
        
        # Command handlers
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("login", self.login))
        self.dispatcher.add_handler(CommandHandler("getkey", self.get_key))
        self.dispatcher.add_handler(CommandHandler("status", self.status))
        
    def start(self, update, context):
        update.message.reply_text(
            "🔥 FIREx Key Generator Bot 🔥\n\n"
            "Available Commands:\n"
            "/login - Website pe login karein\n"
            "/getkey - Key generate karein\n"
            "/status - Login status check karein\n\n"
            "Pehle /login command use karein"
        )
    
    def status(self, update, context):
        if self.logged_in:
            update.message.reply_text("✅ Bot logged in hai")
        else:
            update.message.reply_text("❌ Bot logged in nahi hai. /login use karein")
    
    def login(self, update, context):
        """FIREx website pe login karein"""
        update.message.reply_text("🔄 Logging in...")
        
        try:
            self.session = requests.Session()
            
            # Headers set karein
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://vipowner.online',
                'Referer': 'https://vipowner.online/FIREx/login'
            })
            
            # Login data
            login_data = {
                'username': 'ishashwat',
                'password': '844121'
            }
            
            # Login request
            login_url = "https://vipowner.online/FIREx/login"
            response = self.session.post(login_url, data=login_data, allow_redirects=True)
            
            # Check login success
            if response.status_code == 200:
                # Check if redirected to dashboard or still on login page
                if "login" not in response.url and "dashboard" in response.url.lower() or "keys" in response.url.lower():
                    self.logged_in = True
                    update.message.reply_text("✅ Login successful! Ab aap /getkey use kar sakte hain")
                    logger.info("Login successful")
                else:
                    update.message.reply_text("❌ Login failed. Invalid credentials ya website issue")
                    logger.error("Login failed - still on login page")
            else:
                update.message.reply_text(f"❌ Login failed. Status code: {response.status_code}")
                
        except Exception as e:
            update.message.reply_text(f"❌ Login error: {str(e)}")
            logger.error(f"Login exception: {e}")
    
    def get_key(self, update, context):
        """Key generate karein"""
        if not self.logged_in or not self.session:
            update.message.reply_text("❌ Pehle /login command use karein")
            return
        
        # Duration parameter handle karein
        duration = "1day"  # Default duration
        
        if context.args:
            duration_arg = context.args[0].lower()
            if duration_arg in ['1day', '1week', '1month', '3months']:
                duration = duration_arg
            else:
                update.message.reply_text("❌ Invalid duration. Use: 1day, 1week, 1month, 3months")
                return
        
        update.message.reply_text(f"🔄 Generating {duration} key...")
        
        try:
            # Key generation URL
            key_url = "https://vipowner.online/FIREx/keys/generate"
            
            # Key generation data - duration ke according
            key_data = {
                'duration': duration
            }
            
            # Generate key request
            response = self.session.post(key_url, data=key_data)
            
            if response.status_code == 200:
                # Response se key extract karein
                generated_key = self._extract_key_from_response(response)
                
                if generated_key:
                    update.message.reply_text(
                        f"🎉 Key Successfully Generated!\n\n"
                        f"🔑 Key: `{generated_key}`\n"
                        f"⏰ Duration: {duration}\n\n"
                        f"Copy karne ke liye click karein 👆",
                        parse_mode='Markdown'
                    )
                    logger.info(f"Key generated: {generated_key}")
                else:
                    # Agar key extract nahi ho payi toh manual check karein
                    update.message.reply_text(
                        "⚠️ Key generate hui hai lekin extract nahi ho payi. "
                        "Kripya website check karein ya fir specific duration try karein.\n\n"
                        "Usage: /getkey 1day\n/g getkey 1week\n/g getkey 1month"
                    )
            else:
                update.message.reply_text(f"❌ Key generation failed. Status: {response.status_code}")
                logger.error(f"Key generation failed: {response.status_code}")
                
        except Exception as e:
            update.message.reply_text(f"❌ Error generating key: {str(e)}")
            logger.error(f"Key generation exception: {e}")
    
    def _extract_key_from_response(self, response):
        """Response se key extract karein"""
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Different possible locations for key
            key_selectors = [
                'input[type="text"][value]',  # Input field mein key
                '.key', '.key-code', '.generated-key',  # Common key classes
                'code', 'pre',  # Code blocks
                'div.alert-success',  # Success message mein key
                'table tr td:last-child'  # Table se key
            ]
            
            for selector in key_selectors:
                elements = soup.select(selector)
                for element in elements:
                    text = element.get('value') or element.text
                    if text and len(text) > 10:  # Assuming key length > 10
                        return text.strip()
            
            # Agar koi specific selector nahi mila toh page mein key search karein
            page_text = soup.get_text()
            import re
            # Common key patterns
            key_patterns = [
                r'[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}',  # XXXX-XXXX-XXXX-XXXX
                r'[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}',  # XXXXXXXX-XXXXXXXX-XXXXXXXX
                r'[A-Za-z0-9]{16,32}',  # Alphanumeric 16-32 characters
            ]
            
            for pattern in key_patterns:
                matches = re.findall(pattern, page_text)
                if matches:
                    return matches[0]
                    
            return None
            
        except Exception as e:
            logger.error(f"Key extraction error: {e}")
            return None
    
    def run(self):
        self.updater.start_polling()
        logger.info("Bot started polling...")
        self.updater.idle()

# Main execution
if __name__ == "__main__":
    # Yeh token BotFather se milega
    BOT_TOKEN = "8398897953:AAGJMUHBFLyUyuTR_8yjfXca5fNDq050RRY"
    
    bot = FirexKeyBot(BOT_TOKEN)
    bot.run()
