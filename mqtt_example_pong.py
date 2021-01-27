import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    decoded_message = str(message.payload.decode("utf-8"))
    topic = message.topic
    print(" For topic: " + topic + ", Message received: " + decoded_message)
    client.publish("/ping", "Published")
    time.sleep(1)

broker_address="127.0.0.1"

client = mqtt.Client("Python Client Pong") 
client.on_message=on_message 
client.connect(broker_address)
client.loop_start()

client.subscribe("/pong")

# Keep Client connection alive for 60 seconds
time.sleep(60)
client.loop_stop()

client.disconnect()