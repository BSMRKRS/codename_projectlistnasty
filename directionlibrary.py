import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import sys, tty, termios, signal

######################
## Motor Establishment
######################

motorL = 0
motorR = 1

motorR_forward = 2000
motorR_backward = 1000
motorL_forward = 1000
motorL_backward = 2000

try:
  RPL.pinMode(motorL,RPL.SERVO)
  RPL.servoWrite(motorL,1500)
  RPL.pinMode(motorR,RPL.SERVO)
  RPL.servoWrite(motorR,1500)
except:
  pass

######################
## Individual commands
######################
def stopAll():
  try:
    RPL.servoWrite(motorL,1500)
    RPL.servoWrite(motorR,1500)
  except:
    print "error except"
    pass

def forward():
  RPL.servoWrite(motorL,motorL_forward)
  RPL.servoWrite(motorR,motorR_forward)

def reverse():
  RPL.servoWrite(motorL,motorL_backward)
  RPL.servoWrite(motorR,motorR_backward)

def right():
  RPL.servoWrite(motorL,1460)#motorL_forward)
  RPL.servoWrite(motorR,1460)#motorR_backward)

def left():
  RPL.servoWrite(motorL,1540)#motorL_backward)
  RPL.servoWrite(motorR,1540)#motorR_forward)

def forward_right():
  RPL.servoWrite(motorL,motorL_forward)
  RPL.servoWrite(motorR,1500)

def forward_left():
  RPL.servoWrite(motorL,1500)
  RPL.servoWrite(motorR,motorR_forward)

def backward_right():
  RPL.servoWrite(motorL,1500)
  RPL.servoWrite(motorR,motorR_backward)

def backward_left():
  RPL.servoWrite(motorL,motorL_backward)
  RPL.servoWrite(motorR,1500)

def print_speed():
  print '--FORWARD: Left Motor: ', motorL_forward, ' Right Motor: ', motorR_forward, '\r'
  print '  BACKWARD: Left Motor: ', motorR_backward, ' Right Motor: ', motorL_backward, '\r'

def forwardSpeedChanges(change, mn = 1600, mx = 2900):
  global motorR_forward
  global motorL_forward
  motorR_forward += change
  motorL_forward += change
  motorR_forward = max(min(motorR_forward, mx), mn)
  motorL_forward = max(min(motorL_forward, mx), mn)
  print_speed()

def backwardSpeedChanges(change, mn = 100, mx = 1400):
  global motorR_backward
  global motorL_backward
  motorR_backward += change
  motorL_backward += change
  motorR_backward = max(min(motorR_backward, mx), mn)
  motorL_backward = max(min(motorL_backward, mx), mn)
  print_speed()

def backwardRightSpeedChange(change, mn = 100, mx = 1400):
  global motorR_backward
  motorR_backward += change
  motorR_backward = max(min(motorR_backward, mx), mn)
  print_speed()

def backwardLeftSpeedChange(change, mn = 100, mx = 1400):
  global motorL_backward
  motorL_backward += change
  motorL_backward = max(min(motorL_backward, mx), mn)
  print_speed()

def forwardRightSpeedChange(change, mn = 1600, mx = 2900):
  global motorR_forward
  motorR_forward += change
  motorR_forward = max(min(motorR_forward, mx), mn)
  print_speed()

def forwardLeftSpeedChange(change, mn = 1600, mx = 2900):
  global motorL_forward
  motorL_forward += change
  motorL_forward = max(min(motorL_forward, mx), mn)
  print_speed()