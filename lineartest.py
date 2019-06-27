import RoboPiLib as RPL
import setup, time
RPL.servoWrite(7,2000)
print RPL.analogRead(7)
time.sleep(5)
RPL.servoWrite(7,1000)
print RPL.analogRead(7)
time.sleep(5)
use = 5
while use != 666:
	use = input("How far?")
	use = int(use)
	print str(use)
	RPL.servoWrite(6,use)
