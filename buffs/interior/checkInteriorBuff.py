from common import *
from constants import *

def CheckInteriorBuff():
  OpenSecretary(INTERIOR_BUFF_CENTER_X, INTERIOR_BUFF_CENTER_Y)

  OpenWaitingList()

  CheckIfPlayerCanEnterInBuffList()

  # Close List
  CloseModal()

  CheckTimeInTheBuff()

  # Close waiting list
  CloseModal()