import paho.mqtt.client as mqttClient
import threading,time 
import logging
#from .get_mqtt import on_message

class connexion_mqtt(threading.Thread):

    def __init__(self):      # jusqua = donnée supplémentaire
        threading.Thread.__init__(self)  # ne pas oublier cette ligne
        global broker_address
        broker_address = "dsmsab.site"

      # (appel au constructeur de la classe mère)

    
    def on_connect(self,server_id, userdata, flags, rc):
    
        if rc == 0:
    
            print("Connected to broker")
    
            global Connected                #Use global variable
            Connected = True                #Signal connection 
    
        else:
    
            print("Connection failed")
    
    def on_message(self,server_id, userdata, message):
        print ("Message received: "  + str(message.payload.decode("utf-8")))
        self.message = message.payload.decode("utf-8")

        return str(self.message)

    def on_log(self,server_id, userdata, level, buf):
        print("log: ",buf)


    def run(self):
        broker_address= "dsmsab.site"  #Broker address
        port = 1883                         #Broker port
        Rasp = "560e1cfc-6348-4630-91ac-ab7ba0ad096d"
        self.message = None
        self.server_id = mqttClient.Client(client_id=Rasp)               #create new instance
        self.server_id.on_connect= self.on_connect                      #attach function to callback
        self.server_id.on_message= self.on_message                      #attach function to callback
        self.server_id.on_log=self.on_log
        self.server_id.username_pw_set("7a182fed-8f55-45ff-85f4-77c8fb85f96a", password="ce5a81d0-c7dd-4695-b60b-2e9abde910e4")
        self.server_id.connect(broker_address, port=port)          #connect to broker
        
        self.server_id.loop_start()        #start the loop
        self.server_id.subscribe("channels/8611a392-f843-4edc-893b-8dd9e31fc34e/messages")
        try:
            while True:
                self.background_process()    #Define a thread for FPV and OpenCV

        
        except KeyboardInterrupt:
            print ("exiting")
            self.server_id.disconnect()
            self.server_id.loop_stop()


        # (appel au constructeur de la classe mère)

    def background_process(self):
            try:
                self.send("channels/e7e28c10-1acc-4176-b6ef-a639f17dea2b/messages","100:200:30")
                #Info_Socket.send((Information.get_cpu_tempfunc(self)+' '+Information.get_cpu_use(self)+' '+Information.get_ram_info(self)).encode())
                time.sleep(5)
            except:
                logging.debug("Didn't get hardware info")
                pass

    def send(self,topic_send,data):
        print("Subscribing to topic",str(topic_send))
        self.server_id.publish(str(topic_send),str(data))
        print("Message to topic done",str(topic_send))
