import sys, tty, termios, signal

def interrupted(signum,frame):
    print("Interrupted")


old_settings = termios.tcgetattr(sys.stdin.fileno()) #records current terminal settings
signal.signal(signal.SIGALRM, interrupted) #calls interrupted when alarm stops
tty.setraw(sys.stdin.fileno()) #raw keystroke input, changes terminal settings
print "PRESS Q TO QUIT"
while True:
  signal.setitimer(signal.ITIMER_REAL,0.255) #starts alarm for 0.255 seconds
  ch = sys.stdin.read(1) #saves one keystroke as variable
  signal.setitimer(signal.ITIMER_REAL,0) #resets alarm and ch variable
  if ch == 'q': #press q to quit
    termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings) #Changes the terminal settings back to what they were before
    break
  elif ch == 'w': #press w to go forward
    print "pressed w"
  elif ch == 's': #press s to go backward
    print "pressed s"
