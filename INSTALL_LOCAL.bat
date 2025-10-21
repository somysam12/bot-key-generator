@echo off
echo ========================================
echo FIREx Bot - ONE-TIME SETUP
echo ========================================
echo.

echo Step 1: Uninstalling wrong version...
pip uninstall python-telegram-bot -y

echo.
echo Step 2: Installing correct packages...
pip install python-telegram-bot==13.15
pip install requests==2.31.0
pip install beautifulsoup4==4.12.2
pip install Flask==2.3.3
pip install python-dotenv==1.0.0

echo.
echo ========================================
echo INSTALLATION COMPLETE!
echo ========================================
echo.
echo Now check your .env file and add:
echo BOT_TOKEN=your_actual_token_here
echo FIREX_USERNAME=ishashwat
echo FIREX_PASSWORD=844121
echo.
echo Then run: run_local.bat
echo.
pause
