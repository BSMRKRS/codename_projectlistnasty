import RoboPiLib as RPL
import setup,time
def init():
  print "Initializing co2 sensor"
  co2readings = []
  for x in range(0,20):
    co2readings.append(RPL.analogRead(4))
    time.sleep(0.05)
  print "Initialized"
  return co2readings


def detectHuman():
  average = sum(co2Readings) / len(co2Readings)
  co2 = RPL.analogRead(4)
  if average - co2 >= 20:
    print "Human Dectected"
  else:
    pass
  co2Readings.pop(0)
  co2Readings.append(co2)
#  print "Average: %s \nCO2: %s \nDifference: %s" % (average,co2,average-co2)

co2Readings = init()
#while True:
  #detectHuman()
