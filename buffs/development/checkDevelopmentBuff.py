from common import *
from constants import *

def CheckDevelopmentBuff():
  OpenSecretary(DEVELOPMENT_BUFF_CENTER_X, DEVELOPMENT_BUFF_CENTER_Y)

  OpenWaitingList()

  CheckIfPlayerCanEnterInBuffList()

  # Close List
  CloseModal()

  CheckTimeInTheBuff()

  # Close waiting list
  CloseModal()