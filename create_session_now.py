#!/usr/bin/env python3
"""
Direct Session Creator - Using your extracted cookies
"""

import pickle

print("\n" + "="*60)
print("🔥 Creating FIREx Session from Your Cookies")
print("="*60 + "\n")

# Your cookies from the export
cookies = {
    'ci_session': '9e65df747c420c65b488a9e700d2fed26d4fcfb4',
    'csrf_cookie_name': 'ee03d4224d2e3db0eba42bbdf3e6e65f',
    'cf_clearance': 'mRExy04hazUPD6n1QLyrUqrp2b.X98FP0w431LfdJqc-1761052892-1.2.1.1-w9GrRXYWxTXbycAAoGG81YmVvUfVYACZBGveCIO7eDTCXbAGQgVgMEaHX96iMHfVswLh5SdKEjZgpg_F1lSHxxcigykCSELlLZdzaJQx0Bu_MRrZ7KcdAzMBLj5fLdfmzyxRpFivZTGiZrkyvFJm9FJONQnOcbTcIUerzwVhbepKIz5Z8drM0LyWYFUjph4taXirSOSfROcDmzTZc1VdTcZkNbs1WO7RDvwKFKGNsP8'
}

# Create session data
session_data = {
    'cookies': cookies,
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Referer': 'https://vipowner.online/FIREx/'
    },
    'username': 'ishashwat',
    'method': 'direct_cookie_import'
}

# Save session
SESSION_FILE = 'firex_session.pkl'
with open(SESSION_FILE, 'wb') as f:
    pickle.dump(session_data, f)

print("✅ SESSION FILE CREATED!")
print("="*60)
print(f"📁 File: {SESSION_FILE}")
print(f"🍪 Cookies imported: {len(cookies)}")
for name in cookies.keys():
    print(f"   ✓ {name}")
print()
print("🚀 Ab bot chalao:")
print("   python app.py")
print()
print("✅ Bot automatically saved session use karega!")
print("="*60 + "\n")
