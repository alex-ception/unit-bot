import pyautogui as pg

#-------------------------------------------------------------

def GetAntiBotModalLeaveGameButton():
  try:
    return pg.locateCenterOnScreen("./images/exit-game-button.png", grayscale=True, confidence=0.9)
   
  except pg.ImageNotFoundException: 
    return None

#-------------------------------------------------------------

def CloseAntiBotModal():
  try:
    antiBotModalCloseButton = pg.locateCenterOnScreen("./images/close-modal-button.png", grayscale=True, confidence=0.8)
    pg.click(antiBotModalCloseButton[0], antiBotModalCloseButton[1])

  except pg.ImageNotFoundException: 
    print('Anti bot modal close button NOT FOUND')

#-------------------------------------------------------------

def CheckAndCloseAntiBotModal():
  while True:
    leaveGameButton = GetAntiBotModalLeaveGameButton()

    if leaveGameButton is not None:
      print('Close anti bot modal !!!!!!!!!!!!!')
      CloseAntiBotModal()