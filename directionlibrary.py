import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

def left():
  RPL.servoWrite(15,1000)
def right():
  RPL.servoWrite(15,1800)
def straight():
  RPL.servoWrite(15,1450)
def stop():
  RPL.servoWrite(0,1500)

def stopAll():
  stop()
  straight()
