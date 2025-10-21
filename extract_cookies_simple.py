#!/usr/bin/env python3
"""
Simple Cookie Extractor - Network Tab Method
100% Working for HttpOnly cookies
"""

import pickle

print("\n" + "="*70)
print("🍪 Simple Cookie Extractor - Network Tab Method")
print("="*70 + "\n")

print("📋 INSTRUCTIONS:")
print("-" * 70)
print("1. Browser mein https://vipowner.online/FIREx/ kholo")
print("2. Apne credentials se LOGIN karo (ishashwat / 844121)")
print("3. Login successful hone ke baad:")
print()
print("   ➡️  F12 dabao (Developer Tools)")
print("   ➡️  'Application' tab pe jao (Chrome)")
print("       Ya 'Storage' tab (Firefox)")
print()
print("   ➡️  Left side mein 'Cookies' expand karo")
print("   ➡️  'https://vipowner.online' select karo")
print()
print("4. Cookies dikhenge table mein. Sabse important cookies:")
print("   - ci_session")
print("   - csrf_cookie_name")
print("   - cf_clearance (agar hai)")
print()
print("5. Har cookie ka NAME aur VALUE copy karo\n")
print("="*70 + "\n")

# Collect cookies
cookies = {}

print("Cookies enter karo (har line: name=value)")
print("Enter karne ke baad 'done' type karo\n")

while True:
    line = input("Cookie (name=value) ya 'done': ").strip()
    
    if line.lower() == 'done':
        break
    
    if '=' in line:
        name, value = line.split('=', 1)
        cookies[name.strip()] = value.strip()
        print(f"  ✅ Added: {name.strip()}")
    else:
        print("  ⚠️  Invalid format. Use: name=value")

if not cookies:
    print("\n❌ No cookies added!")
    exit(1)

print(f"\n✅ Total cookies: {len(cookies)}")

# Create session data
session_data = {
    'cookies': cookies,
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://vipowner.online/FIREx/'
    },
    'username': 'ishashwat',
    'method': 'network_tab_manual'
}

# Save session
SESSION_FILE = 'firex_session.pkl'
with open(SESSION_FILE, 'wb') as f:
    pickle.dump(session_data, f)

print("\n" + "="*70)
print("✅ SESSION SAVED SUCCESSFULLY!")
print("="*70)
print(f"📁 File: {SESSION_FILE}")
print(f"🍪 Cookies saved:")
for name in cookies.keys():
    print(f"   - {name}")

print("\n🚀 Ab bot chalao: python app.py")
print("="*70 + "\n")
