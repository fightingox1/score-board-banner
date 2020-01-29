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
t1 = Thread(target = updatescore)
t2 = Thread(target = countscore)
t1.start()
sleep(1)
t2.start()
def countscore():
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
def updatescore():
  update = "true"
  while update == "true":
    score = score1
    while score == 0:
      top.on()
      bottom.on()
      righttop.on()
      rightbottom.on()
      topleft.on()
      bottomleft.on()
      sleep(1)
      top.off()
      bottom.off()
      righttop.off()
      rightbottom.off()
      topleft.off()
      bottomleft.off()
      sleep(1)
    while score == 1:
      righttop.on()
      rightbottom.on
      sleep(1)
      rightbottom.off()
      righttop.off()
      sleep(1)
    while score == 2:
      top.on()
      righttop.on()
      middle.on()
      bottomleft.on()
      bottom.on()
      sleep(1)
      righttop.off()
      top.off()
      middle.off()
      bottomleft.on()
      bottom.off()
      sleep(1)
    while score ==  3:
      top.on()
      righttop.on()
      rightbottom.on()
      middle.on()
      bottom.on()
      sleep(1)
      top.off()
      rightbottom.off()
      middle.off()
      bottom.off()
      sleep(1)
    while score == 4:
      righttop.on()
      rightbottom.on()
      middle.on()
      topleft.on()
      sleep(1)
      righttop.off()
      rightbottom.off()
      middle.off()
      topleft.off()
      sleep(1)
    while score == 5:
      top.on()
      topleft.on()
      middle.on()
      rightbottom.on()
      bottom.on()
      sleep(1)
      top.off()
      topleft.off()
      middle.off()
      rightbottom.off()
      bottom.off()
      sleep(1)
    while score == 6:
      topleft.on()
      bottomleft.on()
      bottom.on()
      rightbottom.on()
      middle.on()
      sleep(1)
      topleft.off()
      bottomlet.off()
      bottom.off()
      rightbottom.off()
      middle.off()
      sleep(1)
    while score == 7:
      top.on()
      righttop.on()
      rightbottom.on()
      sleep(1)
      top.off()
      righttop.off()
      rightbottom.off()
      sleep(1)
    while score == 8:
      top.on()
      righttop.on()
      topleft.on()
      rightbottom.on()
      bottomleft.on()
      middle.on()
      bottom.on()
      sleep(1)
      top.off()
      righttop.off()
      topleft.off()
      rightbottom.off()
      bottomleft.off()
      middle.off()
      bottom.off()
      sleep(1)
    while score == 9:
      middle.on()
      topleft.on()
      top.on()
      righttop.on()
      rightbottom.on()
      sleep(1)
      rightbottom.off()
      righttop.off()
      top.off()
      topleft.off()
      middle.off
      sleep(1)







