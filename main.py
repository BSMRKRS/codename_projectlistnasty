#import co2
import directionlibrary as dl
#This function runs on startup and cleans up or starts anything you might need
def initialize():
  dl.STOP()


def main(*debug): #use main(True) to display sensor readings
    while True:
        dl.autonomy()
        #co2.detectHuman()
        if debug == (True,):
            print(dl.values())
initialize()
main()
