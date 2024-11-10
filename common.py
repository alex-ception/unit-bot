import pyautogui as pg
import pytesseract
import time
import unidecode
import json
import random
from constants import *
from typing import Literal

Secretary = Literal["strategy", "security", "development", "science", "interior"]

#-------------------------------------------------------------

def GetRandomClickInterval():
    with open('./config.json') as config_file:
      jsonConfig = json.load(config_file)

      minInterval = int(jsonConfig['click_interval_in_second']['min'])
      maxInterval = int(jsonConfig['click_interval_in_second']['max'])

      return random.uniform(minInterval, maxInterval)

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

    time.sleep(GetRandomClickInterval())
  except pg.ImageNotFoundException: 
    print('Close modal button not found')

#-------------------------------------------------------------

def OpenWaitingList():
  try:
    waitingList = pg.locateCenterOnScreen("./images/waiting-list-button.png", grayscale=True, confidence=0.8)
    pg.click(waitingList[0], waitingList[1])

    time.sleep(GetRandomClickInterval())
  except pg.ImageNotFoundException: 
    print('Waiting list button not found')

#-------------------------------------------------------------

def OpenSecretary(x, y):
  try:
    # Scroll down to see all secretaries
    pg.scroll(-200)
    time.sleep(GetRandomClickInterval())

    pg.moveTo(x, y)
    pg.click()

    time.sleep(GetRandomClickInterval())
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

def isPlayerBanned(playerNameWithAlliance: str):
  with open('./config.json') as config_file:
    jsonConfig = json.load(config_file)

    playerNameWithoutSpaces = playerNameWithAlliance.strip()

    bracketIndex = playerNameWithoutSpaces.find("[")

    print("bracketIndex=", bracketIndex)

    playerAlliance = playerNameWithoutSpaces[bracketIndex+1 : bracketIndex+4]
    playerName = playerNameWithoutSpaces[bracketIndex+6 : ]

    print("playerAlliance=", playerAlliance)
    print("playerName=", playerName)

    isBanned = False

    for alliance in jsonConfig['blacklist_alliances']:
      if alliance.lower() in playerAlliance.lower():
        isBanned=True

    for player in jsonConfig['blacklist_players']:
      if player.lower() in playerName.lower():
        isBanned=True
        
    return isBanned

#-------------------------------------------------------------

def CheckIfPlayerCanEnterInBuffList():
  playerName = GetFirstPlayerNameInTheList()

  print(playerName)

  if IsBlank(playerName):
    return
  else:
    isBanned = isPlayerBanned(playerName)

    print("isPlayerBanned = ",isBanned)

    if isBanned:
      print("Gonna click on deny")
      DenyPlayerInWaitingList()
    else:
      print("Gonna click on accept")
      AcceptPlayerInWaitingList()

    time.sleep(GetRandomClickInterval())
    
    CheckIfPlayerCanEnterInBuffList()

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

    time.sleep(GetRandomClickInterval())

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

    time.sleep(GetRandomClickInterval())
    
  except pg.ImageNotFoundException:
    print('Confirm Deny player from buff image not found')

#-------------------------------------------------------------

def CheckTimeInTheBuff():
  try:
    with open('./config.json') as config_file:
      jsonConfig = json.load(config_file)

      timeInTheBuffImage = pg.screenshot(region=(TIME_IN_THE_BUFF_TOP_LEFT_X, TIME_IN_THE_BUFF_TOP_LEFT_Y, TIME_IN_THE_BUFF_BOTTOM_RIGHT_X - TIME_IN_THE_BUFF_TOP_LEFT_X, TIME_IN_THE_BUFF_BOTTOM_RIGHT_Y - TIME_IN_THE_BUFF_TOP_LEFT_Y))

      timeInTheBuffFullSentence = pytesseract.image_to_string(timeInTheBuffImage)

      timeInTheBuffLastElement = timeInTheBuffFullSentence.split(' ')[3].replace(" ", "")

      splitLastElement = list(timeInTheBuffLastElement)

      hours = int(splitLastElement[6] + splitLastElement[7])
      minutes = int(splitLastElement[9] + splitLastElement[10])

      totalMinutes = hours * 60 + minutes
      limitInMinutes = int(jsonConfig['max_time_player_has_buff_in_minute'])

      if totalMinutes >= limitInMinutes:
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

    time.sleep(GetRandomClickInterval())

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

    time.sleep(GetRandomClickInterval())

  except pg.ImageNotFoundException:
    print('Confirm Eject player from buff image not found')