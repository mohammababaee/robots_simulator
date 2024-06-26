import paho.mqtt.client as mqtt
import sqlite3

# MQTT broker details
broker = "localhost"
port = 1883
topic = "sensor/data/#"

# Database setup
conn = sqlite3.connect("sensor_data.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS sensor_data 
             (hub_id TEXT, temperature REAL, humidity REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)"""
)
conn.commit()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {rc}\n")


def on_message(client, userdata, msg):
    message = msg.payload.decode()
    hub_id, temp, hum = parse_message(message)
    save_to_db(hub_id, temp, hum)


def parse_message(message):
    parts = message.split(",")
    temp = float(parts[0].split(":")[1].strip().replace("C", ""))
    hum = float(parts[1].split(":")[1].strip().replace("%", ""))
    hub_id = msg.topic.split("/")[-1]
    return hub_id, temp, hum


def save_to_db(hub_id, temp, hum):
    c.execute(
        "INSERT INTO sensor_data (hub_id, temperature, humidity) VALUES (?, ?, ?)",
        (hub_id, temp, hum),
    )
    conn.commit()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.loop_forever()
