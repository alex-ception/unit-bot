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
    waitingList = pg.locateCenterOnScreen("./images/waiting-list-button.png", confidence=0.8)
    pg.click(waitingList[0], waitingList[1])

    time.sleep(GetRandomClickInterval())
  except pg.ImageNotFoundException: 
    print('Waiting list button NOT FOUND')

#-------------------------------------------------------------

def IsScrollDownNeeded():
  # useful to know if there's so many people in the queue list
  try:
    applicantsTitle = pg.locateOnScreen("./images/applicants.png", confidence=0.8)

    if applicantsTitle is not None:
      top_left_x = int(applicantsTitle[0])
      top_left_y = int(applicantsTitle[1])
      bottom_right_x= int(applicantsTitle[0] + applicantsTitle[2] + 100)
      bottom_right_y= int(applicantsTitle[1] + applicantsTitle[3])
    

      getAllApplicantsImage = pg.screenshot(region=(top_left_x, top_left_y, bottom_right_x - top_left_x, bottom_right_y - top_left_y))

      getAllApplicantsFullSentence = pytesseract.image_to_string(getAllApplicantsImage)

      getAllApplicantsNumbers = getAllApplicantsFullSentence.strip()[12:]

      time.sleep(GetRandomClickInterval())

      if int(getAllApplicantsNumbers[0]) > 6 or getAllApplicantsNumbers[1] != "/":
        return True
      else:
        return False
      
  except pg.ImageNotFoundException:
    return False

#-------------------------------------------------------------

def ScrollDown(coords: list[int] | None):
  if coords is not None:
    TOP_LEFT_X, TOP_LEFT_Y = coords

    # Scroll down to get the first player in the list (when there's to many people)
    pg.mouseDown((TOP_LEFT_X + 100), (TOP_LEFT_Y + 100), button='left', duration=0.5) 
    pg.moveTo(TOP_LEFT_X, 15000, duration=1)
    pg.mouseUp(button='left', duration=0.5)
    
#-------------------------------------------------------------

def GetCoordinatesOfTheFirstPlayerInWaitingList():
  try:
    coords = pg.locateCenterOnScreen(
      "./images/officer-request-title.png",  
      confidence=0.8)
    
    if coords is not None:
      time.sleep(0.5)
      
      TOP_LEFT_X = int(coords[0] - 150)
      TOP_LEFT_Y = int(coords[1] + 100)
      BOTTOM_RIGHT_X = int(coords[0] + 230)
      BOTTOM_RIGHT_Y = int(coords[1] + 160)

      return [TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X, BOTTOM_RIGHT_Y]
    else:
      return None

  except pg.ImageNotFoundException:
    print('Officer request image (main title) NOT FOUND')

#-------------------------------------------------------------

def GetFirstPlayerNameInTheList():
  try:
    coords = GetCoordinatesOfTheFirstPlayerInWaitingList()

    if coords is not None:
      TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X , BOTTOM_RIGHT_Y = coords

      isScrollNeeded = IsScrollDownNeeded()

      if isScrollNeeded == True:
        ScrollDown(coords)
        ScrollDown(coords)
        ScrollDown(coords)

      playerNameImage = pg.screenshot(region=(TOP_LEFT_X, TOP_LEFT_Y, (BOTTOM_RIGHT_X - 130) - TOP_LEFT_X, (BOTTOM_RIGHT_Y - 27) - TOP_LEFT_Y))

      time.sleep(0.5)

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

    bracketIndex = playerNameWithoutSpaces.find("]") # Example: [1Pr] (the second braket because sometimes tesseract find "(" instead of "[").

    isBanned = False

    if bracketIndex == -1:
      # PLAYER DON'T HAVE AN ALLIANCE

      for player in jsonConfig['blacklist_players']:
        if player.lower() in playerNameWithoutSpaces.lower():
          isBanned=True
          
    else:
      # PLAYER HAVE AN ALLIANCE

      playerAlliance = playerNameWithoutSpaces[bracketIndex-3 : bracketIndex]
      playerName = playerNameWithoutSpaces[bracketIndex+1 : ]

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
    coords = GetCoordinatesOfTheFirstPlayerInWaitingList()

    if coords is not None:
      TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X , BOTTOM_RIGHT_Y = coords

      accepteEntryButton = pg.locateCenterOnScreen(
        "./images/accept-entry-button.png", 
        region=(TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X - TOP_LEFT_X, BOTTOM_RIGHT_Y - TOP_LEFT_Y), 
        confidence=0.7)
      
      pg.click(accepteEntryButton[0], accepteEntryButton[1])

  except pg.ImageNotFoundException:
    print('Accept entry image NOT FOUND')

