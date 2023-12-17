import os
from ahk import AHK
import pyautogui
import requests
import random
from time import sleep
from pyautogui import hotkey, click, press
import subprocess
pyautogui.FAILSAFE = False
ahk = AHK()

data = {"titles": {"1": "DWARF", "2": "ORK", "3": "DEAD", "4": "HUMAN", "5": "ELFIE"},
        "images": {"1": "Dwarf", "2": "Orc", "3": "Dead", "4": "Human", "5": "Elf"},
        "lvlingPresses": {"1": 2, "2": 3}}
race = "3"
stat = "2"
def checkLvlUp(race):
    levelUp =  pyautogui.locateOnScreen(f"img/levelUp{data['images'][race]}.png", minSearchTime=3, region=(0,0,600,900), confidence=.95)
    if levelUp:
        send_message("Level is upgrading...")
        press('down', presses = data["lvlingPresses"][stat], interval=.15)
        sleep(.2)
        press('enter')
        sleep(.2)
        press('up', presses=3, interval=.15)
        sleep(.2)
        press('enter')
        sleep(.2)
        rightSoft()
        sleep(.5)
        leftSoft()
        send_message("Upgraded")
    else:
        print("No level up")
def terminate_process(process_name):
    try:
        subprocess.run(["taskkill", "/F", "/IM", process_name], check=True)
        print(f"Successfully terminated the process: {process_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to terminate the process: {process_name}. Error: {e}")
def send_message(message, chat_id = '866012534', token = '6916347729:AAEwnWUGrzhsxBrmYNtfr1bTxtjcackORek'):
    print(message)
    try:
        root_url = 'https://api.telegram.org/bot'
        url = f"{root_url}{token}/sendMessage"
        requests.post(url, json = {'chat_id':chat_id, 'text': message}, timeout = .5)
    except Exception as ex:
        print(ex)
def rightSoft():
    click(800, 950)
    sleep(.2)
def leftSoft():
    click(400, 950)
    sleep(.2)
def killWindow():
    send_message("Killing OASIS")
    oasis = ahk.find_window(process=r"C:\Program Files\Java\jre-1.8\bin\javaw.exe")
    if oasis:
        send_message("Found Java, killing | sleep 5...")
        oasis.kill()
    sleep(5)
def runWindow():
    send_message("Run OASIS | sleep 5...")
    os.startfile(f"C:/Users/38098/Desktop/linksOasis/{data['titles'][race]}.lnk")
    sleep(5)
def setWindow():
    print("setting Window")
    win = ahk.find_window(title = f'{data["titles"][race]}'.encode('utf-8'))
    if win:
        print("Found OASIS, setting | sleep 3...")
        win.activate()
        sleep(0.5)
        win.move(0, 0, 1200, 1000)
        sleep(3)
def activate():
    win = ahk.find_window(title = f'{data["titles"][race]}'.encode('utf-8'))
    if win:
        print("Found OASIS, activate | sleep 3...")
        win.activate()
        sleep(0.5)
def toCenter():
    rightSoft()
    sleep(.2)
    press('up')
    sleep(.2)
    press('enter')
    sleep(.2)
def changeLocation():
    send_message("Login into game | sleep 5...")
    press("enter")
    sleep(5)
    def goingRight1():
        beweg = 0
        while True:
            activate()
            send_message("Going Right1")
            press('right', presses=random.randint(12,16), interval=.15)
            sleep(.15)
            press('left', presses=2, interval=.15)
            sleep(.15)
            press('enter')
            sleep(1)
            toCenter()
            if beweg >= 1:
                rightCloud = pyautogui.locateOnScreen("img/opbRgCloud1.png", minSearchTime=1, region=(600,0,600,900), confidence=.9)
                if rightCloud:
                    send_message("Found right Cloud")
                    click(rightCloud)
                    send_message("Location Changed")
                    break
            if beweg >= 30:
                send_message("Can't find right cloud")
                return "bad_Login"
            beweg += 1
    inMap = pyautogui.locateOnScreen("img/opbInMap.png", minSearchTime=1.5, region=(0,0,1200,900), confidence=.9)
    if inMap:
        send_message("Hero's on Map")
        sleep(1)
        leftSoft()
        checkLvlUp(race)
        sleep(1)
        print("Going right...")
        if goingRight1() == "bad_Login":
            return "bad_Login"
    else:
        return "bad_Login"
