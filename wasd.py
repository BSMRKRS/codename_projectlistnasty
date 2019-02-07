#Run this 

import time
import RoboPiLib as RPL
import setup
import curses
import directionlibrary as dl


#These are for keyboard control
screen = curses.initscr()
#curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
  while True:
    char = screen.getch()
    if char == 42:
      dl.stop()
      break
    elif char == 119:
      dl.forward()
      char = False
    elif char == 115:
      dl.backward()
      char = False
    elif char == 97:
      dl.left()
      char = False
    elif char == 100:
      dl.right()
      char = False
    else:
      dl.stop()
finally:
  curses.nocbreak()
  screen.keypad(0)
  curses.echo()
  curses.endwin()
