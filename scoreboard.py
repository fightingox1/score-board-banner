import time
score1 = 0
score2 = 0
tenthup = "false"
loop = "true"
while loop == "true":
  count = "true"
  while count == "true":
    if tenthup == "true":
      if score2 == 9:
        score2 = 0
        score1 = 0
      else:
        score1 = 0
        score2 = score2 + 1
      tenthup = "false"
    score1 = score1 + 1
    if score1 == 9:
      tenthup = "true"
    time.sleep(1)
    count = "true"
    
    
    
