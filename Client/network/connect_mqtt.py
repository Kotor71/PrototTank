import paho.mqtt.client as mqtt #import the client1
import threading,time 
import queue
from .log_mqtt import on_log
import tkinter as tk
from .send_mqtt import send

class connexion_mqtt(threading.Thread):

    def __init__(self, interface_gui):      # jusqua = donnée supplémentaire
        threading.Thread.__init__(self)  # ne pas oublier cette ligne
#        self.broker_address = interface_gui.E1.get()
        self.broker_address = "dsmsab.site"
        self.interface_gui = interface_gui 
        self.SERVER_PORT = 1883   #Define port serial 
        self.interface_process = interface_gui.root
        self.interface_process_color = interface_gui.color_text

      # (appel au constructeur de la classe mère)

    def on_message(self,client, userdata, message):
        #print ("Message received: "  + str(message.payload.decode("utf-8")))
        test = str(message.payload.decode("utf-8")).split(":")
        self.CPU_TEP_lab=tk.Label(self.interface_process,width=18,text='CPU Temp: %s'%test[0],fg=self.interface_process_color,bg='#212121')
        self.CPU_USE_lab=tk.Label(self.interface_process,width=18,text='CPU Usage:%s'%test[1],fg=self.interface_process_color,bg='#212121')
        self.RAM_lab=tk.Label(self.interface_process,width=18,text='RAM Usage:%s'%test[2],fg=self.interface_process_color,bg='#212121')
        self.CPU_TEP_lab.place(x=400,y=15)                         #Define a Label and put it in position
        self.CPU_USE_lab.place(x=400,y=45)                         #Define a Label and put it in position
        self.RAM_lab.place(x=400,y=75)                         #Define a Label and put it in position

    def run(self):
        ########################################
        print("creating new instance")
        P1=b"177d282a-d832-412d-a818-8a514eb50899"
        self.client = mqtt.Client(client_id=P1) #create new instance
        self.client.on_message=self.on_message #attach function to callback
        self.client.on_log=on_log
        self.client.username_pw_set("28dcd11d-e76a-4596-84bd-c3b9f6f863f6", password="3ea61757-388c-41fa-b17d-fc0803fdc7fb")
        print("connecting to broker")
        self.client.connect(self.broker_address, port=1883)
        print("Broker Connected")
        self.client.loop_start() #start the loop
        self.client.subscribe("channels/8611a392-f843-4edc-893b-8dd9e31fc34e/messages")





    def num_import(self,initial):            #Call this function to import data from '.txt' file
        with open("ip.txt") as f:
            for line in f.readlines():
                if(line.find(initial) == 0):
                    r=line
        begin=len(list(initial))
        snum=r[begin:]
        n=snum
        print(n)
        return n    

    def replace_num(self,initial,new_num):   #Call this function to replace data in '.txt' file
        newline=""
        str_num=str(new_num)
        with open("ip.txt","r") as f:
            for line in f.readlines():
                if(line.find(initial) == 0):
                    line = initial+"%s" %(str_num)
                newline += line
        with open("ip.txt","w") as f:
            f.writelines(newline)    #Call this function to replace data in '.txt' file

