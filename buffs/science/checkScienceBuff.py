from common import *
from constants import *

def CheckScienceBuff():
  OpenSecretary(SCIENCE_BUFF_CENTER_X, SCIENCE_BUFF_CENTER_Y)

  OpenWaitingList()

  CheckIfPlayerCanEnterInBuffList()

  # Close List
  CloseModal()

  CheckTimeInTheBuff()

  # Close waiting list
  CloseModal()