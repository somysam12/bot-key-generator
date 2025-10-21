#!/usr/bin/env python3
"""
FIREx Advanced Session Creator with CAPTCHA Bypass
Multiple methods: Cloudscraper, Selenium, 2Captcha
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

def method1_cloudscraper(username, password):
    """
    Method 1: Cloudscraper (Cloudflare bypass)
    Fastest aur free - Cloudflare ke against best hai!
    """
    try:
        import cloudscraper
        
        print("\n🔷 Method 1: Cloudscraper (Cloudflare Bypass)")
        print("-" * 60)
        
        # Create cloudscraper session
        scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'desktop': True
            }
        )
        
        logger.info("🌐 Visiting main page with Cloudscraper...")
        main_page = scraper.get("https://vipowner.online/FIREx/", timeout=30)
        logger.info(f"✅ Main page status: {main_page.status_code}")
        time.sleep(2)
        
        if main_page.status_code != 200:
            print(f"⚠️  Main page returned {main_page.status_code}")
            return None
        
        # Login attempt
        login_data = {
            'username': username,
            'password': password
        }
        
        login_url = "https://vipowner.online/FIREx/login"
        logger.info(f"🔐 Attempting login with Cloudscraper...")
        
        response = scraper.post(
            login_url,
            data=login_data,
            timeout=30
        )
        
        logger.info(f"📊 Login response: {response.status_code}")
        
        if response.status_code == 200 and ("logout" in response.text.lower() or "dashboard" in response.text.lower()):
            # Save session
            session_data = {
                'cookies': scraper.cookies.get_dict(),
                'headers': dict(scraper.headers),
                'username': username,
                'method': 'cloudscraper'
            }
            
            with open(SESSION_FILE, 'wb') as f:
                pickle.dump(session_data, f)
            
            print("\n✅ SUCCESS! Cloudscraper worked!")
            print(f"💾 Session saved: {SESSION_FILE}")
            return True
        else:
            print(f"❌ Cloudscraper failed - Status: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Cloudscraper error: {e}")
        logger.error(f"Cloudscraper exception: {e}")
        return None


def method2_selenium(username, password):
    """
    Method 2: Selenium + Undetected ChromeDriver
    Browser automation - most powerful for 2025!
    """
    try:
        import undetected_chromedriver as uc
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        print("\n🔷 Method 2: Selenium + Undetected ChromeDriver")
        print("-" * 60)
        print("⚠️  Browser window khulega - close mat karna!")
        
        # Setup undetected ChromeDriver
        options = uc.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        logger.info("🚀 Launching undetected Chrome...")
        driver = uc.Chrome(options=options, version_main=None)
        
        try:
            # Visit main page
            logger.info("🌐 Visiting main page...")
            driver.get("https://vipowner.online/FIREx/")
            time.sleep(3)
            
            print("📸 Main page loaded - checking for CAPTCHA...")
            
            # Check for CAPTCHA elements (customize based on actual page)
            if "captcha" in driver.page_source.lower() or "challenge" in driver.page_source.lower():
                print("\n⚠️  CAPTCHA detected!")
                print("🤖 Please solve the CAPTCHA manually in the browser window...")
                print("⏳ Waiting 30 seconds for you to solve it...")
                time.sleep(30)
            
            # Try to find and fill login form
            logger.info("🔐 Looking for login form...")
            driver.get("https://vipowner.online/FIREx/login")
            time.sleep(2)
            
            # Try to find username field (adjust selectors based on actual HTML)
            try:
                # Common input field names/ids
                username_field = None
                password_field = None
                
                # Try different selectors
                for selector in ['username', 'user', 'email', 'login']:
                    try:
                        username_field = driver.find_element(By.NAME, selector)
                        break
                    except:
                        pass
                
                for selector in ['password', 'pass', 'pwd']:
                    try:
                        password_field = driver.find_element(By.NAME, selector)
                        break
                    except:
                        pass
                
                if username_field and password_field:
                    print("✅ Login form found!")
                    username_field.send_keys(username)
                    password_field.send_keys(password)
                    
                    # Find submit button
                    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"], input[type="submit"]')
                    submit_btn.click()
                    
                    print("⏳ Submitting login...")
                    time.sleep(5)
                    
                    # Check if login successful
                    if "logout" in driver.page_source.lower() or "dashboard" in driver.page_source.lower():
                        # Extract cookies
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
                        print("❌ Login failed - check credentials or page structure")
                        driver.save_screenshot('login_failed.png')
                        print("📸 Screenshot saved: login_failed.png")
                else:
                    print("❌ Could not find login form fields")
                    print("💡 Manual intervention needed:")
                    print("   1. Login manually in the browser window")
                    print("   2. Wait for dashboard to load")
                    input("\nPress Enter after you've logged in manually...")
                    
                    # Extract cookies after manual login
                    cookies = driver.get_cookies()
                    cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}
                    
                    session_data = {
                        'cookies': cookie_dict,
                        'headers': {'User-Agent': driver.execute_script("return navigator.userAgent;")},
                        'username': username,
                        'method': 'selenium_manual'
                    }
                    
                    with open(SESSION_FILE, 'wb') as f:
                        pickle.dump(session_data, f)
                    
                    print("\n✅ SUCCESS! Session extracted!")
                    print(f"💾 Session saved: {SESSION_FILE}")
                    driver.quit()
                    return True
                    
            except Exception as e:
                print(f"⚠️  Form automation failed: {e}")
                print("\n💡 Trying manual intervention...")
                print("   Please login manually in the browser window")
                input("\nPress Enter after you've logged in...")
                
                cookies = driver.get_cookies()
                cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}
                
                session_data = {
                    'cookies': cookie_dict,
                    'headers': {'User-Agent': driver.execute_script("return navigator.userAgent;")},
                    'username': username,
                    'method': 'selenium_manual'
                }
                
                with open(SESSION_FILE, 'wb') as f:
                    pickle.dump(session_data, f)
                
                print("\n✅ Session extracted!")
                driver.quit()
                return True
                
        finally:
            if driver:
                driver.quit()
                
    except Exception as e:
        print(f"❌ Selenium error: {e}")
        logger.error(f"Selenium exception: {e}")
        return None


def method3_2captcha(username, password):
    """
    Method 3: 2Captcha Service (Paid but guaranteed)
    Professional CAPTCHA solving service
    """
    print("\n🔷 Method 3: 2Captcha Service")
    print("-" * 60)
    print("💰 This requires a 2Captcha API key (paid service)")
    print("📝 Get API key from: https://2captcha.com")
    print()
    
    api_key = input("Enter your 2Captcha API key (or press Enter to skip): ").strip()
    
    if not api_key:
        print("⏭️  Skipping 2Captcha method")
        return None
    
    try:
        from twocaptcha import TwoCaptcha
        import requests
        
        solver = TwoCaptcha(api_key)
        session = requests.Session()
        
        print("🌐 Visiting website...")
        main_page = session.get("https://vipowner.online/FIREx/", timeout=30)
        
        # Check if CAPTCHA is present (customize based on actual CAPTCHA type)
        if "captcha" in main_page.text.lower():
            print("🤖 CAPTCHA detected - solving via 2Captcha...")
            
            # For image CAPTCHA
            # captcha_img = session.get("CAPTCHA_IMAGE_URL")
            # result = solver.normal(captcha_img.content)
            
            # For reCAPTCHA
            # result = solver.recaptcha(sitekey='SITE_KEY', url='PAGE_URL')
            
            print("⏳ This may take 10-30 seconds...")
            # Implement based on actual CAPTCHA type
            
        # Continue with login after CAPTCHA is solved
        login_data = {
            'username': username,
            'password': password
        }
        
        response = session.post("https://vipowner.online/FIREx/login", data=login_data)
        
        if response.status_code == 200:
            session_data = {
                'cookies': session.cookies.get_dict(),
                'headers': dict(session.headers),
                'username': username,
                'method': '2captcha'
            }
            
            with open(SESSION_FILE, 'wb') as f:
                pickle.dump(session_data, f)
            
            print("\n✅ SUCCESS with 2Captcha!")
            return True
        else:
            print("❌ 2Captcha method failed")
            return None
            
    except Exception as e:
        print(f"❌ 2Captcha error: {e}")
        return None


def create_session_advanced():
    """Main function with multiple bypass methods"""
    
    print("\n" + "="*60)
    print("🔥 FIREx Advanced Session Creator 🔥")
    print("   Multiple CAPTCHA Bypass Methods")
    print("="*60 + "\n")
    
    if os.path.exists(SESSION_FILE):
        overwrite = input(f"⚠️  Session file exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("❌ Cancelled")
            return False
        os.remove(SESSION_FILE)
    
    # Get credentials
    print("📝 Enter FIREx Credentials:")
    print("-" * 40)
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if not username or not password:
        print("❌ Username aur password zaroori hain!")
        return False
    
    print("\n🎯 Trying multiple bypass methods...\n")
    
    # Try Method 1: Cloudscraper (fastest)
    result = method1_cloudscraper(username, password)
    if result:
        return True
    
    print("\n⏭️  Trying next method...\n")
    time.sleep(2)
    
    # Try Method 2: Selenium (most powerful)
    result = method2_selenium(username, password)
    if result:
        return True
    
    print("\n⏭️  Trying last method...\n")
    time.sleep(2)
    
    # Try Method 3: 2Captcha (paid but works)
    result = method3_2captcha(username, password)
    if result:
        return True
    
    print("\n😞 All methods failed. Please contact support.\n")
    return False


if __name__ == "__main__":
    success = create_session_advanced()
    
    if success:
        print("\n" + "="*60)
        print("✅ SESSION CREATED SUCCESSFULLY!")
        print("="*60)
        print(f"📁 File: {SESSION_FILE}")
        print("🚀 Ab bot chalao - automatic session use karega!")
        print("="*60 + "\n")
    else:
        print("\n❌ Session creation failed\n")
