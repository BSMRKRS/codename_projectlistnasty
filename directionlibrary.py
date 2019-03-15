import RoboPiLib as RPL
import setup

def left():
  RPL.servoWrite(15,800)
def right():
  RPL.servoWrite(15,2000)
def straight():
  RPL.servoWrite(15,1450)
def stop():
  RPL.servoWrite(0,0)
  RPL.servoWrite(1,0)

def stopAll():
  stop()
  straight()
