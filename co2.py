import RoboPiLib as RPL
import setup,time

print "Initializing co2 sensor"
readings = []
for x in range(0,20):
  readings.append(RPL.analogRead(6))
  #time.sleep(0.5)
  time.sleep(0.2)
print "Initialized"

while True:
  average = sum(readings) / len(readings)
  co2 = RPL.analogRead(6)
  if average - co2 >= 20:
    print "Human Dectected"
  else:
    pass
  readings.pop(0)
  readings.append(co2)
  print "Average: %s \nCO2: %s \nDifference: %s" % (average,co2,average-co2)
  time.sleep(0.5)
