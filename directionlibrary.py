#This is functions for speed
import RoboPiLib as RPL
import setup

def forward(speed):
  RPL.servoWrite(1,speed[1])
  RPL.servoWrite(0,speed[0])

def left(speed):
  RPL.servoWrite(1,speed[1])
  RPL.servoWrite(0,speed[0])

def right(speed):
  RPL.servoWrite(1,speed[1])
  RPL.servoWrite(0,speed[0])

def backward(speed):
  RPL.servoWrite(1,speed[1])
  RPL.servoWrite(0,speed[0])

def stop():
  RPL.servoWrite(0,0)
  RPL.servoWrite(1,0)

def slowspeed():
  return 1490,1510

def mediumspeed():
  return 1450,1550

def highspeed():
  return 1400,1600
