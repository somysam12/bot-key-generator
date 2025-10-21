#!/usr/bin/env python3
"""
FIREx Session Creator (Pyrogram style)
Ek baar ye script chalaiye, credentials enter kijiye, aur session ban jayega!
"""

import requests
import pickle
import os
import time
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

SESSION_FILE = 'firex_session.pkl'

def create_session():
    """FIREx website pe login karke session banao (Pyrogram jaisa)"""
    
    print("\n" + "="*60)
    print("🔥 FIREx Session Creator (Pyrogram Style) 🔥")
    print("="*60 + "\n")
    
    if os.path.exists(SESSION_FILE):
        overwrite = input(f"⚠️  Session file already exists ({SESSION_FILE}). Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("❌ Cancelled. Existing session kept.")
            return False
        os.remove(SESSION_FILE)
        print("🗑️  Old session deleted.\n")
    
    # User se credentials lo
    print("📝 Enter FIREx Website Credentials:")
    print("-" * 40)
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if not username or not password:
        print("❌ Username aur password dono zaroori hain!")
        return False
    
    print("\n🔄 FIREx website pe login ho raha hai...\n")
    
    try:
        session = requests.Session()
        
        # Browser jaisa headers (403 error avoid karne ke liye)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
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
        
        session.headers.update(headers)
        
        # Step 1: Pehle main page pe jao (cookies lene ke liye)
        logger.info("🌐 Visiting main page...")
        main_page = session.get("https://vipowner.online/FIREx/", timeout=30)
        logger.info(f"✅ Main page loaded: {main_page.status_code}")
        time.sleep(2)
        
        # Step 2: Login karo
        login_data = {
            'username': username,
            'password': password
        }
        
        login_url = "https://vipowner.online/FIREx/login"
        session.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        
        logger.info(f"🔐 Attempting login to {login_url}...")
        response = session.post(
            login_url, 
            data=login_data, 
            allow_redirects=True,
            timeout=30
        )
        
        logger.info(f"📊 Login response status: {response.status_code}")
        logger.info(f"📍 Response URL: {response.url}")
        
        # Step 3: Check karo login successful hua ya nahi
        if response.status_code == 200:
            if "logout" in response.text.lower() or "dashboard" in response.text.lower() or "generate" in response.text.lower():
                
                # Session save karo (Pyrogram jaisa)
                session_data = {
                    'cookies': session.cookies.get_dict(),
                    'headers': dict(session.headers),
                    'username': username  # Reference ke liye
                }
                
                with open(SESSION_FILE, 'wb') as f:
                    pickle.dump(session_data, f)
                
                print("\n" + "="*60)
                print("✅ LOGIN SUCCESSFUL!")
                print("="*60)
                print(f"💾 Session saved to: {SESSION_FILE}")
                print(f"👤 Logged in as: {username}")
                print("\n🎉 Ab aap bot chala sakte hain!")
                print("   Bot automatically is session ko use karega.\n")
                print("📝 Bot chalane ke liye:")
                print("   python app.py")
                print("="*60 + "\n")
                
                logger.info("✅ Session successfully created and saved!")
                return True
                
            else:
                print("\n❌ Login failed!")
                print("⚠️  Possible reasons:")
                print("   1. Wrong username/password")
                print("   2. Website structure changed")
                print("   3. Website blocking requests")
                logger.error(f"Login failed - Response preview: {response.text[:300]}")
                return False
                
        elif response.status_code == 403:
            print("\n❌ 403 Forbidden Error")
            print("⚠️  Website ne request block kar di. Reasons:")
            print("   1. Too many login attempts")
            print("   2. IP blocked")
            print("   3. Captcha required")
            logger.error("403 Forbidden - Website blocking the request")
            return False
            
        else:
            print(f"\n❌ Login failed with HTTP status: {response.status_code}")
            logger.error(f"Unexpected status code: {response.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        print("\n❌ Connection timeout! Website respond nahi kar rahi.")
        logger.error("Connection timeout")
        return False
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Connection error! Internet check karo.")
        logger.error("Connection error")
        return False
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        logger.error(f"Exception during session creation: {e}")
        return False

if __name__ == "__main__":
    success = create_session()
    
    if success:
        print("🚀 Ready to go! Bot ab is session se login karega.\n")
    else:
        print("\n😞 Session creation failed. Please try again.\n")
