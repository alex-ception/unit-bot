import pyautogui as pg
import time
import json
import random
from typing import Literal

def open_secretary(secretary):
  try:
    secretary_button = pg.locateCenterOnScreen('./images/buff/'+secretary+'.png')
    pg.moveTo(secretary_button.x, secretary_button.y)
    pg.click()

    random_click_sleep()
  except:
    print(f'Not able to open the {secretary} secretary modal')

def open_waiting_list():
  try:
    waiting_list = pg.locateCenterOnScreen('./images/waiting-list-button.png', confidence=0.8)
    pg.click(waiting_list[0], waiting_list[1])

    random_click_sleep()
  except pg.ImageNotFoundException:
    print('Waiting list button not found')

def accept_applies(secretary):
  try:
    pg.scroll(50)
    time.sleep(1)
    applies = pg.locateAllOnScreen('./images/accept-entry-button.png', confidence=0.9)
    for applicant in applies:
      accept_applicants = len(list(applies))
      center = pg.center(applicant)
      pg.moveTo(center.x, center.y)
      while accept_applicants >= 0:
        pg.click()
        accept_applicants -= 1
        random_click_sleep()
      return
  except Exception as e:
    print(f'No one in {secretary} secretary list to approve')

def close_modal():
  try:
    close_button = pg.locateCenterOnScreen("./images/close-modal-button.png", confidence=0.8)
    pg.click(close_button[0], close_button[1])

    random_click_sleep()
  except pg.ImageNotFoundException:
    print('Close modal button NOT FOUND')

def random_sleep(min = 30, max = 60):
  sleep_time = round(random.uniform(min,max))
  print(f'Sleeping for {sleep_time} seconds...')
  time.sleep(sleep_time)

def random_click_sleep():
  time.sleep(get_random_click_interval())

def get_random_click_interval():
    with open('./config.json') as config_file:
      json_config = json.load(config_file)

      min_interval = float(json_config['click_interval_in_second']['min'])
      max_interval = float(json_config['click_interval_in_second']['max'])

      return random.uniform(min_interval, max_interval)
