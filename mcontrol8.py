import socket, time, setup, RoboPiLib as RPL
from directionlibrary import *

def SocketReceive(HOST, PORT, command):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        s.send(command)
        reply = s.recv(64)
        return reply


#Initial starting values for motors in arm
#arm1, arm2, arm3 = 1000, 1000, 1000
armState = [1000,1000,1000]

#Defining all the pins used for the sensors for each part of the robot and overall
Pins = [0,1,2,3,16,17,18,19,20,21,22,23]
wheels = [16,17,18,19]
hand = [20,21,22,23]
arm = [1,2,3]
base = [0]

#Initial starting value for grabber motor
grabberState = 1000

#set arm motors to starting position on script start 
for initial in arm:
  RPL.servoWrite(int(initial + 8), armState[initial-1])

while True:
        #Cycles through each of the pins being used (as defined above) 
        for I in Pins:

          #Makes request to the server pi (at ip '192.168.21.142' on port 9999) for the sensor reading of current pin (I)
          value = int(SocketReceive('192.168.21.142', 9999, str(I)))

          #Debugging what each pin's sensor value is returning
          print (I, value)

          #if current pin is for base
          if I in base:
            if value >= 800:
              RPL.servoWrite(int(I + 8), 1550)
            elif value <= 200:
              RPL.servoWrite(int(I + 8), 1450)
            else:
              RPL.servoWrite(int(I + 8), 0)

          #if current pin is for arm                            
          if I in arm:
            if value >= 700 and armState[I-1] <= 3000:
              armState[I-1] += 60
            if value <= 200 and armState[I-1] >= 61:
              armState[I-1] -= 60
            RPL.servoWrite(int(I + 8), armState[I-1])

          #if current pin is for hand/wrist on arm
          if I in hand:
            if I == 21 and value == 0 and grabberState <= 1470:
         	grabberState += 30
        	RPL.servoWrite(13, grabberState) 
            if I == 23 and value == 0 and grabberState >= 1030:
         	grabberState -= 30
         	RPL.servoWrite(13, grabberState)
            if I == 20 and value == 0:
              RPL.servoWrite(12, 1550)
            elif I == 22 and value == 0:
              RPL.servoWrite(12,1450)
            else:
              RPL.servoWrite(12, 0)








