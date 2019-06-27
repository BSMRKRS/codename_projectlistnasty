import RoboPiLib as RPL
import setup, time
import sys, tty, termios, signal
d1 = 1000
d2 = 3000
def interrupted(signum,frame):
    print("Interrupted")
#SYNCHRONIZE
pos7 = int(1000)
pos6 = int(1000)
pos5 = int(1000)
pos4 = int(1000)

RPL.servoWrite(12,1000)
RPL.servoWrite(11,1000)
RPL.servoWrite(10,1000)
RPL.servoWrite(9,1000)
print "synchronized"

#STANDARD SERVOS 
def regulate(pin):
  if pin > 3000:
    pin = 3000
  if pin < 0:
    pin = 10
  print str(pin)
  return pin

time.sleep(2)
old_settings = termios.tcgetattr(sys.stdin.fileno()) #records current terminal settings
signal.signal(signal.SIGALRM, interrupted) #calls interrupted when alarm stops
tty.setraw(sys.stdin.fileno()) #raw keystroke input, changes terminal settings
print "PRESS Q TO QUIT"
print "DON'T HOLD DOWN A BUTTON OR IT WILL BUFFER A BUNCH OF COMMANDS"

#LOOP
while True:
  signal.setitimer(signal.ITIMER_REAL,0.255) #starts alarm for 0.255 seconds
  ch = sys.stdin.read(1) #saves one keystroke as variable
  signal.setitimer(signal.ITIMER_REAL,0) #resets alarm and ch variable
  if ch == 'q': #press q to quit
    termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings) #Changes the terminal settings back to what they were before
    break

#HAND
  elif ch == 't':
    print "pressed t"
    pos7 -= 10
  elif ch == 'g':
    print "pressed g"
    pos7 += 10

#BASE
  elif ch == 'y':
    print "pressed y"
    pos6 +=10
  elif ch == 'h':
    print "pressed h"
    pos6 -=10

#JOINT 1
  elif ch == 'u':
    print "pressed u"
    pos5 -=10
  elif ch == 'j':
    print "pressed j"
    pos5 +=10

#JOINT 2
  elif ch == 'i':
    print "pressed i"
    pos4 +=10
  elif ch == 'k':
    print "pressed k"
    pos4 -=10

#ROTATE HAND
  elif ch == 'o':
    print "pressed o"
    RPL.servoWrite(8,d1)
  elif ch == 'l':
    print "pressed l"
    RPL.servoWrite(8,d2)

  RPL.servoWrite(8,0)
  if pos7 >1500:
    pos7 = 1500
  if pos7 <1000:
    pos7 = 1000
  print str(pos7)
  RPL.servoWrite(12,pos7)
  print "Pin 6"
  RPL.servoWrite(11,regulate(pos6))
  print "Pin 5"
  RPL.servoWrite(10,regulate(pos5))
  print "Pin 4"
  RPL.servoWrite(9,regulate(pos4))

