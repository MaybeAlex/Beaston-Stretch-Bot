import pyautogui, time
while True:
    sec = 0
    start = pyautogui.locateCenterOnScreen("start.JPG", confidence=0.9)
    print("checked")
    if start == None:
        continue
    elif start != None: 
        print("yes, starting")
        while True:
            stop = pyautogui.locateCenterOnScreen("stop.JPG", confidence=0.9)
            if sec % 1200 == 0:
                pyautogui.moveTo(828, 828)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.moveTo(909, 998)
                pyautogui.click()
            time.sleep(0.59)
            if stop != None:
                print("ok im stopping")
                break
            sec += 1
            print(str(sec//86400) + " days "+ str(sec//3600) + "h " + str(sec//60) + "min " + str(sec % 60) + "s")