def searchDragon(dragonImage, region):
    print(f"Searching dragon {dragonImage}...")
    dragon = pyautogui.locateOnScreen(f"img/{dragonImage}.png", minSearchTime=2, region=region, confidence=.9)
    if dragon:
        click(dragon)
        sleep(.23)
        press('up')
        sleep(.2)
        press('enter')
        send_message("Found Dragon, attack | sleep 5...")
        sleep(5)
        return True
    else:
        return False
def searchBattle(field, trollImage):
    print("Search Battle | sleep 5...")
    battle = pyautogui.locateOnScreen(f"img/{field}.png", minSearchTime=5, region=(0,0,600,400), confidence=.9)
    if battle:
        send_message("Found Battle")
        def useMagic():
            print("Using Magic")
            rightSoft()
            press('up', presses=3, interval=.15)
            sleep(.2)
            press('enter', presses=3, interval=.25)
            sleep(.2)
            press('up')
            sleep(.2)
            press('enter')
            sleep(1)
        sleep(.5)
        print("Seach troll...")
        noTroll = 0
        turn = 1
        while True:
            troll = pyautogui.locateCenterOnScreen(f"img/{trollImage}.png", minSearchTime=6, region=(415, 325, 370, 350), confidence=.85, grayscale=True)
            if troll:
                if turn > 0 and turn < 5:
                    useMagic()
                print(f"Found Troll {troll[0]} - {troll[1]}")
                if troll[0] > 600:
                    press('left')
                else:
                    press('right')
                sleep(.2)
                press('enter')
                noTroll = 0
                turn += 1
            else:
                noTroll += 1
                print(f"No troll {noTroll}")
            if noTroll > 1 and noTroll % 2 == 0:
                if noTroll > 3:
                    print("Check message Bug")
                    bug1 = pyautogui.locateOnScreen("img/bBug1.png", minSearchTime=3, region=(0, 0, 1200, 900), confidence=.85)
                    if bug1:
                        ("Fixed message bug")
                        click(600, 900)
                    else:
                        print("just click Enter")
                        press('enter')
                victory = pyautogui.locateOnScreen("img/victory.png", minSearchTime=5, region=(0, 0, 1200, 500), confidence=.9)
                if victory:
                    leftSoft()
                    send_message("Victory")
                    checkLvlUp("5")
                    break
                else:
                    print("No Victory")
            if noTroll >= 6:
                leftSoft()
                send_message("Bad Finish")
                return "badFinish"
        print("Finish Battle")
        return "succesBattle"
    miss = pyautogui.locateOnScreen("img/missFight.png", minSearchTime=1, region=(0,0,1200,600), confidence=.9)
    if miss:
        send_message("Miss(Already fighting)")
        leftSoft()
        return "miss"
def stepping(img, x, y):
    dot = pyautogui.locateCenterOnScreen(f"img/{img}.png", minSearchTime=5, region=(0, 0, 1200, 900), confidence=.85)
    if dot:
        print(f"Found {img}")
        pyautogui.click(dot[0]+x, dot[1]+y)
        sleep(1.3)
    elif not dot:
        send_message(f"Can't find {dot}")
def dragonFinaly(dragoMap, reggi, fieldColor):
    if searchDragon(dragoMap, reggi):
        if fieldColor == "braun":
            fight = searchBattle("brounField", "battleCanGoBr")
        elif fieldColor == "white":
            fight = searchBattle("whiteField", "battleCanGoWh")
        elif fieldColor == "any":
            fight = searchBattle("brounField", "battleCanGoBr")
            if fight == 'succesBattle' or fight == 'miss':
                return "goodFinish"
            elif fight == "badFinish":
                return "badFinish"
            else:
                fight = searchBattle("whiteField", "battleCanGoWh")
                if fight == 'succesBattle' or fight == 'miss':
                    return "goodFinish"
                elif fight == "badFinish":
                    return "badFinish"
        if fight == 'succesBattle' or fight == 'miss':
            return "goodFinish"
        elif fight == "badFinish":
            return "badFinish"
terminate_process("keymanager.exe")

