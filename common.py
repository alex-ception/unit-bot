import pyautogui as pg
import pytesseract
import time
import json
import random
from datetime import datetime
from constants import *
from typing import Literal

Secretary = Literal["strategy", "security", "development", "science", "interior"]

#-------------------------------------------------------------

def CloseBuyKimPack():
  try:
    crossIcon = pg.locateCenterOnScreen("./images/close-buy-kim-pack.png", grayscale=True, confidence=0.6)
    pg.click(crossIcon[0], crossIcon[1])

    time.sleep(GetRandomClickInterval())
  except pg.ImageNotFoundException:
    print('Close kim pack (cross icon) not found')

#-------------------------------------------------------------

def GoToProfile():
  pg.click(PROFILE_PICTURE_X, PROFILE_PICTURE_Y)

  time.sleep(GetRandomClickInterval())

#-------------------------------------------------------------

def OpenCapitol():
  try:
    capitolIcon = pg.locateCenterOnScreen("./images/capitol-icon.png", grayscale=True, confidence=0.7)
    pg.click(capitolIcon[0], capitolIcon[1])

    time.sleep(GetRandomClickInterval())
  except pg.ImageNotFoundException:
    print('Open capitol image not found')

#-------------------------------------------------------------

def OpenSecretary(x, y):
  try:
    pg.moveTo(x, y)
    pg.click()

    time.sleep(GetRandomClickInterval())
  except: 
    print('Not able to open the secretary modal')

#-------------------------------------------------------------

def OpenWaitingList():
  try:
    waitingList = pg.locateCenterOnScreen("./images/waiting-list-button.png", grayscale=True, confidence=0.8)
    pg.click(waitingList[0], waitingList[1])

    time.sleep(GetRandomClickInterval())
  except pg.ImageNotFoundException: 
    print('Waiting list button not found')

#-------------------------------------------------------------

def GetCoordinatesOfTheFirstPlayerInWaitingList():
  try:
    coords = pg.locateCenterOnScreen(
      "./images/officer-request-title.png",  
      grayscale=True, 
      confidence=0.8)
    
    TOP_LEFT_X = int(coords[0] - 150)
    TOP_LEFT_Y = int(coords[1] + 100)
    BOTTOM_RIGHT_X = int(coords[0] + 230)
    BOTTOM_RIGHT_Y = int(coords[1] + 160)

    return [TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X, BOTTOM_RIGHT_Y]

  except pg.ImageNotFoundException:
    print('Officer request image (main title) not found')

#-------------------------------------------------------------

def GetFirstPlayerNameInTheList():
  try:
    TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X , BOTTOM_RIGHT_Y = GetCoordinatesOfTheFirstPlayerInWaitingList()

    playerNameImage = pg.screenshot(region=(TOP_LEFT_X, TOP_LEFT_Y, (BOTTOM_RIGHT_X - 127) - TOP_LEFT_X, (BOTTOM_RIGHT_Y - 27) - TOP_LEFT_Y))

    playerName = pytesseract.image_to_string(playerNameImage)

    return playerName
  except: 
    print('Not able to get player name')

#-------------------------------------------------------------

def CheckIfPlayerCanEnterInBuffList(previousPlayerName = None):
  playerName = GetFirstPlayerNameInTheList()

  print("playerName=", playerName)

  if (IsBlank(playerName) or previousPlayerName == playerName):
    return
  else:
    isBanned = isPlayerBanned(playerName)

    if isBanned:
      print("Gonna click on deny")
      DenyPlayerInWaitingList()
      WriteLogInBannedPlayersFile(playerName)
    else:
      print("Gonna click on accept")
      AcceptPlayerInWaitingList()

    time.sleep(GetRandomClickInterval())
    
    CheckIfPlayerCanEnterInBuffList(playerName)

#-------------------------------------------------------------

def isPlayerBanned(playerNameWithAlliance: str):
  with open('./config.json') as config_file:
    jsonConfig = json.load(config_file)

    playerNameWithoutSpaces = playerNameWithAlliance.strip()

    bracketIndex = playerNameWithoutSpaces.find("[") # Example: [1Pr] (the first braket)

    isBanned = False

    if bracketIndex == -1:
      # PLAYER DON'T HAVE AN ALLIANCE

      for player in jsonConfig['blacklist_players']:
        if player.lower() in playerNameWithoutSpaces.lower():
          isBanned=True
          
    else:
      # PLAYER HAVE AN ALLIANCE

      playerAlliance = playerNameWithoutSpaces[bracketIndex+1 : bracketIndex+4]
      playerName = playerNameWithoutSpaces[bracketIndex+6 : ]


      for alliance in jsonConfig['blacklist_alliances']:
        if alliance.lower() in playerAlliance.lower():
          isBanned=True

      for player in jsonConfig['blacklist_players']:
        if player.lower() in playerName.lower():
          isBanned=True
      
    return isBanned

#-------------------------------------------------------------

def AcceptPlayerInWaitingList():
  try:
    TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X , BOTTOM_RIGHT_Y = GetCoordinatesOfTheFirstPlayerInWaitingList()

    accepteEntryButton = pg.locateCenterOnScreen(
      "./images/accept-entry-button.png", 
      region=(TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X - TOP_LEFT_X, BOTTOM_RIGHT_Y - TOP_LEFT_Y), 
      grayscale=True, 
      confidence=0.8)
    
    pg.click(accepteEntryButton[0], accepteEntryButton[1])

  except pg.ImageNotFoundException:
    print('Accept entry image not found')

#-------------------------------------------------------------

def DenyPlayerInWaitingList():
  try:
    TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X , BOTTOM_RIGHT_Y = GetCoordinatesOfTheFirstPlayerInWaitingList()
    
    denyEntryButton = pg.locateCenterOnScreen(
      "./images/deny-entry-button.png", 
      region=(TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X - TOP_LEFT_X, BOTTOM_RIGHT_Y - TOP_LEFT_Y), 
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

#-------------------------------------------------------------

def WriteLogInBannedPlayersFile(playerName: str):
  date = str(datetime.now())

  messageToWrite = " ".join([date, playerName, '\n'])

  with open('./activityLogs/bannedPlayers.txt', 'a') as f:
    f.write(messageToWrite)

#-------------------------------------------------------------

def CloseModal():
  try:
    closeModal = pg.locateCenterOnScreen("./images/close-modal-button.png", grayscale=True, confidence=0.8)
    pg.click(closeModal[0], closeModal[1])

    time.sleep(GetRandomClickInterval())
  except pg.ImageNotFoundException: 
    print('Close modal button not found')

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