#-------------------------------------------------------------

def DenyPlayerInWaitingList():
  try:
    coords = GetCoordinatesOfTheFirstPlayerInWaitingList()

    if coords is not None:
      TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X , BOTTOM_RIGHT_Y = coords
    
      denyEntryButton = pg.locateCenterOnScreen(
        "./images/deny-entry-button.png", 
        region=(TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_RIGHT_X - TOP_LEFT_X, BOTTOM_RIGHT_Y - TOP_LEFT_Y), 
        confidence=0.7)

      pg.click(denyEntryButton[0], denyEntryButton[1])

      time.sleep(GetRandomClickInterval())

      ConfirmDenyPlayerInWaitingList()

  except pg.ImageNotFoundException:
    print('Deny entry image NOT FOUND')

#-------------------------------------------------------------

def ConfirmDenyPlayerInWaitingList():
  try:
    confirmDenyPlayerInWaitingListButton = pg.locateCenterOnScreen(
      "./images/confirm-deny-entry-button.png",
      confidence=0.7)
    
    pg.click(confirmDenyPlayerInWaitingListButton[0], confirmDenyPlayerInWaitingListButton[1])

    time.sleep(GetRandomClickInterval())
    
  except pg.ImageNotFoundException:
    print('Confirm Deny player from buff image NOT FOUND')

#-------------------------------------------------------------

def CheckTimeInTheBuff():
  try:
    with open('./config.json') as config_file:
      jsonConfig = json.load(config_file)

      timeInTheBuffImage = pg.screenshot(region=(TIME_IN_THE_BUFF_TOP_LEFT_X, TIME_IN_THE_BUFF_TOP_LEFT_Y, TIME_IN_THE_BUFF_BOTTOM_RIGHT_X - TIME_IN_THE_BUFF_TOP_LEFT_X, TIME_IN_THE_BUFF_BOTTOM_RIGHT_Y - TIME_IN_THE_BUFF_TOP_LEFT_Y))

      timeInTheBuffFullSentence = pytesseract.image_to_string(timeInTheBuffImage)

      timeInTheBuffSplitHour = timeInTheBuffFullSentence.strip()[14:]

      hourAndMinute = list(timeInTheBuffSplitHour)

      hours = int(hourAndMinute[0] + hourAndMinute[1])
      minutes = int(hourAndMinute[3] + hourAndMinute[4])

      totalMinutes = (hours * 60) + minutes
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
      confidence=0.7)
    
    pg.click(ejectPlayerFromBuffButton[0], ejectPlayerFromBuffButton[1])

    time.sleep(GetRandomClickInterval())

    ConfirmEjectPlayerFromBuff()

  except pg.ImageNotFoundException:
    print('Eject player from buff image NOT FOUND')

#-------------------------------------------------------------

def ConfirmEjectPlayerFromBuff():
  try:
    confirmEjectPlayerFromBuffButton = pg.locateCenterOnScreen(
      "./images/confirm-eject-player-button.png",
      confidence=0.7)

    pg.click(confirmEjectPlayerFromBuffButton[0], confirmEjectPlayerFromBuffButton[1])

    time.sleep(GetRandomClickInterval())

  except pg.ImageNotFoundException:
    print('Confirm Eject player from buff image NOT FOUND')

#-------------------------------------------------------------

def WriteLogInBannedPlayersFile(playerName: str):
  date = str(datetime.now())

  messageToWrite = " ".join([date, playerName, '\n'])

  with open('./activityLogs/bannedPlayers.txt', 'a') as f:
    f.write(messageToWrite)

#-------------------------------------------------------------

def CloseModal():
  try:
    closeModal = pg.locateCenterOnScreen("./images/close-modal-button.png", confidence=0.8)
    pg.click(closeModal[0], closeModal[1])

    time.sleep(GetRandomClickInterval())
  except pg.ImageNotFoundException: 
    print('Close modal button NOT FOUND')

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
