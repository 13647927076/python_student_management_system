import pyautogui
import time
import pyperclip
import random

from pyautogui import hotkey

text = ["1", "2", "3", '4']
text_1 = ["随机轰炸 @ZeT ", "随机轰炸 @尘疏诀 ", "随机轰炸 @花华画華 "]
time.sleep(5)
for _ in range(100):
    messge = random.choice(text
                           )
    pyperclip.copy(messge)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(random.uniform(0.2, 0.5))