lap = 0
while True:
    runWindow()
    setWindow()
    if changeLocation() == "bad_Login":
        sleep(60)
        send_message("not in town. sleep 60...")
        killWindow()
    send_message("Dragon ##1")
    press('up', presses=11, interval=.15)
    press('down', presses=9, interval=.15)
    for _ in range(4):
        if dragonFinaly("partDrago", (0, 0, 1200, 600), "braun"):
            break
        elif dragonFinaly("opbDragon1a", (0, 0, 1200, 600), "braun"):
            break
        else:
            press('up', presses=9, interval=.15)
            press('left', presses=15, interval=.15)
            print("Going step1")
            stepping("opbStep1", 30, -50)
            toCenter()
            press('down', presses=15, interval=.15)
    press('up', presses=9, interval=.15)
    press('left', presses=15, interval=.15)
    print("Going step1")
    stepping("opbStep1", 30, -50)
    press('right', presses=3, interval=.15)
    press('up', presses=4, interval=.15)
    press('enter')
    sleep(.5)
    toCenter()
    send_message("Dragon ##2")
    for _ in range(2):
        if dragonFinaly("partDrago", (0, 0, 1200, 600), "white"):
            break
    stepping("opbStep2", 250, 168)
    toCenter()
    stepping("opbStep1", 30, -50)
    toCenter()
    stepping("opbStep3", -125, 235)
    toCenter()
    stepping("opbStep3", 120, 245)
    toCenter()
    send_message("Dragon ##3")
    for _ in range(4):
        if dragonFinaly("partDrago", (600, 0, 600, 900), "any"):
            break
        else:
            press('up', presses=11, interval=.15)
            press('left', presses=11, interval=.15)
            stepping("opbStep3", 120, 245)
            toCenter()
    press('up', presses=11, interval=.15)
    press('left', presses=11, interval=.15)
    stepping("opbStep3", 120, 245)
    toCenter()
    stepping("opbStep3", 570, 80)
    toCenter()
    send_message("Dragon ##4")
    for _ in range(2):
        if dragonFinaly("partDrago", (600, 200, 600, 700), "braun"):
            break
    press('up', presses=11, interval=.15)
    stepping("opbStep4", 165, -220)
    toCenter()
    send_message("Dragon ##5")
    for _ in range(4):
        if dragonFinaly("partDrago", (600, 300, 600, 600), "any"):
            break
        else:
            stepping("opbStep4", 165, -220)
            toCenter()
    stepping("opbStep4", 165, -220)
    toCenter()
    press('up', presses=15, interval=.15)
    send_message("Dragon ##6")
    for _ in range(4):
        if dragonFinaly("partDrago", (600, 0, 600, 500), "white"):
            break
        else:
            press('down', presses=15, interval=.15)
            stepping("opbStep4", 165, -220)
            toCenter()
            press('up', presses=15, interval=.15)
    toCenter()
    press('down', presses=15, interval=.15)
    stepping("opbStep4", 165, -220)
    toCenter()
    press('down', presses=17, interval=.15)
    stepping("opbStep5", 160, -100)
    toCenter()
    press('down', presses=12, interval=.15)
    send_message("Dragon ##7")
    for _ in range(4):
        if dragonFinaly("partDrago", (0, 300, 1200, 600), "any"):
            break
        else:
            press('up', presses=11, interval=.15)
            stepping("opbStep5", 160, -100)
            toCenter()
            press('down', presses=12, interval=.15)
    toCenter()
    press('up', presses=11, interval=.15)
    stepping("opbStep5", 160, -100)
    toCenter()
    stepping("opbStep5", -295, 300)
    toCenter()
    press('left', presses=15, interval=.15)
    send_message("Dragon ##8")
    for _ in range(4):
        if dragonFinaly("partDrago", (0, 300, 600, 600), "white"):
            break
        else:
            press('up', presses=13, interval=.15)
            press('left', presses=15, interval=.15)
            stepping("opbStep6", -170, -45)
            press('down', presses=14, interval=.15)
    toCenter()
    press('up', presses=13, interval=.15)
    press('left', presses=15, interval=.15)
    stepping("opbStep6", -170, -45)
    toCenter()
    send_message("Dragon ##9")
    for _ in range(4):
        if dragonFinaly("partDrago", (0, 0, 600, 600), "white"):
            break
        else:
            stepping("opbStep6", -170, -45)
            toCenter()
    killWindow()
    lap += 1
    send_message(f"LAP {lap} COMPLETED")

hotkey('win', '3')
sleep(3)
keyM = ahk.find_window(process=r"C:\NewFolder\ATNSOFT_Key_Manager\keymanager.exe")
if keyM:
    keyM.kill()