# -*- coding: UTF-8 -*-

import sys
import time
import threading
import tkinter as tk
import argparse
import logging

from utils.logger import logger
from utils import parse
from command.control import control_process
from GUI.design import gui
from network.get_information import information_process
from GUI.button import gui_button
from network.connect_mqtt import connexion_mqtt


class main():

    def __init__(self):      # jusqua = donnée supplémentaire
        logger.debug("Init... ")
        parser = argparse.ArgumentParser(description='My awesome script')
        parser.add_argument(
            "-c", "--conf", action="store", dest="conf_file",
            help="Path to config file", default=r"C:\Users\Sabatier\Documents\Dev\PrototTank\server\src\server\configuration\config.yml"
        )
        args = parser.parse_args()
        self.conf = parse.parse_config(path=args.conf_file)


    def run(self):
        self.mqtt_client = connexion_mqtt(self.conf)
        self.mqtt_client.run()
        self.control = control_process(self.mqtt_client.client)
        #info_threading = information_process()
        # info_threading.start()
        # ultra_threading = ultra_process(interface_gui)
        # ultra_threading.start()


if __name__ == '__main__':
    Start= main()                   # Load GUI
    Start.run()



