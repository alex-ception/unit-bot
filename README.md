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
   4. **pip install pytesseract** More complicated so check this video (https://www.youtube.com/watch?v=HNCypVfeTdw)

## Before Starting the bot

1. (if you want to ban some alliance) You can set the alliance's name in **blacklist_alliances** in the **config.json** file (ex: CyS)
2. (if you want to ban some player) You can give a nickname to some players as you want in Last war. Do it before set player's name in **blacklist_players** in the **in config.json** file (ex: YolKal).
3. Be the first lady
4. In game:
   1. click on your profile
   2. click on #serverNumber
   3. open capitole buffs interface
   4. Scroll down to the bottom (not needed in the future)

## Start bot

1. Don't do anything while script is running.
2. To stop the script, set your mouse on the corner of the screen (top right for example) for the **"fail-safe"**.
3. Start the script: **python startBot.py**
