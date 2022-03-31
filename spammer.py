from errno import ENETRESET
import sys,time,random,pyautogui,signal
try:
  typing_speed = 100
  def plztype(t):
      for l in t:
          sys.stdout.write(l)
          sys.stdout.flush()
          time.sleep(random.random()*10.0/typing_speed)
  plztype("""\033[1;32;40m spammer 1.1.0 by bob

  █▀ █▀█ ▄▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀█
  ▄█ █▀▀ █▀█ █░▀░█ █░▀░█ ██▄ █▀▄
  

    dont use this to annoy other people!!!!
  """)
  m = input("\033[1;32;40m message you wanna type is: ")
  s = input("\033[1;32;40m how fast do you want to type? (example = 1.0)")
  plztype("""\033[1;32;40m oke , you have 10 seconds before spam starts , \n
  go and click on the text input (where you type)
  """)
  time.sleep(10)
  while True:
    pyautogui.write(m)
    bool(time.sleep(s))
    pyautogui.press('enter')
 
except KeyboardInterrupt:
 print("\n \033[1;32;40m goodbye! have a great time! ")
