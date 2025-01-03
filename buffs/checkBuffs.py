import pyautogui as pg
import time
from buffs.strategy.checkStrategyBuff import CheckStrategyBuff
from buffs.security.checkSecurityBuff import CheckSecurityBuff
from buffs.development.checkDevelopmentBuff import CheckDevelopmentBuff
from buffs.science.checkScienceBuff import CheckScienceBuff
from buffs.interior.checkInteriorBuff import CheckInteriorBuff
from constants import STRATEGY_BUFF_CENTER_X

def CheckBuffs():
  # Scroll down to see all secretaries
  pg.mouseDown(STRATEGY_BUFF_CENTER_X, 130, button="left", duration=0.5) 
  pg.moveTo(STRATEGY_BUFF_CENTER_X, -600, duration=1)
  pg.mouseUp(button="left", duration=0.5)

  time.sleep(2)

  while True:
    CheckStrategyBuff()

    CheckSecurityBuff()

    CheckDevelopmentBuff()

    CheckScienceBuff()

    CheckInteriorBuff()
