from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X:  727 Y:  548 RGB: ( 75, 219, 106)

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #Pauses the click for 0.01 second to register it
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel (727, 548) [0] == 75:
        click (727,548)
    if pyautogui.pixel (727, 548) [1] == 219:
        click (727,548)
    if pyautogui.pixel (727, 548) [0] == 106:
        click (727,548)
