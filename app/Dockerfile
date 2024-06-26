# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /src

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /src
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Command to run MQTT subscriber and FastAPI app concurrently
CMD ["sh", "-c", "python /src/mqtt_subscriber.py & uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]
