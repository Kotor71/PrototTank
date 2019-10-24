
import socket
import time
import threading
# import Adafruit_PCA9685
# from rpi_ws281x import *
import argparse
import os
import psutil
import sys
import traceback


#import server.function.findline as findline
# import function.move as move
# import function.servo as servo

#import network.ultra_send as ultra_send_client
from network.info_send import info_send_client
from network.connect_mqtt import connexion_mqtt
# from network.getcommand import Getcommand



#import function.LED as LED
class main(threading.Thread):
   
    def __init__(self):      # jusqua = donnée supplémentaire
        threading.Thread.__init__(self)  # ne pas oublier cette ligne


    def run(self):
            #move.setup()
            #findline.setup()
        Connexion = connexion_mqtt()
        Connexion.start()
        print("GOOD")
        info_threading=info_send_client(Connexion)    #Define a thread for FPV and OpenCV
        info_threading.start()                                     #Thread starts

            #get_command=Getcommand(Connexion)  #Define a thread for FPV and OpenCV
            #get_command.start()                                     #Thread starts

            #move.stand()
        
if __name__ == '__main__':
    Start = main()
    Start.start()
