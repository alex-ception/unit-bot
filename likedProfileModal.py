import pyautogui as pg

#-------------------------------------------------------------

def GetLikedProfileButton():
  try:
    return pg.locateCenterOnScreen("./images/dismiss-liked-profile.png", grayscale=True, confidence=0.9)
   
  except pg.ImageNotFoundException: 
    return None

#-------------------------------------------------------------

def CheckLikedProfileModal():
  while True:
    likedProfileButton = GetLikedProfileButton()

    if likedProfileButton is not None:
      print('Close liked profile modal !!!!!!!!!!!!!')
      pg.click(likedProfileButton[0], likedProfileButton[1])