# Todo List for Software Engineering Candidate Task



## 1. Communication Protocol

### Set Up MQTT Broker
- [ ] Choose an MQTT broker (e.g., Mosquitto, RabbitMQ).
- [ ] Install and configure the MQTT broker on your local machine or a server.
- [ ] Test the broker to ensure it can receive and relay messages.

## 2. Server and Database

### Implement Server
- [ ] Choose a web framework (e.g., Django, FastAPI) for the server.
- [ ] Implement the server to subscribe to MQTT topics and receive data from hubs.
- [ ] Write functions to parse incoming messages.
- [ ] Test the server to ensure it receives and processes data correctly.

### Design Database Schema
- [ ] Choose a database (e.g., SQLite, PostgreSQL).
- [ ] Design a schema to store sensor data efficiently.
- [ ] Create the database and implement tables for storing data.
- [ ] Write functions to insert received data into the database.

### Example Server Code
- [ ] Adapt and expand the provided example server code to fit your needs.
- [ ] Test the code thoroughly to ensure it works with your MQTT broker and database.

## 3. Data Visualization

### Create Dashboard
- [ ] Choose a front-end framework (e.g., React, Vue.js).
- [ ] Design a simple web dashboard to visualize sensor data.
- [ ] Implement the dashboard with features to display temperature and humidity over time.
- [ ] Integrate the dashboard with the backend to fetch and display real-time data.

## 4. Documentation

### Design Documentation
- [ ] Document the system architecture, including components like the simulator, server, database, and dashboard.
- [ ] Include diagrams to illustrate data flow and system interactions.

### Code Documentation
- [ ] Thoroughly comment on all code to explain functionality.
- [ ] Write a README file with detailed setup and running instructions.

### Decision Documentation
- [ ] Explain the choice of technologies and approaches used in the project.
- [ ] Discuss any trade-offs or alternatives considered during development.

## Optional Enhancements (PLUS)
- [ ] Implement authentication and authorization for the server.
- [ ] Optimize the database schema for better performance.
- [ ] Enhance the dashboard with advanced visualizations and filtering options.

