# BOT for Last War (do First Lady)

## Requirements

1. Set display resolution of emulator (MEmu for example) to: **1280x720** (tablet)
2. Set the language game to **French** (because screenshots are in the french language)
3. Works perfectly with Windows11 **BUT** if you use MacOS or Linux, the installation will be different, watch out

## Installations

1. Install the programming language [Python](https://www.python.org/downloads/),
2. Open the terminal command in administrator mode and write:
   1. pip install pyautogui
   2. pip install pillow
   3. pip install opencv-python
   4. now install tesseract/pytesseract. More complicated so check this video (https://www.youtube.com/watch?v=HNCypVfeTdw)

## Before Starting the bot

1. (if you want to ban some alliance) You can set the alliance's name in **blacklist_alliances** in the **config.json** file (ex: CyS)
2. (if you want to ban some player) You can give a nickname to some players as you want in Last war. Do it before set player's name in **blacklist_players** in the **in config.json** file (ex: YolKal).
3. Be the first lady
4. In game:
   1. click on your profile
   2. click on #serverNumber
   3. open capitole buffs interface

## Start bot

1. Don't do anything while script is running.
2. To stop the script, set your mouse on the corner of the screen (top right for example) for the **"fail-safe"**.
3. Open new terminal with administrator rights
4. Start the script: **python startBot.py**

## How to update the bot ?

There's many ways to do that:

- Either by me, so you just have to update the main branch: **git pull**
- Or by youself but I promise it's not so tricky :D
  - Just **make new screenshots** for update images in the images folder (Last war can update UI buttons)
  - Your screen resolution changed so the script can't click on the right regions so it's faster to **update pixel variables** by yourself directly (remove loop in startBot.py and just call GetPosition(). Then start the script with **Python startBot.py** and set your mouse wherever your want, you gonna have the X and Y positions)

## Is it work perfectly ?

No, the bot can make mistakes because it uses OCR techniques and these techniques are not 100% reliable (especially tesseract).
