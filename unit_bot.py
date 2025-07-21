import time
from common import *
from buffs.check_buffs import check_buffs
from antiBotModal import CheckAndCloseAntiBotModal
from likedProfileModal import CheckLikedProfileModal
from multiprocessing import Process

def unit_bot():
  random_click_sleep()
  check_buffs()

# Start 3 loops.
# 1 to close the modal when someone like your profile (CheckLikedProfileModal) 
# 1 to close anti bot modal (CheckAndCloseAntiBotModal) 
# 1 for main bot (StartBot)
if __name__ == '__main__':
  #Process(target=CheckLikedProfileModal).start()
  #Process(target=CheckAndCloseAntiBotModal).start()
  #Process(target=StartBot).start()
  unit_bot()