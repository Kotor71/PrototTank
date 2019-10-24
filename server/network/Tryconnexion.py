
import socket
import time
import threading
import argparse
import os
import psutil
#import server.function.LED as LED

def trycon():
    try:
        s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("1.1.1.1",80))
        ipaddr_check=s.getsockname()[0]
        s.close()
        print(ipaddr_check)
        EtatCo=True
    except:
        #     EtatCo=False
        #     ap_threading=threading.Thread(target=ap_thread)   #Define a thread for data receiving
        #     ap_threading.setDaemon(True)                          #'True' means it is a front thread,it would close when the mainloop() closes
        #     ap_threading.start()                                  #Thread starts
        #     LED.colorWipe(Color(0,16,50))
        #     time.sleep(1)
        #     LED.colorWipe(Color(0,16,100))
        #     time.sleep(1)
        #     LED.colorWipe(Color(0,16,150))
        #     time.sleep(1)
        #     LED.colorWipe(Color(0,16,200))
        #     time.sleep(1)
        #     LED.colorWipe(Color(0,16,255))
              time.sleep(1)
        #     LED.colorWipe(Color(35,255,35))
    return EtatCo