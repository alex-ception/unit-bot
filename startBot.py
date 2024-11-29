import time
from common import *
from constants import *
from buffs.checkBuffs import CheckBuffs
from antiBotModal import CheckAntiBotModal
from multiprocessing import Process


def StartBot():
  # To have time to change window from VSCode to emulator
  time.sleep(GetRandomClickInterval())

  # Don't call this function "CloseBuyKimPack" if you already bought Kim
  # CloseBuyKimPack()

  # GoToProfile()

  # OpenCapitol()

  CheckBuffs()

# Start 2 loops. 1 for main bot and 1 to close anti bot modal
if __name__ == '__main__':
  Process(target=StartBot).start()
  Process(target=CheckAntiBotModal).start()