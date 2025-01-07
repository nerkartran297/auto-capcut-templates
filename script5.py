import pyautogui
import pyperclip
import time

def PathPaste(ten):
    path = f"C:\\Users\\nerka\\Downloads\\new\\{ten}" 
    pyperclip.copy(path)
    pyautogui.hotkey('ctrl', 'v')

def AutoEdit(ten):
    pyautogui.click(340,820)
    time.sleep(0.3)
    pyautogui.rightClick(340,820)
    time.sleep(0.3)
    pyautogui.click(420,900)
    time.sleep(0.3)
    pyautogui.click(520,160) #path
    time.sleep(0.3)
    PathPaste(ten) #PasteThePath
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.click(350,290) #file location
    time.sleep(0.3)
    pyautogui.click(1050,910) #open button
    time.sleep(0.3)
    pyautogui.click(1026,730) #replace clip button
    time.sleep(1)

    pyautogui.click(580,820) #replace second clip
    time.sleep(0.3)
    pyautogui.rightClick(580,820)
    time.sleep(0.3)
    pyautogui.click(660,900)
    time.sleep(0.3)
    pyautogui.click(350,320) #file location
    time.sleep(0.3)
    pyautogui.click(1050,910) #open button
    time.sleep(0.3)
    pyautogui.click(1026,730) #replace clip button
    time.sleep(1)

    pyautogui.click(740,820) #replace clip 3
    time.sleep(0.3)
    pyautogui.rightClick(740,820)
    time.sleep(0.3)
    pyautogui.click(820,900)
    time.sleep(0.3)
    pyautogui.click(350,345) #file location
    time.sleep(0.3)
    pyautogui.click(1050,910) #open button
    time.sleep(0.3)
    pyautogui.click(1026,730) #replace clip button
    time.sleep(1)

    pyautogui.click(960,820) #replace clip 4
    time.sleep(0.3)
    pyautogui.rightClick(960,820)
    time.sleep(0.3)
    pyautogui.click(1040,900)
    time.sleep(0.3)
    pyautogui.click(350,370) #file location
    time.sleep(0.3)
    pyautogui.click(1050,910) #open button
    time.sleep(0.3)
    pyautogui.click(1026,730) #replace clip button
    time.sleep(1)

    pyautogui.click(1220,820) #replace clip 5
    time.sleep(0.3)
    pyautogui.rightClick(1220,820)
    time.sleep(0.3)
    pyautogui.click(1300,900)
    time.sleep(0.3)
    pyautogui.click(350,395) #file location
    time.sleep(0.3)
    pyautogui.click(1050,910) #open button
    time.sleep(0.3)
    pyautogui.click(1026,730) #replace clip button
    time.sleep(1)

    pyautogui.click(1500,820) #replace clip 6
    time.sleep(0.3)
    pyautogui.rightClick(1500,820)
    time.sleep(0.3)
    pyautogui.click(1580,900)
    time.sleep(0.3)
    pyautogui.click(350,420) #file location
    time.sleep(0.3)
    pyautogui.click(1050,910) #open button
    time.sleep(0.3)
    pyautogui.click(1026,730) #replace clip button
    time.sleep(1)

    pyautogui.click(1760,18) #export button
    time.sleep(0.5)
    pyautogui.click(1092,249) #double click vao ten
    time.sleep(0.1)
    pyautogui.click(1092,249)
    time.sleep(0.3)
    pyperclip.copy(ten) #copy name to clipboard
    pyautogui.hotkey('ctrl', 'v') #paste name
    time.sleep(0.3)
    pyautogui.click(1148,824) #final export button
    time.sleep(5)
    pyautogui.click(1230,820) #cancel button





# time.sleep(3)
# name=10
# AutoEdit(name)
name=159
while name<=159:
    time.sleep(3)
    AutoEdit(name)
    name=name+1

