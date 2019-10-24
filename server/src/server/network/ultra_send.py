from .connect import EtabliConnexion
import socket 
import time
ultrasonicMode = 0


class ultra_send_client():
    def ultra_send_client(self):
        Connexion = EtabliConnexion.connect(self)

        ultra_IP = Connexion.addr[0]
        ultra_PORT = 2257   #Define port serial 
        ultra_ADDR = (ultra_IP, ultra_PORT)
        ultra_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Set connection value for socket
        ultra_Socket.connect(ultra_ADDR)
        print(ultra_ADDR)
        while 1:
            while ultrasonicMode:
                try:
                    ultra_Socket.send(str(round(ultra.checkdist(),2)).encode())
                    time.sleep(0.5)
                    continue
                except:
                    pass
            time.sleep(0.5)