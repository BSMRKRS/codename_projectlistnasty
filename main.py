import directionlibrary as dl

def initialize():
  dl.STOP()
  #co2 here

def main(*debug):
  try:
    while True:
      dl.autonomy()
      if debug == (True,):
        print(dl.values())
  except KeyboardInterrupt:
    wasd()

def wasd():
  while True:
    userinput = raw_input("Taking keystroke input\n")
    if userinput == "return":
      main()

initialize()
main()
