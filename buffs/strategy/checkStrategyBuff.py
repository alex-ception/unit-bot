from common import *
from constants import *

def CheckStrategyBuff():
  OpenSecretary(STRATEGY_BUFF_CENTER_X, STRATEGY_BUFF_CENTER_Y)

  OpenWaitingList()

  CheckIfPlayerCanEnterInBuffList()

  # Close List
  CloseModal()

  CheckTimeInTheBuff()

  # Close waiting list
  CloseModal()