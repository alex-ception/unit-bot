import time
from common import *
from constants import *
from buffs.checkBuffs import CheckBuffs
from antiBotModal import CheckAndCloseAntiBotModal
from likedProfileModal import CheckLikedProfileModal
from multiprocessing import Process

#-------------------------------------------------------------

def StartBot():
  # To have time to change window from VSCode to emulator
  time.sleep(GetRandomClickInterval())

  CheckBuffs()

#-------------------------------------------------------------

# Start 3 loops. 
# 1 to close the modal when someone like your profile (CheckLikedProfileModal) 
# 1 to close anti bot modal (CheckAndCloseAntiBotModal) 
# 1 for main bot (StartBot)
if __name__ == '__main__':
  Process(target=CheckLikedProfileModal).start()
  Process(target=CheckAndCloseAntiBotModal).start()
  Process(target=StartBot).start()