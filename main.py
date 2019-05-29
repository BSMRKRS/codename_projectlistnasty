import directionlibrary as dl
import color,co2


#This function runs on startup and cleans up or starts anything you might need
def initialize():
  dl.STOP()

def main(*debug): #use main(True) to display sensor readings
  try:
    while True:
      print color.color() #prints the colors lmao
      co2.detectHuman()
      dl.autonomy() #run autonomy functions
      if debug == (True,):
        print(dl.values())
  except KeyboardInterrupt:
    wasd()

def wasd(): #This is still a work in progress
  dl.STOP()
  while True:
    userinput = raw_input("Taking keystroke input\n")
    if userinput == "return":
      main()

initialize()
main()
