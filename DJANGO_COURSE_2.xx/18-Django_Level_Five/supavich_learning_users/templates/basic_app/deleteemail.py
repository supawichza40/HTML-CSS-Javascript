import pyautogui
import time
counter = 0
counter2 = 0
while(True):
    if counter2>=10:
        break
    if counter<=10:
        pyautogui.click(x=2222,y=190)
        time.sleep(1)
        pyautogui.click(x=2254,y=326)
        time.sleep(1)
        pyautogui.click(x=2346,y=193)
        time.sleep(1)
        counter+=1
    else:
        time.sleep(2)
        counter = 0
        
        counter2 +=1
        pyautogui.click(x=2222,y=190)
        time.sleep(2)
        pyautogui.click(x=2278,y=286)
        time.sleep(1)
        pyautogui.click(x=2557,y=195)
        time.sleep(2)
        pyautogui.click(x=2605,y=333)
        time.sleep(1)
        
        
        
        
        