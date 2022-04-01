from errno import ENETRESET
import sys,time,random,pyautogui,signal
fuckyou = 0
try:
  typing_speed = 150
  def plztype(t):
      for l in t:
          sys.stdout.write(l)
          sys.stdout.flush()
          time.sleep(random.random()*10.0/typing_speed)
  plztype("""\033[1;50;40m spammer 1.1.0 by bob                                                

  █▀ █▀█ ▄▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀█
  ▄█ █▀▀ █▀█ █░▀░█ █░▀░█ ██▄ █▀▄
  

    dont use this to annoy other people!!!!
  """)
  m = input("\033[1;50;40m message you wanna type is: ")
  s = input("\033[1;50;40m how fast do you want it to be?(example:1.0)")
  ss = int(input("\033[1;50;40m how much do you want to spam? ( 0 for infinite)"))
  plztype("""\033[1;50;40m oke , you have 10 seconds before spam starts , \n
  go and click on the text input (where you type)
  """)
  time.sleep(10)
  for i in range(int(ss)):
    pyautogui.write(m)
    time.sleep(float(s))
    pyautogui.press('enter')
 
  if ss == fuckyou:
    while True:
      pyautogui.write(m)
      time.sleep(float(s))
      pyautogui.press('enter')
except KeyboardInterrupt:
  print("\n \033[1;50;40m goodbye! have a great time! ")
