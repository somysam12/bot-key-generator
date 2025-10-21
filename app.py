import os
import logging
import requests
from bs4 import BeautifulSoup
import re
import threading
import time
from flask import Flask

# Flask app for Render health checks
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 FIREx Bot is running!", 200

@app.route('/health')
def health():
    return "✅ Healthy", 200

@app.route('/test')
def test():
    return "🚀 Bot Server Active", 200

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
        self.updater = None
        
    def setup_bot(self):
        """Setup telegram bot"""
        try:
            from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
            
            BOT_TOKEN = os.getenv('BOT_TOKEN')
            if not BOT_TOKEN:
                logger.error("❌ BOT_TOKEN not set!")
                return False
            
            # Stable version - python-telegram-bot v13.15
            self.updater = Updater(BOT_TOKEN, use_context=True)
            self.dispatcher = self.updater.dispatcher
            
            # Register handlers
            self.dispatcher.add_handler(CommandHandler("start", self.start))
            self.dispatcher.add_handler(CommandHandler("login", self.login))
            self.dispatcher.add_handler(CommandHandler("getkey", self.get_key))
            self.dispatcher.add_handler(CommandHandler("status", self.status))
            self.dispatcher.add_handler(CommandHandler("help", self.help_command))
            
            # Register callback query handler for button clicks
            self.dispatcher.add_handler(CallbackQueryHandler(self.button_callback))
            
            logger.info("✅ Telegram bot setup successful")
            return True
            
        except Exception as e:
            logger.error(f"❌ Bot setup error: {e}")
            return False
    
    def start(self, update, context):
        """Send welcome message with inline buttons"""
        from telegram import InlineKeyboardButton, InlineKeyboardMarkup
        
        user = update.effective_user
        welcome_text = f"""
🔥 Namaste {user.first_name}! FIREx Key Generator Bot 🔥

Available Commands:
/login - Website pe login karein
/getkey - Key generate karein  
/status - Login status check karein
/help - Help message

Pehle login button dabayein!
        """
        
        keyboard = [
            [InlineKeyboardButton("🔐 Login", callback_data='login')],
            [
                InlineKeyboardButton("📊 Status", callback_data='status'),
                InlineKeyboardButton("❓ Help", callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        update.message.reply_text(welcome_text, reply_markup=reply_markup)
    
    def help_command(self, update, context):
        """Help message with buttons"""
        from telegram import InlineKeyboardButton, InlineKeyboardMarkup
        
        help_text = """
📋 **Bot Kaise Use Karein:**

1. Pehle Login button dabayein
2. Phir key generate button dabayein
3. Apne duration select karein

🔧 **Need help?** Contact admin.
        """
        
        keyboard = [
            [InlineKeyboardButton("🔐 Login", callback_data='login')],
            [
                InlineKeyboardButton("1 Day Key 📅", callback_data='key_1day'),
                InlineKeyboardButton("1 Week Key 📅", callback_data='key_1week')
            ],
            [
                InlineKeyboardButton("1 Month Key 📅", callback_data='key_1month'),
                InlineKeyboardButton("3 Month Key 📅", callback_data='key_3months')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        if update.message:
            update.message.reply_text(help_text, reply_markup=reply_markup, parse_mode='Markdown')
        elif update.callback_query:
            update.callback_query.message.reply_text(help_text, reply_markup=reply_markup, parse_mode='Markdown')
    
    def status(self, update, context):
        """Check login status with buttons"""
        from telegram import InlineKeyboardButton, InlineKeyboardMarkup
        
        if self.logged_in and self.session:
            status_text = "✅ Bot logged in hai aur ready hai!"
            keyboard = [
                [
                    InlineKeyboardButton("1 Day Key 📅", callback_data='key_1day'),
                    InlineKeyboardButton("1 Week Key 📅", callback_data='key_1week')
                ],
                [
                    InlineKeyboardButton("1 Month Key 📅", callback_data='key_1month'),
                    InlineKeyboardButton("3 Month Key 📅", callback_data='key_3months')
                ]
            ]
        else:
            status_text = "❌ Bot logged in nahi hai. Login button dabayein."
            keyboard = [
                [InlineKeyboardButton("🔐 Login Now", callback_data='login')]
            ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        if update.message:
            update.message.reply_text(status_text, reply_markup=reply_markup)
        elif update.callback_query:
            update.callback_query.message.reply_text(status_text, reply_markup=reply_markup)
    
    def button_callback(self, update, context):
        """Handle button clicks"""
        query = update.callback_query
        query.answer()
        
        callback_data = query.data
        
        if callback_data == 'login':
            self.login_action(query, context)
        elif callback_data == 'status':
            self.status_action(query, context)
        elif callback_data == 'help':
            self.help_action(query, context)
        elif callback_data.startswith('key_'):
            duration = callback_data.replace('key_', '')
            self.generate_key_action(query, context, duration)
    
    def login_action(self, query, context):
        """Login action from button"""
        query.message.reply_text("🔄 FIREx mein login ho raha hai...")
        
        try:
            self.session = requests.Session()
            
            # Improved headers to avoid 403 error
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Cache-Control': 'max-age=0',
                'DNT': '1',
                'Referer': 'https://vipowner.online/'
            }
            
            self.session.headers.update(headers)
            
            # First visit the main page to get cookies
            try:
                logger.info("🔄 Visiting main page first...")
                main_page = self.session.get("https://vipowner.online/FIREx/", timeout=30)
                time.sleep(2)
                logger.info(f"Main page status: {main_page.status_code}")
            except Exception as e:
                logger.warning(f"Main page visit failed: {e}")
            
            # Get credentials from environment variables (REQUIRED)
            username = os.getenv('FIREX_USERNAME')
            password = os.getenv('FIREX_PASSWORD')
            
            if not username or not password:
                logger.error("❌ FIREX_USERNAME and FIREX_PASSWORD must be set!")
                query.message.reply_text("❌ Bot credentials not configured. Please contact admin.")
                return
            
            login_data = {
                'username': username,
                'password': password
            }
            
            login_url = "https://vipowner.online/FIREx/login"
            
            # Update Content-Type for POST request
            self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded'
            
            logger.info(f"🔄 Attempting login to {login_url}")
            response = self.session.post(
                login_url, 
                data=login_data, 
                allow_redirects=True,
                timeout=30
            )
            
            logger.info(f"Login response status: {response.status_code}")
            logger.info(f"Response URL: {response.url}")
            
            if response.status_code == 200:
                if "logout" in response.text.lower() or "dashboard" in response.text.lower() or "generate" in response.text.lower():
                    self.logged_in = True
                    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
                    
                    keyboard = [
                        [
                            InlineKeyboardButton("1 Day Key 📅", callback_data='key_1day'),
                            InlineKeyboardButton("1 Week Key 📅", callback_data='key_1week')
                        ],
                        [
                            InlineKeyboardButton("1 Month Key 📅", callback_data='key_1month'),
                            InlineKeyboardButton("3 Month Key 📅", callback_data='key_3months')
                        ]
                    ]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    
                    query.message.reply_text("✅ Login successful! Ab key generate kar sakte hain:", reply_markup=reply_markup)
                    logger.info("✅ FIREx login successful")
                else:
                    query.message.reply_text("❌ Login failed. Please check credentials or website might be blocking.")
                    logger.error(f"Login failed - Response preview: {response.text[:200]}")
            elif response.status_code == 403:
                query.message.reply_text("❌ 403 Error: Website ne access block kar diya. Retry kar rahe hain...")
                logger.error("403 Forbidden - Website blocking the request")
            else:
                query.message.reply_text(f"❌ Login failed. HTTP Status: {response.status_code}")
                logger.error(f"Login failed with status {response.status_code}")
                
        except Exception as e:
            query.message.reply_text(f"❌ Login error: {str(e)}")
            logger.error(f"Login exception: {e}")
    
    def login(self, update, context):
        """Login command handler"""
        update.message.reply_text("🔄 FIREx mein login ho raha hai...")
        
        try:
            self.session = requests.Session()
            
            # Improved headers to avoid 403 error
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Cache-Control': 'max-age=0',
                'DNT': '1',
                'Referer': 'https://vipowner.online/'
            }
            
            self.session.headers.update(headers)
            
            # First visit the main page to get cookies
            try:
                logger.info("🔄 Visiting main page first...")
                main_page = self.session.get("https://vipowner.online/FIREx/", timeout=30)
                time.sleep(2)
                logger.info(f"Main page status: {main_page.status_code}")
            except Exception as e:
                logger.warning(f"Main page visit failed: {e}")
            
            # Get credentials from environment variables (REQUIRED)
            username = os.getenv('FIREX_USERNAME')
            password = os.getenv('FIREX_PASSWORD')
            
            if not username or not password:
                logger.error("❌ FIREX_USERNAME and FIREX_PASSWORD must be set!")
                if update.message:
                    update.message.reply_text("❌ Bot credentials not configured. Please contact admin.")
                elif hasattr(update, 'callback_query') and update.callback_query:
                    update.callback_query.message.reply_text("❌ Bot credentials not configured. Please contact admin.")
                return
            
            login_data = {
                'username': username,
                'password': password
            }
            
            login_url = "https://vipowner.online/FIREx/login"
            
            # Update Content-Type for POST request
            self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded'
            
            logger.info(f"🔄 Attempting login to {login_url}")
            response = self.session.post(
                login_url, 
                data=login_data, 
                allow_redirects=True,
                timeout=30
            )
            
            logger.info(f"Login response status: {response.status_code}")
            logger.info(f"Response URL: {response.url}")
            
            if response.status_code == 200:
                if "logout" in response.text.lower() or "dashboard" in response.text.lower() or "generate" in response.text.lower():
                    self.logged_in = True
                    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
                    
                    keyboard = [
                        [
                            InlineKeyboardButton("1 Day Key 📅", callback_data='key_1day'),
                            InlineKeyboardButton("1 Week Key 📅", callback_data='key_1week')
                        ],
                        [
                            InlineKeyboardButton("1 Month Key 📅", callback_data='key_1month'),
                            InlineKeyboardButton("3 Month Key 📅", callback_data='key_3months')
                        ]
                    ]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    
                    update.message.reply_text("✅ Login successful! Ab key generate kar sakte hain:", reply_markup=reply_markup)
                    logger.info("✅ FIREx login successful")
                else:
                    update.message.reply_text("❌ Login failed. Please check credentials or website might be blocking.")
                    logger.error(f"Login failed - Response preview: {response.text[:200]}")
            elif response.status_code == 403:
                update.message.reply_text("❌ 403 Error: Website ne access block kar diya. Retry kar rahe hain...")
                logger.error("403 Forbidden - Website blocking the request")
            else:
                update.message.reply_text(f"❌ Login failed. HTTP Status: {response.status_code}")
                logger.error(f"Login failed with status {response.status_code}")
                
        except Exception as e:
            update.message.reply_text(f"❌ Login error: {str(e)}")
            logger.error(f"Login exception: {e}")
    
    def status_action(self, query, context):
        """Status action from button"""
        update_obj = type('obj', (object,), {
            'callback_query': query,
            'message': None
        })()
        self.status(update_obj, context)
    
    def help_action(self, query, context):
        """Help action from button"""
        update_obj = type('obj', (object,), {
            'callback_query': query,
            'message': None
        })()
        self.help_command(update_obj, context)
    
    def generate_key_action(self, query, context, duration):
        """Generate key from button click"""
        if not self.logged_in or not self.session:
            from telegram import InlineKeyboardButton, InlineKeyboardMarkup
            
            keyboard = [[InlineKeyboardButton("🔐 Login Now", callback_data='login')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            query.message.reply_text("❌ Pehle login karein:", reply_markup=reply_markup)
            return
        
        query.message.reply_text(f"🔄 {duration} key generate ho rahi hai...")
        
        try:
            key_url = "https://vipowner.online/FIREx/keys/generate"
            key_data = {'duration': duration}
            
            response = self.session.post(key_url, data=key_data, timeout=30)
            
            logger.info(f"Key generation response status: {response.status_code}")
            
            if response.status_code == 200:
                generated_key = self._extract_key_from_response(response)
                
                if generated_key:
                    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
                    
                    message = f"""
🎉 **Key Successfully Generated!**

🔑 **Key:** `{generated_key}`
⏰ **Duration:** {duration}

✅ **Enjoy!**
                    """
                    
                    keyboard = [
                        [
                            InlineKeyboardButton("1 Day Key 📅", callback_data='key_1day'),
                            InlineKeyboardButton("1 Week Key 📅", callback_data='key_1week')
                        ],
                        [
                            InlineKeyboardButton("1 Month Key 📅", callback_data='key_1month'),
                            InlineKeyboardButton("3 Month Key 📅", callback_data='key_3months')
                        ]
                    ]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    
                    query.message.reply_text(message, parse_mode='Markdown', reply_markup=reply_markup)
                    logger.info(f"✅ Key generated: {duration}")
                else:
                    query.message.reply_text("⚠️ Key generate hui lekin extract nahi ho payi. Response check kar rahe hain...")
                    logger.warning(f"Key extraction failed. Response preview: {response.text[:300]}")
            else:
                query.message.reply_text(f"❌ Key generation failed. Status: {response.status_code}")
                logger.error(f"Key generation failed with status {response.status_code}")
                
        except Exception as e:
            query.message.reply_text(f"❌ Error: {str(e)}")
            logger.error(f"Key generation exception: {e}")
    
    def get_key(self, update, context):
        """Generate key with specified duration (command handler)"""
        from telegram import InlineKeyboardButton, InlineKeyboardMarkup
        
        if not self.logged_in or not self.session:
            keyboard = [[InlineKeyboardButton("🔐 Login Now", callback_data='login')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text("❌ Pehle login karein:", reply_markup=reply_markup)
            return
        
        duration_map = {
            '1day': '1day',
            '1week': '1week', 
            '1month': '1month',
            '3months': '3months'
        }
        
        duration = "1day"
        
        if context.args:
            duration_arg = context.args[0].lower()
            duration = duration_map.get(duration_arg, "1day")
        
        update.message.reply_text(f"🔄 {duration} key generate ho rahi hai...")
        
        try:
            key_url = "https://vipowner.online/FIREx/keys/generate"
            key_data = {'duration': duration}
            
            response = self.session.post(key_url, data=key_data, timeout=30)
            
            logger.info(f"Key generation response status: {response.status_code}")
            
            if response.status_code == 200:
                generated_key = self._extract_key_from_response(response)
                
                if generated_key:
                    message = f"""
🎉 **Key Successfully Generated!**

🔑 **Key:** `{generated_key}`
⏰ **Duration:** {duration}

✅ **Enjoy!**
                    """
                    
                    keyboard = [
                        [
                            InlineKeyboardButton("1 Day Key 📅", callback_data='key_1day'),
                            InlineKeyboardButton("1 Week Key 📅", callback_data='key_1week')
                        ],
                        [
                            InlineKeyboardButton("1 Month Key 📅", callback_data='key_1month'),
                            InlineKeyboardButton("3 Month Key 📅", callback_data='key_3months')
                        ]
                    ]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    
                    update.message.reply_text(message, parse_mode='Markdown', reply_markup=reply_markup)
                    logger.info(f"✅ Key generated: {duration}")
                else:
                    update.message.reply_text("⚠️ Key generate hui lekin extract nahi ho payi. Response check kar rahe hain...")
                    logger.warning(f"Key extraction failed. Response preview: {response.text[:300]}")
            else:
                update.message.reply_text(f"❌ Key generation failed. Status: {response.status_code}")
                logger.error(f"Key generation failed with status {response.status_code}")
                
        except Exception as e:
            update.message.reply_text(f"❌ Error: {str(e)}")
            logger.error(f"Key generation exception: {e}")
    
    def _extract_key_from_response(self, response):
        """Extract key from response"""
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Input fields check
            input_fields = soup.find_all('input', {'type': 'text'})
            for field in input_fields:
                value = field.get('value', '').strip()
                if value and len(value) >= 8:
                    return value
            
            # Code blocks check
            code_elements = soup.find_all(['code', 'pre'])
            for element in code_elements:
                text = element.get_text().strip()
                if text and len(text) >= 8:
                    return text
            
            # Regex patterns
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
    
    def run_polling(self):
        """Start bot with polling"""
        try:
            if self.setup_bot():
                logger.info("🤖 Starting bot polling...")
                self.updater.start_polling()
                logger.info("✅ Bot polling started successfully!")
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
        logger.info("🚀 Starting bot in background...")
        firex_bot.run_polling()
    except Exception as e:
        logger.error(f"❌ Background bot error: {e}")

# Start bot when app starts (in both Replit and Render environments)
if os.getenv('BOT_TOKEN'):
    logger.info("🎯 Starting bot in background thread...")
    bot_thread = threading.Thread(target=start_bot_background)
    bot_thread.daemon = True
    bot_thread.start()
else:
    logger.warning("⚠️ BOT_TOKEN not set - Bot will not start!")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"🌐 Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port)
