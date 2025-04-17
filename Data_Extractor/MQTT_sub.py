# mqtt_subscriber.py
import paho.mqtt.client as mqtt
import json
from pymongo import MongoClient

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received:", data)
    db.sensordata.insert_one(data)  # Save to MongoDB

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("sensor/turbidity")
client.on_message = on_message

# MongoDB setup
db = MongoClient("mongodb://localhost:27017/").iot_data

client.loop_forever()
