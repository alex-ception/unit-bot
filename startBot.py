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

# Start 2 loops. 1 for main bot and 1 to close anti bot modal
if __name__ == '__main__':
  Process(target=CheckAndCloseAntiBotModal).start()
  Process(target=CheckAndGoToTheBuffsPage).start()
  Process(target=StartBot).start()