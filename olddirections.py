import RoboPiLib as RPL
import setup, time

def values():
  global frontright,frontmiddle,frontleft,right,left,back
  #Digital and analog readings
  #THESE NEED TO BE UPDATED CONSTANTLY
  right = RPL.analogRead(5)
  back = RPL.digitalRead(17)
  frontright = RPL.digitalRead(20)
  left = RPL.analogRead(6)
  #frontmiddle = RPL.digitalRead(19)
  frontmiddle = RPL.analogRead(7)
  frontleft = RPL.digitalRead(18)
  #print(values) to debug readings
  return "front right = %s\nfront middle = %s\nfront left = %s\nright = %s\nleft = %s\nback = %s" % (frontright,frontmiddle,frontleft,right,left,back)


################
###Directions###
################
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
#############################

#turn the robot a specific degree amount
#example: turn("left",90)
#to stop the robot after the turn is complete use:
#turn("left",90,"STOP")
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

#This function checks to see if there is any space available to turn
#If no wall is found, the robot will turn until the analog sensor detects a specific distance
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


#This function is used for when the robot gets stuck in a box
#The robot will go backwards until it finds an opening to continue
def reverse():
  STOP()
  time.sleep(1)
  BACKWARD()
  loop = True
  while loop:
    values()
    if back == 0: #If the robot has boxed itself completely in
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
  time.sleep(1) #maybe make this shorter, idk

#####################
###AUTONOMOUS CODE###
#####################
def autonomy():
  values()
  #if frontright == 0 or frontleft == 0:
    #turntowall() #This code may or may not be used in Mk. 3
  if frontright == 0 or frontleft == 0: #1
    if frontright == 0:
      turn("left",20)
    elif frontleft == 0:
      turn("right",20)
      time.sleep(0.3)
  elif frontmiddle <= 250: #2
    FORWARD()
  elif left < 420  or right < 430: #3
    if right < 420:
      turn("right",90)
    elif left < 420:
      turn("left",90)
  else:
    reverse() #4
#Progression
"""
1: detect side wall(if the robot is going to come up on the wall at an angle)
  - turn a small distance and slowly the robot will correct itself to being parallel to the wall
2: detect wall directly infront
3: detect walls on either side
  -first check right side, if open, turn right
  -If right side has a wall, check left, turn left
4: if walls infront and on sides, go backwards
  -If the robot has boxed it self in, it will go backwards until it finds an opening
"""
