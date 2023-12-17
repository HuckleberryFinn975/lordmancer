import pyautogui

dot = pyautogui.locateCenterOnScreen("img/opbStep6.png", minSearchTime=5, region=(0, 0, 1200, 900), confidence=.85)
print(dot)
pyautogui.moveTo(dot[0] - 295, dot[1] + 300)
# pyautogui.click()