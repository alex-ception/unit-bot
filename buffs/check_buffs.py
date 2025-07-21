import pyautogui as pg
from common import *

def check_buffs():
  buffs = ['strategy', 'security', 'development', 'science', 'interior']
  while True:
    for buff in buffs:
      print(f'Enter {buff} secretary')
      open_secretary(buff)
      open_waiting_list()
      accept_applies(buff)
      close_modal()
      close_modal()
    random_sleep(5, 15)