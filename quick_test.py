import os

# Directly set environment variables for testing
os.environ['BOT_TOKEN'] = '8398897953:AAGJMUHBFLyUyuTR_8yjfXca5fNDq050RRY'
os.environ['FIREX_USERNAME'] = 'ishashwat'
os.environ['FIREX_PASSWORD'] = '844121'
os.environ['PORT'] = '5000'

# Now run the bot
import app
