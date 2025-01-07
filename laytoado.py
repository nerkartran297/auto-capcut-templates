import pyautogui
import time 

def laytoado ():
    i=3
    while i>0:
        print(i)
        time.sleep(1)
        i=i-1
    current_mouse_position = pyautogui.position()
    print(f"x={current_mouse_position.x}, y={current_mouse_position.y}")


laytoado()

