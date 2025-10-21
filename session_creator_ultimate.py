#!/usr/bin/env python3
"""
FIREx Ultimate Session Creator (2025)
TLS Fingerprint Bypass + Multiple Methods
"""

import os
import time
import pickle
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

SESSION_FILE = 'firex_session.pkl'


def method1_curl_cffi(username, password):
    """
    Method 1: curl-cffi (Best for 2025!)
    Browser TLS fingerprint mimicking - 403 bypass ke liye best!
    """
    try:
        from curl_cffi import requests as curl_requests
        
        print("\n🔷 Method 1: curl-cffi (TLS Fingerprint Bypass)")
        print("   Latest 2025 technique - Browser TLS mimicking!")
        print("-" * 60)
        
        # Chrome 120 TLS fingerprint use karenge
        logger.info("🌐 Visiting main page with Chrome TLS fingerprint...")
        
        response = curl_requests.get(
            "https://vipowner.online/FIREx/",
            impersonate="chrome120",
            timeout=30
        )
        
        logger.info(f"✅ Main page status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"⚠️  Main page returned {response.status_code}")
            # Even if 403, let's try login
        
        time.sleep(2)
        
        # Login attempt with browser TLS
        login_data = {
            'username': username,
            'password': password
        }
        
        login_url = "https://vipowner.online/FIREx/login"
        logger.info(f"🔐 Attempting login with Chrome TLS fingerprint...")
        
        # Create session
        session = curl_requests.Session()
        
        # First get the page to establish session
        session.get("https://vipowner.online/FIREx/", impersonate="chrome120", timeout=30)
        time.sleep(1)
        
        # Now login
        login_response = session.post(
            login_url,
            data=login_data,
            impersonate="chrome120",
            timeout=30,
            allow_redirects=True
        )
        
        logger.info(f"📊 Login response: {login_response.status_code}")
        logger.info(f"📍 Final URL: {login_response.url}")
        
        # Check response
        if login_response.status_code == 200:
            response_text = login_response.text.lower()
            
            if "logout" in response_text or "dashboard" in response_text or "generate" in response_text:
                # Extract cookies
                cookies = {}
                if hasattr(session, 'cookies'):
                    cookies = dict(session.cookies)
                
                session_data = {
                    'cookies': cookies,
                    'headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                    },
                    'username': username,
                    'method': 'curl_cffi'
                }
                
                with open(SESSION_FILE, 'wb') as f:
                    pickle.dump(session_data, f)
                
                print("\n✅ SUCCESS! curl-cffi worked!")
                print("   TLS fingerprint bypass successful!")
                print(f"💾 Session saved: {SESSION_FILE}")
                return True
            else:
                print(f"❌ Login failed - No success indicators found")
                print(f"📄 Response preview: {login_response.text[:200]}")
                return None
        else:
            print(f"❌ curl-cffi failed - Status: {login_response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ curl-cffi error: {e}")
        logger.error(f"curl-cffi exception: {e}")
        return None


def method2_selenium_fixed(username, password):
    """
    Method 2: Selenium with proper Chromium setup
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        import undetected_chromedriver as uc
        
        print("\n🔷 Method 2: Selenium (Fixed for Replit)")
        print("-" * 60)
        
        # Option A: Try undetected-chromedriver with explicit binary
        try:
            print("🚀 Trying undetected ChromeDriver...")
            
            options = uc.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--headless=new')
            
            # Set chromium binary path for Replit
            options.binary_location = '/nix/store/qa9cnw4v5xkxyip6mb9kxqfq1z4x2dx1-chromium-138.0.7204.100/bin/chromium'
            
            driver = uc.Chrome(
                options=options,
                driver_executable_path='/nix/store/8zj50jw4w0hby47167kqqsaqw4mm5bkd-chromedriver-unwrapped-138.0.7204.100/bin/chromedriver',
                version_main=None,
                use_subprocess=False
            )
            
        except Exception as e:
            print(f"⚠️  Undetected Chrome failed: {e}")
            print("🔄 Trying regular Selenium...")
            
            # Option B: Regular Selenium
            options = Options()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--headless=new')
            options.add_argument('--disable-blink-features=AutomationControlled')
            
            # Find chromium binary
            import subprocess
            chromium_result = subprocess.run(['which', 'chromium'], capture_output=True, text=True)
            if chromium_result.returncode == 0:
                options.binary_location = chromium_result.stdout.strip()
            
            driver = webdriver.Chrome(options=options)
        
        try:
            logger.info("🌐 Navigating to FIREx...")
            driver.get("https://vipowner.online/FIREx/")
            time.sleep(3)
            
            print(f"📊 Page loaded - Status: {driver.title}")
            
            # Try login page
            driver.get("https://vipowner.online/FIREx/login")
            time.sleep(2)
            
            # Try to find and fill form
            try:
                # Look for common form fields
                username_selectors = [
                    (By.NAME, 'username'),
                    (By.NAME, 'user'),
                    (By.ID, 'username'),
                    (By.ID, 'user'),
                    (By.CSS_SELECTOR, 'input[type="text"]'),
                ]
                
                password_selectors = [
                    (By.NAME, 'password'),
                    (By.NAME, 'pass'),
                    (By.ID, 'password'),
                    (By.CSS_SELECTOR, 'input[type="password"]'),
                ]
                
                username_field = None
                password_field = None
                
                for by, selector in username_selectors:
                    try:
                        username_field = driver.find_element(by, selector)
                        break
                    except:
                        continue
                
                for by, selector in password_selectors:
                    try:
                        password_field = driver.find_element(by, selector)
                        break
                    except:
                        continue
                
                if username_field and password_field:
                    print("✅ Login form found!")
                    username_field.send_keys(username)
                    password_field.send_keys(password)
                    
                    # Submit
                    submit_selectors = [
                        (By.CSS_SELECTOR, 'button[type="submit"]'),
                        (By.CSS_SELECTOR, 'input[type="submit"]'),
                        (By.CSS_SELECTOR, 'button'),
                    ]
                    
                    for by, selector in submit_selectors:
                        try:
                            submit_btn = driver.find_element(by, selector)
                            submit_btn.click()
                            break
                        except:
                            continue
                    
                    print("⏳ Waiting for response...")
                    time.sleep(5)
                    
                    # Check success
                    page_source = driver.page_source.lower()
                    if "logout" in page_source or "dashboard" in page_source:
                        cookies = driver.get_cookies()
                        cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}
                        
                        session_data = {
                            'cookies': cookie_dict,
                            'headers': {'User-Agent': driver.execute_script("return navigator.userAgent;")},
                            'username': username,
                            'method': 'selenium'
                        }
                        
                        with open(SESSION_FILE, 'wb') as f:
                            pickle.dump(session_data, f)
                        
                        print("\n✅ SUCCESS! Selenium worked!")
                        print(f"💾 Session saved: {SESSION_FILE}")
                        driver.quit()
                        return True
                    
                else:
                    print("❌ Login form not found in page")
                    driver.save_screenshot('page.png')
                    print("📸 Screenshot saved: page.png")
                    
            except Exception as form_error:
                print(f"⚠️  Form error: {form_error}")
            
            driver.quit()
            return None
            
        except Exception as nav_error:
            print(f"❌ Navigation error: {nav_error}")
            if driver:
                driver.quit()
            return None
            
    except Exception as e:
        print(f"❌ Selenium error: {e}")
        logger.error(f"Selenium exception: {e}")
        return None


def create_session_ultimate():
    """Ultimate session creator with best 2025 methods"""
    
    print("\n" + "="*60)
    print("🔥 FIREx ULTIMATE Session Creator (2025) 🔥")
    print("   TLS Fingerprint + Advanced Bypass")
    print("="*60 + "\n")
    
    if os.path.exists(SESSION_FILE):
        overwrite = input(f"⚠️  Session exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("❌ Cancelled")
            return False
        os.remove(SESSION_FILE)
    
    print("📝 Enter FIREx Credentials:")
    print("-" * 40)
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if not username or not password:
        print("❌ Credentials required!")
        return False
    
    print("\n🎯 Trying advanced bypass methods...\n")
    
    # Method 1: curl-cffi (Best for 2025 - TLS fingerprint bypass)
    result = method1_curl_cffi(username, password)
    if result:
        return True
    
    print("\n⏭️  Trying Selenium method...\n")
    time.sleep(2)
    
    # Method 2: Selenium with proper setup
    result = method2_selenium_fixed(username, password)
    if result:
        return True
    
    print("\n😞 Both advanced methods failed.")
    print("\n💡 Possible solutions:")
    print("   1. Website might have strong anti-bot protection")
    print("   2. Try using a VPN or different IP")
    print("   3. Check if credentials are correct")
    print("   4. Website structure might have changed\n")
    
    return False


if __name__ == "__main__":
    success = create_session_ultimate()
    
    if success:
        print("\n" + "="*60)
        print("✅ SESSION CREATED SUCCESSFULLY!")
        print("="*60)
        print(f"📁 File: {SESSION_FILE}")
        print("🚀 Bot ab automatic session use karega!")
        print("💪 Same IP se hamesha login karega!")
        print("="*60 + "\n")
    else:
        print("\n❌ Session creation failed\n")
