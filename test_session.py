import pickle
import requests

# Load session
with open('firex_session.pkl', 'rb') as f:
    session_data = pickle.load(f)

# Create session
session = requests.Session()

# Set cookies
for name, value in session_data['cookies'].items():
    session.cookies.set(name, value)

# Set headers
session.headers.update(session_data['headers'])

# Test session
print("🧪 Testing session...")
try:
    response = session.get("https://vipowner.online/FIREx/", timeout=10)
    print(f"📊 Status: {response.status_code}")
    
    if response.status_code == 200:
        if "logout" in response.text.lower() or "dashboard" in response.text.lower() or "keys" in response.text.lower():
            print("✅ SESSION IS VALID!")
            print("🎉 Bot ab is session se keys generate kar sakta hai!")
        else:
            print("⚠️  Response received but validation unclear")
    else:
        print(f"⚠️  Unexpected status: {response.status_code}")
        
except Exception as e:
    print(f"❌ Test failed: {e}")
