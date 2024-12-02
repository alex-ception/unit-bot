import pyautogui as pg

#-------------------------------------------------------------

def GetAntiBotModalLeaveGameButton():
  try:
    return pg.locateCenterOnScreen("./images/leave-game-button.png", grayscale=True, confidence=0.8)
   
  except pg.ImageNotFoundException: 
    None

#-------------------------------------------------------------

def CloseAntiBotModal():
  try:
    antiBotModalCloseButton = pg.locateCenterOnScreen("./images/close-modal-button.png", grayscale=True, confidence=0.8)
    pg.click(antiBotModalCloseButton[0], antiBotModalCloseButton[1])

  except pg.ImageNotFoundException: 
    print('Anti bot modal close button not found')

#-------------------------------------------------------------

def CheckAndCloseAntiBotModal():
  while True:
    leaveGameButton = GetAntiBotModalLeaveGameButton()

    if leaveGameButton is not None:
      print('Close anti bot modal !!!!!!!!!!!!!')
      CloseAntiBotModal()