
import socket
import time
import threading
import argparse
import os
import sys
import traceback
import platform
#import server.function.findline as findline
#import network.ultra_send as ultra_send_client
from configuration import parse
from network.connect_mqtt import connexion_mqtt
from configuration.logger import logger

if platform.system() == 'Linux':
    import Adafruit_PCA9685
    import function.move as move
    import function.servo as servo
    import psutil
    from rpi_ws281x import *
    from network.getcommand import Getcommand
    from function.LED import LED    



#import function.LED as LED
class main():
   
    def __init__(self):      # jusqua = donnee supplementaire
        logger.debug("Init... ")
        self.Main = True
        parser = argparse.ArgumentParser(description='My awesome script')
        parser.add_argument(
            "-c", "--conf", action="store", dest="conf_file",
            help="Path to config file", default=r"C:\Users\Sabatier\Documents\Dev\PrototTank\server\src\server\configuration\config.yml"
        )
        args = parser.parse_args()
        self.conf = parse.parse_config(path=args.conf_file)

    def run(self):
        Connexion = connexion_mqtt(self.conf)
        Connexion.run()
        if platform.system() == 'Linux':
            logger.debug("Linux detect...")
            move.setup()
            #findline.setup()
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
        else:
            logger.debug("Not a linux system detect...")

            #move.stand()
        cmd = "on"
        shut_cmd = ['quit', 'exit', 'stop', 'q']
        while True:
            if input().lower() in shut_cmd:
                break


if __name__ == '__main__':
    Start = main()
    Start.run()
