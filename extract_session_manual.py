#!/usr/bin/env python3
"""
FIREx Manual Session Extractor
100% Working - Manual login, automatic cookie extraction!
"""

import pickle
import requests

SESSION_FILE = 'firex_session.pkl'

def extract_session_from_cookies():
    """
    Manual session extraction - 100% working method!
    """
    
    print("\n" + "="*60)
    print("🔥 FIREx Manual Session Extractor 🔥")
    print("   100% Working Method!")
    print("="*60 + "\n")
    
    print("📋 Instructions:")
    print("-" * 60)
    print("1. Browser mein https://vipowner.online/FIREx/ kholo")
    print("2. Apne credentials se login karo")
    print("3. Login successful hone ke baad:")
    print("   - Press F12 (Developer Tools khulenge)")
    print("   - 'Console' tab pe jao")
    print("   - Ye command paste karo aur Enter dabao:")
    print()
    print("   document.cookie")
    print()
    print("4. Sab cookies copy karo (quotes ke beech wala text)")
    print("5. Yaha paste karo\n")
    print("="*60 + "\n")
    
    cookies_string = input("Cookies paste karo (ya 'help' type karo instructions ke liye): ").strip()
    
    if cookies_string.lower() == 'help':
        print("\n📖 Detailed Instructions:")
        print("-" * 60)
        print("Step 1: Browser kholo (Chrome/Firefox recommended)")
        print("Step 2: https://vipowner.online/FIREx/ pe jao")
        print("Step 3: Apne username/password se login karo")
        print("Step 4: F12 dabao (Developer Tools)")
        print("Step 5: Console tab select karo")
        print("Step 6: Type karo: document.cookie")
        print("Step 7: Output copy karo (quotes ke beech ka)")
        print("Step 8: Yaha paste karo\n")
        
        cookies_string = input("\nCookies paste karo: ").strip()
    
    if not cookies_string:
        print("❌ Cookies empty hain!")
        return False
    
    # Parse cookies
    cookie_dict = {}
    
    # Handle different formats
    if ';' in cookies_string:
        # Format: name1=value1; name2=value2
        pairs = cookies_string.split(';')
        for pair in pairs:
            pair = pair.strip()
            if '=' in pair:
                name, value = pair.split('=', 1)
                cookie_dict[name.strip()] = value.strip()
    else:
        print("⚠️  Cookie format incorrect. Expected format: name1=value1; name2=value2")
        return False
    
    if not cookie_dict:
        print("❌ Could not parse cookies!")
        return False
    
    print(f"\n✅ Found {len(cookie_dict)} cookies!")
    
    # Get username
    username = input("\nEnter your FIREx username (for reference): ").strip()
    
    # Create session data
    session_data = {
        'cookies': cookie_dict,
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        },
        'username': username or 'manual_user',
        'method': 'manual_extraction'
    }
    
    # Save session
    with open(SESSION_FILE, 'wb') as f:
        pickle.dump(session_data, f)
    
    print("\n" + "="*60)
    print("✅ SESSION SAVED SUCCESSFULLY!")
    print("="*60)
    print(f"📁 File: {SESSION_FILE}")
    print(f"🍪 Cookies: {len(cookie_dict)}")
    print("\n🎯 Testing session...")
    
    # Test session
    session = requests.Session()
    for name, value in cookie_dict.items():
        session.cookies.set(name, value)
    
    session.headers.update(session_data['headers'])
    
    try:
        test_response = session.get("https://vipowner.online/FIREx/", timeout=10)
        
        if test_response.status_code == 200:
            if "logout" in test_response.text.lower() or "dashboard" in test_response.text.lower():
                print("✅ Session is VALID!")
                print("🚀 Bot ab is session ko use karega!")
            else:
                print("⚠️  Session saved but validation unclear")
                print("   Bot ko chalao aur test karo")
        else:
            print(f"⚠️  Test returned status: {test_response.status_code}")
            print("   Session saved hai, bot ko try karo")
            
    except Exception as e:
        print(f"⚠️  Test failed: {e}")
        print("   But session saved hai - bot try karo!")
    
    print("="*60 + "\n")
    return True


def extract_session_from_browser_export():
    """
    Alternative: Import from browser extension (EditThisCookie format)
    """
    
    print("\n🔷 Alternative Method: Browser Extension")
    print("-" * 60)
    print("1. Install 'EditThisCookie' extension in Chrome")
    print("2. Login to https://vipowner.online/FIREx/")
    print("3. Click EditThisCookie icon")
    print("4. Click 'Export' button")
    print("5. Paste JSON here\n")
    
    import json
    
    json_input = input("Paste exported cookies JSON (or 'skip' to use manual method): ").strip()
    
    if json_input.lower() == 'skip' or not json_input:
        return extract_session_from_cookies()
    
    try:
        cookies_list = json.loads(json_input)
        
        cookie_dict = {}
        for cookie in cookies_list:
            if 'name' in cookie and 'value' in cookie:
                cookie_dict[cookie['name']] = cookie['value']
        
        if not cookie_dict:
            print("❌ No valid cookies found in JSON!")
            return False
        
        print(f"✅ Imported {len(cookie_dict)} cookies!")
        
        username = input("Enter your FIREx username: ").strip()
        
        session_data = {
            'cookies': cookie_dict,
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            },
            'username': username or 'manual_user',
            'method': 'browser_export'
        }
        
        with open(SESSION_FILE, 'wb') as f:
            pickle.dump(session_data, f)
        
        print("\n✅ SESSION SAVED!")
        print(f"📁 File: {SESSION_FILE}\n")
        return True
        
    except json.JSONDecodeError:
        print("❌ Invalid JSON format!")
        return False


if __name__ == "__main__":
    print("\n🔥 Choose extraction method:")
    print("1. Manual Cookie Extraction (Recommended)")
    print("2. Browser Extension Export (Alternative)")
    
    choice = input("\nChoice (1/2): ").strip()
    
    if choice == '2':
        success = extract_session_from_browser_export()
    else:
        success = extract_session_from_cookies()
    
    if success:
        print("🎉 Session ready! Ab bot chalao!\n")
    else:
        print("❌ Session extraction failed. Try again!\n")
