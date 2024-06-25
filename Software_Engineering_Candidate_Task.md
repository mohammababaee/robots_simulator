# Software Engineering Candidate Task

## Task

We are designing and building an Industrial IoT (IIoT) system to monitor temperature and humidity levels in a manufacturing plant. The system consists of one or more sensors that can collect data from different parts of the plant and transmit it to a Server.

### Requirements:

1. **Sensors and Hubs:**
   - Each sensor will measure temperature and humidity.
   - Each hub will collect data from one or more sensors and transmit it to the server.
   - Each hub has a unique ID and reports the humidity and temperature values to the server at regular intervals.

2. **Communication Protocol:**
   - The communication protocol between the hubs and the server should be MQTT (Message Queuing Telemetry Transport).

3. **Server and Database:**
   - The server must receive the data from the hubs and store it in a database.
   - The database should be designed to efficiently store and retrieve time-series data.

4. **Data Visualization:**
   - For additional points, visualize the collected data on a dashboard with timestamps.

5. **Documentation:**
   - Provide comprehensive documentation of your design, implementation, and any decisions made.

### Objective

By completing this task, you will demonstrate your ability to design and implement a scalable, reliable IIoT system, including utilizing communication protocols, designing cloud architecture, developing server-side applications, and creating user-friendly data visualization tools.



---

### Detailed Task Breakdown

#### 1. Sensors and Hubs

- **Sensors**: Simulate sensors that generate random temperature and humidity data. You can use Python to create these simulations.
- **Hubs**: Create a hub script that collects data from the simulated sensors. This hub will be responsible for sending the data to the server using MQTT.

**Example Code**: (Already provided)
- Python script for a hub to publish data to an MQTT broker.
- Bash script to run the hub script multiple times with random parameters.

#### 2. Communication Protocol

- **MQTT Broker**: Set up an MQTT broker. You can set up a local broker using tools like Mosquitto or RabbitMQ.
   - you have to change the broker url in hub_simulator

#### 3. Server and Database

- **Server**: Implement a server that subscribes to the MQTT topics and receives data from the hubs.
  - You can use Python with libraries like `paho-mqtt`,`pika` for the MQTT client and `Django` or `FastAPI` for the web server.
- **Database**: Design a database schema to store the received sensor data efficiently.

**Example Server Code**:
```python
import paho.mqtt.client as mqtt
import sqlite3

# MQTT broker details
broker = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
port = 1883
topic = "sensor/data/#"

# Database setup
conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensor_data 
             (hub_id TEXT, temperature REAL, humidity REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
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
    parts = message.split(',')
    temp = float(parts[0].split(':')[1].strip().replace('C', ''))
    hum = float(parts[1].split(':')[1].strip().replace('%', ''))
    hub_id = msg.topic.split('/')[-1]
    return hub_id, temp, hum

def save_to_db(hub_id, temp, hum):
    c.execute("INSERT INTO sensor_data (hub_id, temperature, humidity) VALUES (?, ?, ?)", (hub_id, temp, hum))
    conn.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.loop_forever()

```

#### 4. Data Visualization
- **Dashboard**: Create a simple web dashboard to visualize the data.
   - Use a front-end framework like React.
   - Integrate with the backend server to fetch and display data.


#### 5. Documentation
- **Design Documentation**: Describe the system architecture, including simulator, server, database, and dashboard.

- **Code Documentation**: Comment on the code thoroughly and provide a README file with instructions on how to set up and run the system.

- **Decision Documentation**: Explain why certain technologies or approaches were chosen over others..



### Optional Enhancements (PLUS)
   - Implement authentication and authorization for the server.
   - Optimize the database schema for better performance.
   - Enhance the dashboard with more advanced visualizations and filtering options.


### Good luck! If you have any questions or need further assistance, feel free to reach out. 
### hosein.gholami@digikala.com