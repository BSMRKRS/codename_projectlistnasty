#This is functions for speed
import RoboPiLib as RPL
import setup

def f():
  RPL.servoWrite(1,1600)
  RPL.servoWrite(0,1400)

def l():
  RPL.servoWrite(1,1600)
  RPL.servoWrite(0,1500)

def r():
  RPL.servoWrite(1,1500)
  RPL.servoWrite(0,1400)

def b():
  RPL.servoWrite(1,1400)
  RPL.servoWrite(0,1600)

def stop():
  RPL.servoWrite(0,0)
  RPL.servoWrite(1,0)
