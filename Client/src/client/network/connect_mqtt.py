import paho.mqtt.client as mqtt #import the client1
import threading,time 
import queue
from .log_mqtt import on_log
import tkinter as tk
from .send_mqtt import send

logger = logging.getLogger('ProtoTank_Client.ProbeCollector')

class connexion_mqtt():

    def __init__(self, conf):      # jusqua = donnée supplémentaire
        logger.debug("Init mqtt connexion")
        self.params = conf
        self.broker_address = self.params['Mqtt']['name']
        self.SERVER_PORT = self.params['Mqtt']['port']
        self.topic_send = self.params['Topic']['Control']
        self.topic_get = self.params['Topic']['Information']
        self.id_connect = self.params['Mqtt']['id']
        self.user = self.params['Mqtt']['user']
        self.password = self.params['Mqtt']['password']

    def on_message(self,client, userdata, message):
        #print ("Message received: "  + str(message.payload.decode("utf-8")))
        test = str(message.payload.decode("utf-8")).split(":")
        print(test)

    def run(self):
        ########################################
        print("creating new instance")
        self.client = mqtt.Client(client_id=self.id_connect) #create new instance
        self.client.on_message=self.on_message #attach function to callback
        self.client.on_log=on_log
        self.client.username_pw_set(self.user, password=self.password)
        print("connecting to broker")
        self.client.connect(self.broker_address, port=1883)
        print("Broker Connected")
        self.client.loop_start() #start the loop
        self.client.subscribe(self.topic_get)
