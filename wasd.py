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

speed = dl.slowspeed() #setting the speed to be slow

try:
  while True:
    char = screen.getch()
    if char == 42:
      dl.stop()
      break
    elif char == 119:
      dl.forward(speed)
    elif char == 115:
      dl.backward(speed)
    elif char == 97:
      dl.left(speed)
    elif char == 100:
      dl.right(speed)
    elif char == 48:
      dl.stop()
      print 'speed set to OFF'
    elif char == 49:
      speed = dl.slowspeed()
      print 'speed set to SLOW'
    elif char == 50:
      speed = dl.mediumspeed()
      print 'speed set to MEDIUM'
    elif char == 51:
      speed = dl.highspeed()
      print 'speed set to HIGH'
    else:
      print 'Sorry, that command is not recognized'
finally:
  curses.nocbreak()
  screen.keypad(0)
  curses.echo()
  curses.endwin()
