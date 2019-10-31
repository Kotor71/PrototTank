import paho.mqtt.client as mqttClient
import threading, time , logging

logger = logging.getLogger('ProtoTank_Server.ProbeCollector')


class connexion_mqtt():

    def __init__(self, conf ):      # jusqua = donnée supplémentaire
        logger.debug("Init mqtt connexion")
        self.params = conf
        self.broker_address = self.params['Mqtt']['name']
        self.port = self.params['Mqtt']['port']
        self.topic = self.params['Topic']['Information']
        self.id_connect = self.params['Mqtt']['id']
        self.user = self.params['Mqtt']['user']
        self.password = self.params['Mqtt']['password']

    def on_connect(self,server_id, userdata, flags, rc):
        if rc == 0:
            logger.debug("Connected to broker")
            global Connected                #Use global variable
            Connected = True                #Signal connection 
        else:
            logger.debug("Connection failed")

    def on_message(self,server_id, userdata, message):
        logger.debug("Message received: "  + str(message.payload.decode("utf-8")))
        self.message = message.payload.decode("utf-8")
        return str(self.message)

    def on_log(self,server_id, userdata, level, buf):
        return

    def run(self):
        self.server_id = mqttClient.Client(client_id=self.id_connect)               #create new instance
        self.server_id.on_connect= self.on_connect                      #attach function to callback
        self.server_id.on_message= self.on_message                      #attach function to callback
        self.server_id.on_log=self.on_log
        self.server_id.username_pw_set(self.user, password=self.password)
        self.server_id.connect(self.broker_address, port=self.port)          #connect to broker
        self.server_id.loop_start()        #start the loop
        self.server_id.subscribe(self.topic)
        #try:
          #  while True:
           #     self.background_process()    #Define a thread for FPV and OpenCV


        # except KeyboardInterrupt:
        #     print ("exiting")
        #     self.server_id.disconnect()
        #     self.server_id.loop_stop()


        # (appel au constructeur de la classe mère)

    def background_process(self):
            try:
                self.send("channels/e7e28c10-1acc-4176-b6ef-a639f17dea2b/messages","100:200:30")
                #Info_Socket.send((Information.get_cpu_tempfunc(self)+' '+Information.get_cpu_use(self)+' '+Information.get_ram_info(self)).encode())
                time.sleep(5)
            except:
                logger.debug("Didn't get hardware info")
                pass

    def send(self,topic_send,data):
        print("Subscribing to topic",str(topic_send))
        self.server_id.publish(str(topic_send),str(data))
        print("Message to topic done",str(topic_send))
