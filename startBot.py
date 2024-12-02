import time
from common import *
from constants import *
from buffs.checkBuffs import CheckBuffs
from antiBotModal import CheckAndCloseAntiBotModal
from goToTheBuffsPage import CheckAndGoToTheBuffsPage
from multiprocessing import Process

#-------------------------------------------------------------

def StartBot():
  # To have time to change window from VSCode to emulator
  time.sleep(GetRandomClickInterval())

  CheckBuffs()

#-------------------------------------------------------------

# Start 3 loops. 
# 1 for main bot (StartBot)
# 1 to close anti bot modal (CheckAndCloseAntiBotModal) 
# 1 to comeback to the buffs section in case of reboot (CheckAndGoToTheBuffsPage)
if __name__ == '__main__':
  Process(target=CheckAndCloseAntiBotModal).start()
  Process(target=CheckAndGoToTheBuffsPage).start()
  Process(target=StartBot).start()