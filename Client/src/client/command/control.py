import threading, time
import queue
from network.send_mqtt import build_payload
flags = 0

class control_process():

        def __init__(self, mqtt_client):      # jusqua = donnée supplémentaire
                global client, topic, flags , Queue_control
                flags = 0

                client = mqtt_client
                Queue_control = queue.Queue() #initialises a first in first out queue
                topic ="channels/2bc073e6-a43b-4864-a9db-956a9281ad5e/messages"


        # (appel au constructeur de la classe mère)
        def set_R(self):
                time.sleep(0.03)
                build_payload(client,topic, Queue_control,Queue_control,('wsR %s'%var_R.get()))


        def set_G(self):
                time.sleep(0.03)
                build_payload(client,topic, Queue_control,('wsG %s'%var_G.get()))


        def set_B(self):
                time.sleep(0.03)
                build_payload(client,topic, Queue_control,('wsB %s'%var_B.get()))



        def call_forward(self):         #When this function is called,client commands the car to move forward
                up = "forward"
                time.sleep(0.03)
                build_payload(client,topic, Queue_control, up)
                
        def call_back(self):            #When this function is called,client commands the car to move backward
                down = "backward"
                time.sleep(0.03)
                build_payload(client,topic, Queue_control, down)


        def call_FB_stop(self):            #When this function is called,client commands the car to stop moving
                ds ="DS"
                time.sleep(0.03)

                build_payload(client,topic, Queue_control,ds)

        def call_Turn_stop(self):            #When this function is called,client commands the car to stop moving
                ts = "TS"
                build_payload(client,topic, Queue_control,ts)


        def call_Left(self):            #When this function is called,client commands the car to turn left
                left = "left"
                build_payload(client, topic , Queue_control, left)


        def call_Right(self):           #When this function is called,client commands the car to turn right
                build_payload(client,topic, Queue_control,"right")


        def call_LeftSide(self):
                build_payload(client,topic, Queue_control,"out")


        def call_RightSide(self):
                build_payload(client,topic, Queue_control,"in")


        def call_CLeft(self):
                build_payload(client,topic, Queue_control,"c_left")


        def call_CRight(self):
                build_payload(client,topic, Queue_control,"c_right")


        def call_headup(self,event):
                build_payload(client,topic, Queue_control,"headup")


        def call_headdown(self):
                build_payload(client,topic, Queue_control,"headdown")


        def call_headleft(self):
                build_payload(client,topic, Queue_control,"catch")


        def call_headright(self):
                build_payload(client,topic, Queue_control,"loose")


        def call_headhome(self):
                build_payload(client,topic, Queue_control,"headhome")


        def call_steady(self):
                global ultrasonicMode
                if funcMode == 0:
                        build_payload(client,topic, Queue_control,"steady")
                        ultrasonicMode = 1
                else:
                        build_payload(client,topic, Queue_control,"funEnd")


        def call_FindColor(self):
                if funcMode == 0:
                        build_payload(client,topic, Queue_control,"FindColor")
                else:
                        build_payload(client,topic, Queue_control,"funEnd")


        def call_WatchDog(self):
                if funcMode == 0:
                        build_payload(client,topic, Queue_control,"WatchDog")
                else:
                        build_payload(client,topic, Queue_control,"funEnd")


        def call_FindLine(self):
                if funcMode == 0:
                        build_payload(client,topic, Queue_control,"FindLine")
                else:
                        build_payload(client,topic, Queue_control,"funEnd")

