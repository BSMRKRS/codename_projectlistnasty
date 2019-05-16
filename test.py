import time
import directionlibrary as dl

#while True:
  #print dl.values()

dl.RIGHT()
init = time.time()
try:
  while True:
    pass
except:
  print time.time() - init
  dl.STOP()

#for degree in range(0,180,10):
 # print degree
  #dl.turn("right",degree,"STOP")
  #time.sleep(1)
