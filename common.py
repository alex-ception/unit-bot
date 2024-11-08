import pyautogui as pg
import time
import pytesseract
from typing import Literal
from constants import *
import unidecode

Secretary = Literal["strategy", "security", "development", "science", "interior"]

#-------------------------------------------------------------

def IsBlank (myString):
    return not (myString and myString.strip())

#-------------------------------------------------------------

def GetPosition():
  print(pg.position())

#-------------------------------------------------------------

def CloseModal():
  try:
    closeModal = pg.locateCenterOnScreen("./images/close-modal-button.png", grayscale=True, confidence=0.8)
    pg.click(closeModal[0], closeModal[1])

    time.sleep(1)
  except pg.ImageNotFoundException: 
    print('Close modal button not found')

#-------------------------------------------------------------

def OpenWaitingList():
  try:
    waitingList = pg.locateCenterOnScreen("./images/waiting-list-button.png", grayscale=True, confidence=0.8)
    pg.click(waitingList[0], waitingList[1])

    time.sleep(1)
  except pg.ImageNotFoundException: 
    print('Waiting list button not found')

#-------------------------------------------------------------

def OpenSecretary(x, y):
  try:
    # Scroll down to see all secretaries
    pg.scroll(-200)
    time.sleep(1)

    pg.moveTo(x, y)
    pg.click()

    time.sleep(1)
  except: 
    print('Not able to open the secretary modal')

#-------------------------------------------------------------

def GetFirstPlayerNameInTheList():
  try:
    playerNameImage = pg.screenshot(region=(LIST_BUFF_TOP_LEFT_X, LIST_BUFF_TOP_LEFT_Y, LIST_BUFF_CENTER_X - LIST_BUFF_TOP_LEFT_X, LIST_BUFF_CENTER_Y - LIST_BUFF_TOP_LEFT_Y))

    playerName = pytesseract.image_to_string(playerNameImage)

    playerNameWithoutAccent = unidecode.unidecode(playerName)

    return playerNameWithoutAccent
  except: 
    print('Not able to get player name')
    
#-------------------------------------------------------------

def isPlayerBanned(playerName: str):
  isBanned = False

  for name in BANNED_PLAYERS_AND_ALLIANCES:
    if name.lower() in playerName.lower():
      isBanned=True
      print("BANNED !")
    else:
      print("Not banned")

  return isBanned

#-------------------------------------------------------------

def CheckIfPlayerCanEnterInBuffList():
  playerName = GetFirstPlayerNameInTheList()

  print(playerName)

  if IsBlank(playerName):
    return
  else:
    isBanned = isPlayerBanned(playerName)

    if isBanned:
      print("Gonna click on deny")
      return DenyPlayerInWaitingList()
    else:
      print("Gonna click on accept")
      return AcceptPlayerInWaitingList()

#-------------------------------------------------------------

def AcceptPlayerInWaitingList():
  try:
    accepteEntryButton = pg.locateCenterOnScreen(
      "./images/accept-entry-button.png", 
      region=(LIST_BUFF_TOP_LEFT_X, LIST_BUFF_TOP_LEFT_Y, LIST_BUFF_BOTTOM_RIGHT_X - LIST_BUFF_TOP_LEFT_X, LIST_BUFF_BOTTOM_RIGHT_Y - LIST_BUFF_TOP_LEFT_Y), 
      grayscale=True, 
      confidence=0.8)
    
    pg.click(accepteEntryButton[0], accepteEntryButton[1])

  except pg.ImageNotFoundException:
    print('Accept entry image not found')

#-------------------------------------------------------------

def DenyPlayerInWaitingList():
  try:
    denyEntryButton = pg.locateCenterOnScreen(
      "./images/deny-entry-button.png", 
      region=(LIST_BUFF_TOP_LEFT_X, LIST_BUFF_TOP_LEFT_Y, LIST_BUFF_BOTTOM_RIGHT_X - LIST_BUFF_TOP_LEFT_X, LIST_BUFF_BOTTOM_RIGHT_Y - LIST_BUFF_TOP_LEFT_Y), 
      grayscale=True, 
      confidence=0.8)
        
    pg.click(denyEntryButton[0], denyEntryButton[1])

    time.sleep(1)

    ConfirmDenyPlayerInWaitingList()

  except pg.ImageNotFoundException:
    print('Deny entry image not found')

#-------------------------------------------------------------

def ConfirmDenyPlayerInWaitingList():
  try:
    confirmDenyPlayerInWaitingListButton = pg.locateCenterOnScreen(
      "./images/confirm-deny-entry-button.png",
      grayscale=True, 
      confidence=0.6)
    
    pg.click(confirmDenyPlayerInWaitingListButton[0], confirmDenyPlayerInWaitingListButton[1])

    time.sleep(1)
    
  except pg.ImageNotFoundException:
    print('Confirm Deny player from buff image not found')

#-------------------------------------------------------------

def CheckTimeInTheBuff():
  try:
    timeInTheBuffImage = pg.screenshot(region=(TIME_IN_THE_BUFF_TOP_LEFT_X, TIME_IN_THE_BUFF_TOP_LEFT_Y, TIME_IN_THE_BUFF_BOTTOM_RIGHT_X - TIME_IN_THE_BUFF_TOP_LEFT_X, TIME_IN_THE_BUFF_BOTTOM_RIGHT_Y - TIME_IN_THE_BUFF_TOP_LEFT_Y))

    timeInTheBuffFullSentence = pytesseract.image_to_string(timeInTheBuffImage)

    timeInTheBuffLastElement = timeInTheBuffFullSentence.split(' ')[3].replace(" ", "")

    splitLastElement = list(timeInTheBuffLastElement)

    hours = splitLastElement[6] + splitLastElement[7]
    minutes = splitLastElement[9] + splitLastElement[10]

    if int(hours[0]) > 0 or int(hours[1]) > 0 or int(minutes[0]) > 0:
      EjectPlayerFromBuff()

  except:
    print('Not able to get time in the buff')

#-------------------------------------------------------------

def EjectPlayerFromBuff():
  try:
    ejectPlayerFromBuffButton = pg.locateCenterOnScreen(
      "./images/eject-player-from-buff.png",
      grayscale=True, 
      confidence=0.8)
    
    pg.click(ejectPlayerFromBuffButton[0], ejectPlayerFromBuffButton[1])

    time.sleep(1)

    ConfirmEjectPlayerFromBuff()

  except pg.ImageNotFoundException:
    print('Eject player from buff image not found')

#-------------------------------------------------------------

def ConfirmEjectPlayerFromBuff():
  try:
    confirmEjectPlayerFromBuffButton = pg.locateCenterOnScreen(
      "./images/confirm-eject-player-button.png",
      grayscale=True, 
      confidence=0.6)
    
    pg.click(confirmEjectPlayerFromBuffButton[0], confirmEjectPlayerFromBuffButton[1])

    time.sleep(1)

  except pg.ImageNotFoundException:
    print('Confirm Eject player from buff image not found')