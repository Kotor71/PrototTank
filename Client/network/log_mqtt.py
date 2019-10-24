import paho.mqtt.client as mqtt #import the client1
import threading,time 


def on_log(client, userdata, level, buf):
    print("log: ",buf)
