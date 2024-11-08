# BOT for Last War (do First Lady)

## Requirements

1. Set display resolution of emulator (MEmu for example) to: **1280x720** (tablet)
2. Set the language game to **French** (it will be change in the futurue)
3. Works perfectly with Windows11 **BUT** if you use MacOS or Linux, the installation will be different, watch out

## Installations

1. Install the programming language [Python](https://www.python.org/downloads/),
2. Open the terminal command in administrator mode and write:
   1. **pip install pyautogui**
   2. **pip install pillow**
   3. **pip install opencv-python**
   4. **pip install pytesseract** (https://www.youtube.com/watch?v=HNCypVfeTdw)
   5. **pip install Unidecode**

## Before Starting the bot

1. (if you want to ban some player/alliance) You can give a nickname to some players as you want in Last war. Do it before set player's name in the blacklist.
2. (if you want to ban some player/alliance) You can set player name in the blacklist array in the constants.py file (BANNED_PLAYERS_AND_ALLIANCES)
3. In game:
   1. click on your profile
   2. click on #serverNumber
   3. open capitole buffs interface

## Start bot

1. Don't do anything while script is running.
2. To stop the script, set the mouse on the corner of the screen (top right for example) for the **"fail-safe"**.
3. Start the script: **python startBot.py**
