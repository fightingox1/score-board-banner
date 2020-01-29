from time import sleep
from gpiozero import LED, Button
from threading import Thread
top = LED(2)
righttop = LED(3)
rightbottom = LED(4)
bottom = LED(14)
middle = LED(15)
bottomleft = LED(18)
topleft = LED(16)
score1 = 0
score2 = 0
tenthup = "false"
  loop = "true"
  while loop == "true":
    count = "true"
    while count == "true":
      if tenthup == "true":
        score1 = 0
        tenthup = "false"
      score1 = score1 + 1
      if score1 == 9:
        tenthup = "true"
      time.sleep(1.5)
      count = "true"
