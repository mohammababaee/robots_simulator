from fastapi import FastAPI
from typing import List
import sqlite3

app = FastAPI()

# Function to fetch sensor data from SQLite
def fetch_sensor_data():
    conn = sqlite3.connect("/src/sensor_data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC")
    data = c.fetchall()
    conn.close()
    return data

# Route to fetch sensor data
@app.get("/api/sensor-data", response_model=List[dict])
async def get_sensor_data():
    data = fetch_sensor_data()
    sensor_data = []
    for entry in data:
        sensor_data.append(
            {
                "hub_id": entry[0],
                "temperature": entry[1],
                "humidity": entry[2],
                "timestamp": entry[3],
            }
        )
    return sensor_data

# This block allows the script to be run directly with Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
