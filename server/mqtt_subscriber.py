import re
import os
import json
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS, WritePrecision
from influxdb_client.client.write.point import Point
from datetime import datetime
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Read InfluxDB details from environment variables
influxdb_url = os.getenv("INFLUXDB_URL")
influxdb_token = os.getenv("INFLUXDB_TOKEN")
influxdb_org = os.getenv("INFLUXDB_ORG")
influxdb_bucket = os.getenv("INFLUXDB_BUCKET")

# MQTT broker details
broker = os.getenv("MQTT_BROKER")
port = os.getenv("MQTT_PORT")

# # InfluxDB details
# influxdb_url = "http://localhost:****"
# influxdb_token = "token"
# influxdb_org = "org name"
# influxdb_bucket = "bucket name"

# Create a new InfluxDB client instance
influx_client = InfluxDBClient(url=influxdb_url, token=influxdb_token, org=influxdb_org)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        client.subscribe("sensor/sound")
    else:
        print(f"Connect failed with code {rc}")

def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")
    try:
        payload = message.payload.decode()
        try:
            # Try to parse the payload as JSON
            data = json.loads(payload)
            print(f"Parsed data as JSON: {data}")  # Debugging statement
        except json.JSONDecodeError:
            # If JSON parsing fails, assume the payload is a plain float value
            match = re.search(r"[-+]?\d*\.\d+|\d+", payload)
            if match:
                data = float(match.group())
                print(f"Parsed data as float: {data}")  # Debugging statement
            else:
                print("No numeric value found in payload")
                return

        # Construct the data structure for InfluxDB
        if isinstance(data, dict) and 'value' in data and 'timestamp' in data:
            point = Point("sound_sensor") \
                .tag("location", "raspberry_pi") \
                .field("value", float(data["value"])) \
                .time(data["timestamp"], WritePrecision.NS)
        elif isinstance(data, float):
            point = Point("sound_sensor") \
                .tag("location", "raspberry_pi") \
                .field("value", data) \
                .time(datetime.utcnow(), WritePrecision.NS)
        else:
            print("Received data does not contain expected fields or is not a float")
            return
        write_api.write(bucket=influxdb_bucket, org=influxdb_org, record=point)
        print("Data written to InfluxDB")
    except Exception as e:
        print(f"Error writing to InfluxDB: {e}")

# Create a new MQTT client instance
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

try:
    # Connect to the broker
    client.connect(broker, port, 60)
    client.loop_forever()
except Exception as e:
    print(f"Failed to connect to broker: {e}")
    exit(1)

# Start the MQTT client loop
client.loop_forever()
