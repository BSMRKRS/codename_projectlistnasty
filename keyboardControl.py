
import sys, tty, termios, signal
import directionlibrary as dl


######################################
## Other motor commands should go here
######################################

def stopAll():
  try:
    RPL.servoWrite(motorL,1500)
    RPL.servoWrite(motorR,1500)
  except:
    print "error except"
    pass

def interrupted(signum, frame): # this is the method called at the end of the alarm
  dl.stopAll()



print "Ready To Drive! Press * to quit.\r"
## the SHORT_TIMEOUT needs to be greater than the press delay on your keyboard
## on your computer, set the delay to 250 ms with `xset r rate 250 20`

def keyboardControl():
  fd = sys.stdin.fileno() # I don't know what this does
  old_settings = termios.tcgetattr(fd) # this records the existing console settings that are later changed with the tty.setraw... line so that they can be replaced when the loop ends

  signal.signal(signal.SIGALRM, interrupted) # this calls the 'interrupted' method when the alarm goes off
  tty.setraw(sys.stdin.fileno()) # this sets the style of the input
  SHORT_TIMEOUT = 0.255 # number of seconds your want for timeout

  while True:
    signal.setitimer(signal.ITIMER_REAL,SHORT_TIMEOUT) # this sets the alarm
    ch = sys.stdin.read(1) # this reads one character of input without requiring an enter keypress
    signal.setitimer(signal.ITIMER_REAL,0) # this turns off the alarm
    if ch == '*': # pressing the asterisk key kills the process
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # this resets the console settings
      break # this ends the loop
    else:
      if ch == 'w':
        dl.forward()
      elif ch == "a":
        dl.left()
      elif ch == "s":
        dl.reverse()
      elif ch == "d":
        dl.right()
      elif ch == "e":
        dl.forward_right()
      elif ch == "q":
        dl.forward_left()
      elif ch == "z":
        dl.backward_left()
      elif ch == "c":
        dl.backward_right()
      elif ch == "]":
       dl.forwardSpeedChanges(100)
      elif ch == "[":
        dl.backwardSpeedChanges(-100)
      elif ch == "}":
        dl.forwardSpeedChanges(-100)
      elif ch == "{":
        dl.backwardSpeedChanges(100)
      elif ch == "1":
        dl.forwardLeftSpeedChange(100)
      elif ch == "!":
        dl.forwardLeftSpeedChange(-100)
      elif ch == "2":
        dl.forwardRightSpeedChange(100)
      elif ch == "@":
        dl.forwardRightSpeedChange(-100)
      elif ch == "3":
        dl.backwardLeftSpeedChange(-100)
      elif ch == "#":
        dl.backwardLeftSpeedChange(100)
      elif ch == "4":
        dl.backwardRightSpeedChange(-100)
      elif ch == "$":
        dl.backwardRightSpeedChange(100)