# -*- coding: UTF-8 -*-
# File name   : client.py
# Description : client  
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2018/08/22

from socket import *
import sys
import time
import threading
import tkinter as tk
from network.connect_mqtt import connexion_mqtt

from command.control import control_process
from GUI.design import gui
from network.get_information import information_process
from GUI.button import gui_button

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('Start main program')

root = ''
stat=0
ultra_data = 'Ultrasonic OFF'
class main():

    def __init__(self):      # jusqua = donnée supplémentaire
        print ("Starting")
      # (appel au constructeur de la classe mère)

    def run(self):
        self.interface_gui = gui()
        self.mqtt_client = connexion_mqtt(self.interface_gui)
        self.mqtt_client.start()
        self.interface_button = gui_button(self.mqtt_client, self.interface_gui)
        time.sleep(0.5)
        self.control = control_process(self.mqtt_client.client)
        while True:
            self.interface_gui.root.mainloop()  # Run the mainloop()

  

        #info_threading = information_process()
        # info_threading.start()

        # ultra_threading = ultra_process(interface_gui)
        # ultra_threading.start()


if __name__ == '__main__':
    Start= main()                   # Load GUI
    Start.run()



