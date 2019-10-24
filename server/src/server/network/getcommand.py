import socket
import time
import threading
import function.move as move
import function.servo as servo
from rpi_ws281x import Color


step_set = 1
speed_set = 100
rad = 0.6


direction_command = 'no'
turn_command = 'no'

pos_input = 1
catch_input = 1
cir_input = 6





Y_pitch = 0
Y_pitch_MAX = 200
Y_pitch_MIN = -200

class Getcommand(threading.Thread):
    def __init__(self, Connexion, led_process):      # jusqua = donnée supplémentaire
        global LED
        threading.Thread.__init__(self)  # ne pas oublier cette ligne
        self.Connexion = Connexion
        LED = led_process
        # (appel au constructeur de la classe mère)




    def run(self):

        
        global direction_command, turn_command, pos_input, catch_input, cir_input, ultrasonicMode, FindLineMode, FindColorMode

        while True: 
            data = ''
            if self.Connexion.message is not None:
                data = self.Connexion.message
            if not data:
                continue
            elif '"forward"' == data:
                direction_command = 'forward'
                ws_R = 300
                ws_G = 0
                ws_B = 
                LED.colorWipe(Color(ws_R,ws_G,ws_B))
                move.move(speed_set, direction_command, turn_command, rad)
            elif '"backward"' == data:
                ws_R = 0
                ws_G = 0
                ws_B = 300
                LED.colorWipe(Color(ws_R,ws_G,ws_B))                
                direction_command = 'backward'
                move.move(speed_set, direction_command, turn_command, rad)
            elif '"DS"' in data:
                direction_command = 'no'
                move.move(speed_set, direction_command, turn_command, rad)

            elif '"left"' == data:
                turn_command = 'left'
                move.move(speed_set, direction_command, turn_command, rad)
            elif '"right"' == data:
                turn_command = 'right'
                move.move(speed_set, direction_command, turn_command, rad)
            elif '"TS"' in data:
                turn_command = 'no'
                move.move(speed_set, direction_command, turn_command, rad)

            elif '"out"' == data:
                if pos_input < 17:
                    pos_input+=1
                servo.hand_pos(pos_input)
            elif 'in' == data:
                if pos_input > 1:
                    pos_input-=1
                servo.hand_pos(pos_input)

            elif '"headup"' == data:
                servo.camera_ang('lookup',0)
            elif '"headdown"' == data:
                servo.camera_ang('lookdown',0)
            elif '"headhome"' == data:
                servo.camera_ang('home',0)
                servo.hand('in')
                servo.cir_pos(6)
                pos_input = 1
                catch_input = 1
                cir_input = 6
                servo.catch(catch_input)
                time.sleep(0.5)
                servo.clean_all()

            elif '"c_left"' == data:
                if cir_input < 12:
                    cir_input+=1
                servo.cir_pos(cir_input)
            elif '"c_right"' == data:
                if cir_input > 1:
                    cir_input-=1
                servo.cir_pos(cir_input)

            elif '"catch"' == data:
                if catch_input < 13:
                    catch_input+=1
                servo.catch(catch_input)
            elif '"loose"' == data:
                if catch_input > 1:
                    catch_input-=1
                servo.catch(catch_input)

            elif '"wsR"' in data:
                try:
                    set_R=data.split()
                    ws_R = int(set_R[1])
                    self.LED.colorWipe(Color(ws_R,ws_G,ws_B))
                except:
                    pass
            elif '"wsG"' in data:
                try:
                    set_G=data.split()
                    ws_G = int(set_G[1])
                    self.LED.colorWipe(Color(ws_R,ws_G,ws_B))
                except:
                    pass
            elif '"wsB"' in data:
                try:
                    set_B=data.split()
                    ws_B = int(set_B[1])
                    self.LED.colorWipe(Color(ws_R,ws_G,ws_B))
                except:
                    pass

            elif '"FindColor"' in data:
                FindColorMode = 0
                EtabliConnexion.send(self,('FindColor').encode())

            elif '"WatchDog"' in data:
                EtabliConnexion.send(self,('WatchDog').encode())

            elif '"steady"' in data:
                ultrasonicMode = 1
                EtabliConnexion.send(self,('steady').encode())

            elif '"FindLine"' in data:
                FindLineMode = 1
                EtabliConnexion.send(self,('FindLine').encode())

            elif '"funEnd"' in data:
                ultrasonicMode = 0
                FindLineMode   = 0
                FindColorMode  = 0
                EtabliConnexion.send(self,('FunEnd').encode())
                move.motorStop()

            else:
                pass