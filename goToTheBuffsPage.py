import pyautogui as pg
import time
from constants import *

#-------------------------------------------------------------

def GetKimPackModal():
  try:
    return pg.locateCenterOnScreen("./images/kim-pack.png", grayscale=True, confidence=0.6)
   
  except pg.ImageNotFoundException: 
    None

#-------------------------------------------------------------

def CloseKimPack():
  try:
    closeButtonCoords = pg.locateCenterOnScreen("./images/kim-pack-close-button.png", grayscale=True, confidence=0.8)
    pg.click(closeButtonCoords[0], closeButtonCoords[1])

    time.sleep(0.3)

  except pg.ImageNotFoundException: 
    print('Kim pack close button not found')

#-------------------------------------------------------------

def GetLikedButton():
  try:
    return pg.locateCenterOnScreen("./images/liked-button.png", grayscale=True, confidence=0.8)
  
  except pg.ImageNotFoundException:
    None

#-------------------------------------------------------------

def GoToProfile():
  pg.click(PROFILE_PICTURE_X, PROFILE_PICTURE_Y)

  time.sleep(0.3)

  likedButton = GetLikedButton()

  if likedButton is not None:
    # If profile liked, click on the liked button to close the modal
    pg.click(likedButton[0], likedButton[1])

#-------------------------------------------------------------

def OpenCapitol():
  try:
    capitolIcon = pg.locateCenterOnScreen("./images/capitol-icon.png", grayscale=True, confidence=0.6)
    pg.click(capitolIcon[0], capitolIcon[1])

    time.sleep(0.3)

  except pg.ImageNotFoundException:
    print('Open capitol image not found')

#-------------------------------------------------------------

def CheckAndGoToTheBuffsPage():
  while True:
    kimPackModal = GetKimPackModal()

    if kimPackModal is not None:
      print('Go to the buffs page !!!!!!!!!!!!!')

      CloseKimPack() 
      GoToProfile()
      OpenCapitol()