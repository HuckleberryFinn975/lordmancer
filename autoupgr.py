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
race = input("\t1 - Dwarf\n\t2 - Orc\n\t3 - Dead\n\t4 - Human\n\t5 - Elf\nSelect race: ")
stat = input("\t1 - Dexterity(Ловкость)\t\n2 - Cunning(Хитрость)\nChoose a skill to level up: ")

def terminate_process(process_name):
    try:
        subprocess.run(["taskkill", "/F", "/IM", process_name], check=True)
        print(f"Successfully terminated the process: {process_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to terminate the process: {process_name}. Error: {e}")
terminate_process("keymanager.exe")
def send_message(message, chat_id = '866012534', token = '6905459015:AAGO26EbTHvy3xIlaSm6hpd94RklEWVhRAs'):
    print(message)
    try:
        root_url = 'https://api.telegram.org/bot'
        url = f"{root_url}{token}/sendMessage"
        requests.post(url, json = {'chat_id':chat_id, 'text': message}, timeout = .5)
    except Exception as ex:
        print(ex)

def checkLvlUp():
    levelUp =  pyautogui.locateOnScreen(f"img/levelUp{data['titles'][race]}.png", minSearchTime=3, region=(0,0,600,900), confidence=.95)
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
        click(800, 950)
        sleep(.2)
        click(400, 950)
        sleep(.2)
        send_message("Upgraded")
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
    send_message("setting Window")
    win = ahk.find_window(title = f'{data["titles"][race]}'.encode('utf-8'))
    if win:
        send_message("Found OASIS, setting | sleep 3...")
        win.activate()
        sleep(0.5)
        win.move(0, 0, 1200, 1000)
        sleep(3)
def activate():
    win = ahk.find_window(title = f'{data["titles"][race]}'.encode('utf-8'))
    if win:
        send_message("Found OASIS, activate | sleep 3...")
        win.activate()
        sleep(0.5)
def changeLocation():
    send_message("Login into game | sleep 5...")
    press("enter")
    sleep(5)
    inTown = pyautogui.locateOnScreen(f"img/inTown{data['images'][race]}.png", minSearchTime=1.5, region=(0,0,1200,900), confidence=.95)
    if inTown:
        send_message("Hero's in Town")
        send_message("go out town")
        sleep(2)
        press("enter")
        sleep(2)
        checkLvlUp()
        sleep(1)
        send_message("Going right...")
        press('right', presses=11, interval=.15)
        sleep(.5)
        press('enter')
        send_message('Search right edge')
        beweg = 0
        while True:
            rightEdge = pyautogui.locateOnScreen("img/mapRightEdge.png", minSearchTime=1, region=(600,600,600,300), confidence=.95)
            if rightEdge:
                send_message("Found right edge")
                click(rightEdge)
                sleep(1)
            if beweg >= 2:
                rightCloud = pyautogui.locateOnScreen("img/mapRightCloud.png", minSearchTime=1, region=(600,0,600,900), confidence=.9)
                if rightCloud:
                    send_message("Found right Cloud")
                    click(rightCloud)
                    send_message("Location Changed")
                    sleep(5)
                    send_message("Going right...")
                    press('right', presses=8, interval=.15)
                    sleep(.5)
                    press('enter')
                    break
            if beweg >= 30:
                send_message("Can't find right cloud")
                return "bad_Login"
            beweg += 1
    else:
        return "bad_Login"
def going():
    def searchCloudUp():
        upperCloud = pyautogui.locateOnScreen("img/mapUpperCloud.png", minSearchTime=1, region=(0,0,1200,450), confidence=.9)
        if upperCloud:
            send_message("Found upper Cloud")
            click(upperCloud)
            send_message("Location Changed")
            return True
    def searchCloudDown():
        lowerCloud = pyautogui.locateOnScreen("img/mapLowerCloud.png", minSearchTime=1, region=(0,450,1200,650), confidence=.9)
        if lowerCloud:
            send_message("Found lower Cloud")
            click(lowerCloud)
            send_message("Location Changed")
            return True
    def searchDragon():
        dragon = pyautogui.locateOnScreen("img/mapDragon.png", minSearchTime=1, region=(0,0,1200,900), confidence=.95)
        if dragon:
            click(dragon)
            sleep(.33)
            click(400, 777)
            send_message("Found Dragon, attack | sleep 5...")
            sleep(5)
            return True
    def searchBattle():
        battle = pyautogui.locateOnScreen("img/startBattle.png", minSearchTime=1, region=(0,0,600,400), confidence=.95)
        if battle:
            send_message("Found Battle | sleep 100...")
            sleep(100)
            click(420, 950)
            send_message("close pop-up")
            deff = 0
            while True:
                battle = pyautogui.locateOnScreen("img/startBattle.png", minSearchTime=1, region=(0,0,600,400), confidence=.95)
                if battle:
                    break
                sleep(5)
                send_message("wait finish battle")
                if deff>=30:
                    send_message("5 min went")
                    break
                deff += 1
            return "battle"
        miss = pyautogui.locateOnScreen("img/missFight.png", minSearchTime=1, region=(0,0,1200,600), confidence=.95)
        if miss:
            send_message("Miss(Already fighting)")
            click(420, 950)
            return "miss"
    def goingUP():
        dcount = 0
        while True:
            activate()
            send_message("Going UP")
            if searchDragon():
                k = searchBattle()
                if k == "battle":
                    send_message("Finished")
                    return "finish"
                if k == "miss":
                    pass
            if searchCloudUp():
                sleep(5)
                press('down')
                sleep(.25)
                press('enter')
                return
            if dcount >= 30:
                return "finish"
            press('up', presses=random.randint(13,17), interval=.15)
            sleep(.15)
            press('down', presses=2, interval=.15)
            sleep(.15)
            press('enter')
            sleep(1)
            click(800, 950)
            sleep(.1)
            click(800, 777)
            sleep(.1)
            dcount += 1
    def goingDown():
        dcount = 0
        while True:
            activate()
            send_message("Going Down")
            if searchDragon():
                k = searchBattle()
                if k == "battle":
                    send_message("Finished")
                    return "finish"
                if k == "miss":
                    pass
                else:
                    sleep(2)
                    continue
            if searchCloudDown():
                sleep(5)
                press('up')
                sleep(.25)
                press('enter')
                return
            if dcount >= 30:
                return "finish"
            press('down', presses=random.randint(13,17), interval=.15)
            sleep(.15)
            press('up', presses=2, interval=.15)
            sleep(.15)
            press('enter')
            sleep(1)
            click(800, 950)
            sleep(.1)
            click(800, 777)
            sleep(.1)
            dcount += 1
    while True:
        if goingDown() == 'finish':
            break
        if goingUP() == 'finish':
            break
        

        
# while True:
#     runWindow()
#     setWindow()
#     if changeLocation() == "bad_Login":
#         sleep(60)
#         send_message("not in town. sleep 60...")
#         killWindow()
#         continue
#     going()
#     killWindow()

runWindow()
setWindow()