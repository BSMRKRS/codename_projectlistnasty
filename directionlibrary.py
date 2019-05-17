import RoboPiLib as RPL
import setup, time

def values():
  global frontright,frontmiddle,frontleft,right,left,back
  right = RPL.analogRead(5)
  back = RPL.digitalRead(17)
  frontright = RPL.digitalRead(20)
  left = RPL.analogRead(6)
  frontmiddle = RPL.digitalRead(19)
  frontleft = RPL.digitalRead(18)
  return "front right = %s\nfront middle = %s\nfront left = %s\nright = %s\nleft = %s\nback = %s" % (frontright,frontmiddle,frontleft,right,left,back)

def FORWARD():
  RPL.servoWrite(0,1590)
  RPL.servoWrite(1,1410)
  RPL.servoWrite(2,1590)
  RPL.servoWrite(3,1410)
def BACKWARD():
  RPL.servoWrite(0,1410)
  RPL.servoWrite(1,1590)
  RPL.servoWrite(2,1410)
  RPL.servoWrite(3,1590)
def RIGHT():
  RPL.servoWrite(0,1410)
  RPL.servoWrite(1,1410)
  RPL.servoWrite(2,1410)
  RPL.servoWrite(3,1410)
def LEFT():
  RPL.servoWrite(0,1590)
  RPL.servoWrite(1,1590)
  RPL.servoWrite(2,1590)
  RPL.servoWrite(3,1590)
def STOP():
  for x in range(0,4):
    RPL.servoWrite(x,0)
def turn(direction,degree,*optional):
  if direction == "right":
    RIGHT()
  elif direction == "left":
    LEFT()
  else:
    print "please specify right or left"
    exit()
  pause = 0.021111 * degree + 0.0000000001
  time.sleep(pause)
  if optional == ("STOP",):
    STOP()
def turntowall():
  rightloop = False
  leftloop = False
  if frontright == 0:
    RIGHT()
    rightloop = True
  elif frontleft == 0:
    LEFT()
    leftloop = True
  else:
    rightloop = False
    leftloop = False
  while rightloop:
    values()
    if left > 450:
      time.sleep(0.5)
      rightloop = False
  while leftloop:
    values()
    if right > 500:
      time.sleep(0.5)
      leftloop = False

def reverse():
  STOP()
  time.sleep(1)
  BACKWARD()
  loop = True
  while loop:
    values()
    if back == 0:
      STOP()
      print "human input required"
      exit()
    elif left < 420:
      time.sleep(1.0)
      turn("left",90)
      loop = False
    elif right < 420:
      time.sleep(1.0)
      turn("right",90)
      loop = False
  FORWARD()
  time.sleep(1)

def autonomy():
  values()
  #if frontright == 0 or frontleft == 0:
    #turntowall()
  if frontright == 0 or frontleft == 0:
    if frontright == 0:
      turn("right",30)
    elif frontleft == 0:
      turn("left",30)
      time.sleep(0.3)
  elif frontmiddle == 1:
    FORWARD()
  elif left < 420  or right < 430:
    if right < 420:
      turn("right",90)
    elif left < 420:
      turn("left",90)
  else:
    reverse()
