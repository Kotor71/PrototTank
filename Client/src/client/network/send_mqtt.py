import time 
import json
import copy
old_message = ''
def send(client,topic,data):
    print("Subscribing to topic",topic)
    client.subscribe(topic)
    print("Publishing message to topic",topic)
    client.publish(topic,str(data))
    print("Message to topic done",topic)



def build_payload(client, topic, queue, message):
        global old_message
        msg = ''
        message_build = json.dumps(message)
        queue.put(message_build)
        if not queue.empty(): #check if the queue is empty
            msg = queue.get()  #get the first message which was received and delete
            if msg != old_message:
                send(client, topic, msg)
                old_message = copy.deepcopy(msg)

            else:
                return "break"