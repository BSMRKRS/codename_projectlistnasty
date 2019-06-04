import RoboPiLib as RPL
import setup, time

def values():
  global left,right,leftwheel,rightwheel,frontleft,frontright,top
  left = RPL.analogRead(0)
  leftwheel = RPL.analogRead(1)
  frontleft = RPL.analogRead(2)
  top = RPL.analogRead(3)
  frontright = RPL.analogRead(4)
  rightwheel = RPL.analogRead(5)
  right = RPL.analogRead(6)
  return "Top: %s\nFront left: %s\nFront right: %s\n\nLeft: %s\nRight: %s\n\nRight wheel: %s\nLeft wheel: %s" % (top,frontleft,frontright,left,right,rightwheel,leftwheel)

################
###Directions###
################
def FORWARD():
  RPL.servoWrite(8,1410)
  RPL.servoWrite(9,1590)
  RPL.servoWrite(10,1410)
  RPL.servoWrite(11,1590)
def BACKWARD():
  RPL.servoWrite(8,1590)
  RPL.servoWrite(9,1410)
  RPL.servoWrite(10,1590)
  RPL.servoWrite(11,1410)
def RIGHT():
  RPL.servoWrite(8,1410)
  RPL.servoWrite(9,1410)
  RPL.servoWrite(10,1410)
  RPL.servoWrite(11,1410)
def LEFT():
  RPL.servoWrite(8,1590)
  RPL.servoWrite(9,1590)
  RPL.servoWrite(10,1590)
  RPL.servoWrite(11,1590)
def STOP():
  for x in range(8,12):
    RPL.servoWrite(x,0)
##########################

###################
###Turn to angle###
###################
def turn(direction,degree,*optional):
  if direction == "right":
    RIGHT()
  elif direction == "left":
    LEFT()
  else:
    print "please specify right or left"
    exit()
  pause = 0.022 * degree
  time.sleep(pause)
  if optional == ("STOP",):
    STOP()
#######################

##################
###TURN TO WALL###
##################
#This code is not being used currently
def turntowall():
  rightloop = False
  leftloop = False
  if frontright >= 370:
    LEFT()
    rightloop = True
  elif frontleft >= 430:
    RIGHT()
    leftloop = True
  else:
    rightloop = False
    leftloop = False
  while rightloop:
    values()
    if right > 450:
      time.sleep(0.5)
      rightloop = False
  while leftloop:
    values()
    if left > 500:
      time.sleep(0.5)
      leftloop = False
######################

#############
###REVERSE###
#############
def reverse():
  BACKWARD()
  loop = True
  while loop:
    values()
    if left < 420:
      time.sleep(1.0)
      turn("left",90)
      loop = False
    elif right < 420:
      time.sleep(1.0)
      turn("right",90)
      loop = False
###################

###################
###MAIN FUNCTION###
###################
def autonomy():
    values()
    if frontright >= 450 or frontleft >= 430:
        if frontright >= 450:
            turn("left",10)
        elif frontleft >= 430:
            turn("right",10)
    elif top <= 250:
        FORWARD()
    elif left > 400 and right > 450:
        reverse()
    elif left > 400:
        turn("right",45)
    elif right > 450:
        turn("left",45)
