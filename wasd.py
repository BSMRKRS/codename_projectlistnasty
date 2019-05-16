import sys,tty,termios,signal
import directionlibrary as dl
import RoboPiLib as RPL
###
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

def interrupted(signum, frame):
  dl.stopAll()

signal.signal(signal.SIGALRM, interrupted)
tty.setraw(sys.stdin.fileno())

while True:
  signal.setitimer(signal.ITIMER_REAL,0.255)
  ch = sys.stdin.read(1)
  signal.setitimer(signal.ITIMER_REAL,0)
  if ch == 'q':
    termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
    break
  elif ch == 'w':
    RPL.servoWrite(0,1300)
    #RPL.servoWrite(0,700)
  elif ch == 's':
    RPL.servoWrite(0,1700)
    #RPL.servoWrite(0,2200)
  elif ch == 'a':
    dl.left()
  elif ch == 'd':
    dl.right()
