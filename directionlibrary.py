#This is functions for speed
import RoboPiLib as RPL
import setup

def forward():
  RPL.servoWrite(1,1600)
  RPL.servoWrite(0,1400)

def left():
  RPL.servoWrite(1,1600)
  RPL.servoWrite(0,1500)

def right():
  RPL.servoWrite(1,1500)
  RPL.servoWrite(0,1400)

def backward():
  RPL.servoWrite(1,1400)
  RPL.servoWrite(0,1600)

def stop():
  RPL.servoWrite(0,0)
  RPL.servoWrite(1,0)
