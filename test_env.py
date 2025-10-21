import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Check if variables are loaded
print("=" * 50)
print("Environment Variables Check:")
print("=" * 50)

bot_token = os.getenv('BOT_TOKEN')
username = os.getenv('FIREX_USERNAME')
password = os.getenv('FIREX_PASSWORD')

print(f"BOT_TOKEN exists: {bot_token is not None}")
if bot_token:
    print(f"BOT_TOKEN: {bot_token[:10]}...")
else:
    print("BOT_TOKEN: NOT FOUND")

print(f"\nFIREX_USERNAME exists: {username is not None}")
if username:
    print(f"FIREX_USERNAME: {username}")
else:
    print("FIREX_USERNAME: NOT FOUND")

print(f"\nFIREX_PASSWORD exists: {password is not None}")
if password:
    print(f"FIREX_PASSWORD: {password[:3]}...")
else:
    print("FIREX_PASSWORD: NOT FOUND")

print("\n" + "=" * 50)
print("Current working directory:", os.getcwd())
print("Files in current directory:")
for file in os.listdir('.'):
    if file.startswith('.env'):
        print(f"  ✓ {file}")
print("=" * 50)
