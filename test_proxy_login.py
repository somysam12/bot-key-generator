#!/usr/bin/env python3
"""
Test FIREx Login with FREE Proxies
Quick test to see if proxy bypasses 403
"""

import os
from proxy_helper import get_proxy_manager
import requests
import time

def test_login_with_proxy():
    """Test login using free proxies"""
    
    print("\n" + "="*60)
    print("🔥 Testing FIREx Login with FREE Proxies")
    print("="*60 + "\n")
    
    # Get credentials
    username = os.getenv('FIREX_USERNAME', 'ishashwat')
    password = os.getenv('FIREX_PASSWORD', '844121')
    
    print(f"📝 Username: {username}")
    print(f"🔐 Password: {password[:3]}***\n")
    
    # Initialize proxy manager
    print("🌐 Initializing proxy manager...")
    proxy_mgr = get_proxy_manager()
    
    # Get working proxies
    print("🔍 Finding working proxies (this may take 30-60 seconds)...\n")
    working_proxies = proxy_mgr.get_working_proxies(max_test=30)
    
    if not working_proxies:
        print("❌ No working proxies found!")
        print("💡 Try again or use local setup instead.\n")
        return False
    
    print(f"\n✅ Found {len(working_proxies)} working proxies!")
    print("-" * 60)
    
    # Try login with each proxy
    for i, proxy in enumerate(working_proxies[:5], 1):
        print(f"\n🔄 Attempt {i}/{min(5, len(working_proxies))}")
        print(f"🌐 Proxy: {proxy}")
        
        try:
            session = requests.Session()
            
            # Headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
            }
            
            session.headers.update(headers)
            
            proxy_dict = {
                'http': f'http://{proxy}',
                'https': f'http://{proxy}'
            }
            
            # Visit main page
            print("   📄 Visiting main page...")
            main_response = session.get(
                "https://vipowner.online/FIREx/",
                proxies=proxy_dict,
                timeout=15
            )
            
            print(f"   📊 Main page: {main_response.status_code}")
            
            if main_response.status_code == 403:
                print("   ❌ Still 403 - proxy might be blacklisted too")
                continue
            
            time.sleep(2)
            
            # Try login
            print("   🔐 Attempting login...")
            login_data = {
                'username': username,
                'password': password
            }
            
            login_response = session.post(
                "https://vipowner.online/FIREx/login",
                data=login_data,
                proxies=proxy_dict,
                timeout=15,
                allow_redirects=True
            )
            
            print(f"   📊 Login response: {login_response.status_code}")
            
            if login_response.status_code == 200:
                # Check if login successful
                if "logout" in login_response.text.lower() or "dashboard" in login_response.text.lower():
                    print("\n" + "="*60)
                    print("✅ SUCCESS! LOGIN WORKED WITH PROXY!")
                    print("="*60)
                    print(f"🌐 Working Proxy: {proxy}")
                    print(f"📊 Status: {login_response.status_code}")
                    print("\n💾 You can now integrate this into the bot!")
                    print("="*60 + "\n")
                    return True
                else:
                    print("   ⚠️  200 but no success indicators")
            else:
                print(f"   ❌ Failed with status: {login_response.status_code}")
                
        except requests.exceptions.Timeout:
            print("   ⏱️  Timeout - proxy too slow")
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:50]}")
        
        time.sleep(1)
    
    print("\n" + "="*60)
    print("😞 All proxy attempts failed")
    print("="*60)
    print("\n💡 Options:")
    print("1. Try again (proxies change frequently)")
    print("2. Use PAID proxy service ($5-10/month)")
    print("3. Run bot LOCALLY on your computer (100% works!)")
    print("="*60 + "\n")
    
    return False


if __name__ == "__main__":
    success = test_proxy_login()
    
    if not success:
        print("\n📖 LOCAL SETUP GUIDE:")
        print("-" * 60)
        print("Apne computer pe bot chalane ke liye:")
        print()
        print("1. Python install karo (python.org)")
        print("2. Code download karo")
        print("3. Install packages:")
        print("   pip install python-telegram-bot requests beautifulsoup4")
        print()
        print("4. Environment variables set karo:")
        print("   Windows: set BOT_TOKEN=your_token")
        print("   Linux/Mac: export BOT_TOKEN=your_token")
        print()
        print("5. Bot chalao: python app.py")
        print()
        print("✅ Your home IP not blacklisted = Will work!")
        print("-" * 60 + "\n")
