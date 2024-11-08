import time
from common import *
from constants import *
from buffs.strategy.checkStrategyBuff import CheckStrategyBuff
from buffs.security.checkSecurityBuff import CheckSecurityBuff
from buffs.development.checkDevelopmentBuff import CheckDevelopmentBuff
from buffs.science.checkScienceBuff import CheckScienceBuff
from buffs.interior.checkInteriorBuff import CheckInteriorBuff


# To have time to change the window
time.sleep(2)

# Start script
while True:
  CheckStrategyBuff()

  CheckSecurityBuff()

  CheckDevelopmentBuff()

  CheckScienceBuff()

  CheckInteriorBuff()
