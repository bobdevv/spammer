from errno import ENETRESET
import pyautogui
import time
import sys
import sys,time,random

typing_speed = 70
def plztype(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
plztype("""spammer 1.0.0 by bob

█▀ █▀█ ▄▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀█
▄█ █▀▀ █▀█ █░▀░█ █░▀░█ ██▄ █▀▄
  

  dont use this to annoy other people!!!!
""")
m = input("what is the message? \n")
plztype("""oke , you have 10 seconds before spam starts , \n
go and click on the text input (where you type)
""")
time.sleep(10)
while True:
    pyautogui.typewrite(m)
    time.sleep(0.5)
    pyautogui.press('enter')