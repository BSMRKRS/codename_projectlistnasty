import socket, time, setup, RoboPiLib as RPL

def SocketReceive(HOST, PORT, command):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        s.send(command)
        reply = s.recv(64)
        return reply

arm1, arm2, arm3 = 1000, 1000, 1000
Pins = [0,1,2,3,16,17,18,19,20,21,22,23]
wheels = [16,17,18,19]
hand = [20,21,22,23]
arm = [1,2,3]
base = [0]
armPos = 1000
for x in arm:
	RPL.servoWrite(int(x + 8), 1000)
while True:
        for I in Pins:
                value = int(SocketReceive('192.168.21.142', 9999, str(I)))
                print (I, value)
                if I in base:
                        if value >= 700:
                                RPL.servoWrite(int(I + 8), 1600)
                        elif value <= 200:
                                RPL.servoWrite(int(I + 8), 1400)
                        else:
                        		RPL.servoWrite(int(I + 8), 0)
                if I in arm:
                        if value >= 700 and vars()['arm{}'.format(I)] <= 3000:
                        		vars()['arm{}'.format(I)] += 60 
                         		RPL.servoWrite(int(I + 8), vars()['arm{}'.format(I)])
                        if value <= 200 and vars()['arm{}'.format(I)] >= 61:
                        		vars()['arm{}'.format(I)] -= 60 
	                            	RPL.servoWrite(int(I + 8), vars()['arm{}'.format(I)])
                if I in hand:
               		if I == 21 and value == 0 and armPos <= 1440:
               			armPos += 60
               			RPL.servoWrite(13, armPos)
			if I == 22 and value == 0:
				 RPL.servoWrite(12, 1300)
			elif I == 20 and value == 0:
				RPL.servoWrite(12, 1700)
			else:
				RPL.servoWrite(12,0)
               		if I == 23 and value == 0 and armPos >= 1060:
               			armPos -= 60
               			RPL.servoWrite(13, armPos) 
