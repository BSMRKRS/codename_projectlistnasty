import socket, time, setup, RoboPiLib as RPL

def SocketReceive(HOST, PORT, command):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        s.send(command)
        reply = s.recv(64)
        return reply

arm0, arm1, arm2, arm3 = 1000

Pins = [0,1,2,3,16,17,18,19,20,21,22,23]
wheels = [16,17,18,19]
hand = [20,21,22,23]
arm = [0,1,2,3]
while True:
        for I in Pins:
                value = int(SocketReceive('192.168.21.142', 9999, str(I)))
                if I in arm:
                        if value >= 700:
                        		arm{}.format(I) += 10 
                                RPL.servoWrite(int(I + 8), arm{}.format(i))
                        if value <= 200:
                        		arm{}.format(I) -= 10 
                                RPL.servoWrite(int(I + 8), arm{}.format(i))

