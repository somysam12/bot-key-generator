import pickle

# Cookies from Network tab
cookies_string = "cf_clearance=BlBcHsIzUL7MoDWdCWyOv8MF_xTfpxZs1TTa4Y0XTwE-1755357609-1.2.1.1-EFdwUyuNc0p_KaySC_DUgHkZn77HU2gSzWMpePnqiBvZLtesmk6GvtYbY7HqNMakFPeA4pfaqm_Afc2jkGETMDVmtef6PVkpq43GWaTmnKROIWPSDqqdacRSmuj5quCpjJRXz9p7.vZn0m.7M94Go4Iqpg4q8k3ruDc.1C8z4_.rVT39kl2fdnWJbAU.lkrQRYlqwYmPirvQKbeL9YxFmy4VR.GpX6iTgqyMkGfTBbg; cf_clearance=mRExy04hazUPD6n1QLyrUqrp2b.X98FP0w431LfdJqc-1761052892-1.2.1.1-w9GrRXYWxTXbycAAoGG81YmVvUfVYACZBGveCIO7eDTCXbAGQgVgMEaHX96iMHfVswLh5SdKEjZgpg_F1lSHxxcigykCSELlLZdzaJQx0Bu_MRrZ7KcdAzMBLj5fLdfmzyxRpFivZTGiZrkyvFJm9FJONQnOcbTcIUerzwVhbepKIz5Z8drM0LyWYFUjph4taXirSOSfROcDmzTZc1VdTcZkNbs1WO7RDvwKFKGNsP8; ci_session=b24ad99631fe346a2148a7bf379458c6eccbbd06; csrf_cookie_name=f518bd82cd0e0fb7867fa327e1fbdc71"

# Parse cookies
cookie_dict = {}
for pair in cookies_string.split('; '):
    if '=' in pair:
        name, value = pair.split('=', 1)
        cookie_dict[name.strip()] = value.strip()

# Create session data
session_data = {
    'cookies': cookie_dict,
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    },
    'username': 'ishashwat',
    'method': 'manual_network_tab'
}

# Save session
SESSION_FILE = 'firex_session.pkl'
with open(SESSION_FILE, 'wb') as f:
    pickle.dump(session_data, f)

print(f"✅ Session saved: {SESSION_FILE}")
print(f"🍪 Cookies: {len(cookie_dict)}")
for name in cookie_dict.keys():
    print(f"   - {name}")
