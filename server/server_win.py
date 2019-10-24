
import socket
import time
import threading
# import Adafruit_PCA9685
from rpi_ws281x import *
import argparse
import os
import psutil
import sys
import traceback


#import server.function.findline as findline
import function.move as move
import function.servo as servo
from function.LED import LED

#import network.ultra_send as ultra_send_client
from network.connect_mqtt import connexion_mqtt
from network.getcommand import Getcommand



#import function.LED as LED
class main(threading.Thread):
   
    def __init__(self):      # jusqua = donnee supplementaire
        threading.Thread.__init__(self)  # ne pas oublier cette ligne


    def run(self):
        move.setup()
            #findline.setup()

        Connexion = connexion_mqtt()
        Connexion.start()
        print("GOOD")
        led_process = LED()
        led_process.colorWipe(Color(255,16,0))
        led_process.colorWipe(Color(0,16,50))
        time.sleep(1)
        led_process.colorWipe(Color(0,16,100))
        time.sleep(1)
        led_process.colorWipe(Color(0,16,150))
        time.sleep(1)
        led_process.colorWipe(Color(0,16,200))
        time.sleep(1)
        led_process.colorWipe(Color(0,16,255))
        time.sleep(1)
        led_process.colorWipe(Color(35,255,35))



        get_command=Getcommand(Connexion, led_process)  #Define a thread for FPV and OpenCV
        get_command.start()                                     #Thread starts

            #move.stand()
        
if __name__ == '__main__':
    Start = main()
    Start.start()
