import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    decoded_message = str(message.payload.decode("utf-8"))
    topic = message.topic
    print(" For topic: " + topic + ", Message received: " + decoded_message)
    client.publish("/pong", "Published")
    time.sleep(1)

broker_address="127.0.0.1"

client = mqtt.Client("Python Client Ping") 
client.on_message=on_message 
client.connect(broker_address)
client.loop_start()

client.subscribe("/ping")
time.sleep(4) # Wait 4 seconds for second client to connect and subscribe
client.publish("/pong","First hit")

# Keep Client connection alive for 60 seconds
time.sleep(60)
client.loop_stop()

client.disconnect()