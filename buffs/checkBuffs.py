import pyautogui as pg
import time
from buffs.strategy.checkStrategyBuff import CheckStrategyBuff
from buffs.security.checkSecurityBuff import CheckSecurityBuff
from buffs.development.checkDevelopmentBuff import CheckDevelopmentBuff
from buffs.science.checkScienceBuff import CheckScienceBuff
from buffs.interior.checkInteriorBuff import CheckInteriorBuff

def CheckBuffs():
  # Scroll down to see all secretaries
  pg.click(733, 128) # Top left on the window
  pg.scroll(-400)
  time.sleep(2)

  while True:
    CheckStrategyBuff()

    CheckSecurityBuff()

    CheckDevelopmentBuff()

    CheckScienceBuff()

    CheckInteriorBuff()
