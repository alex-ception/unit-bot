from common import *
from constants import *

def CheckSecurityBuff():
  OpenSecretary(SECURITY_BUFF_CENTER_X, SECURITY_BUFF_CENTER_Y)

  OpenWaitingList()

  CheckIfPlayerCanEnterInBuffList()

  # Close List
  CloseModal()

  CheckTimeInTheBuff()

  # Close waiting list
  CloseModal()