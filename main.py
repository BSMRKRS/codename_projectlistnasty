import directionlibrary as dl


#This function runs on startup and cleans up or starts anything you might need
def initialize():
  dl.STOP()
  #co2 here

def main(*debug): #use main(True) to display sensor readings
  try:
    while True:
      dl.autonomy() #run autonomy functions
      if debug == (True,):
        print(dl.values())
  except KeyboardInterrupt:
    wasd()

def wasd():
  dl.STOP()
  while True:
    userinput = raw_input("Taking keystroke input\n")
    if userinput == "return":
      main()

initialize()
main()
