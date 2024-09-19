from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

import datetime

token = "Ph0Y7mUDYUCHsq2-XD24N1xOZ6SP5nWth7Da0rVZq8_Yih3twTaHG5gcWAcotzKvX24f8axAiTk5qq-dGgIImA==" #influxdb token
org = "91Life" #influxdb organization
bucket = "noise_sensor" #influxdb bucket
url = "http://localhost:8086" 

client = InfluxDBClient(url=url, token=token, org = org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Define the data to be written
measurement = "Noise_Level"
tags = {"location": "office"}
fields = {"Value": 50.0}
timestamp = datetime.datetime.now(datetime.timezone.utc)

# Create a Point object
point = Point(measurement) \
    .tag("location", "office") \
    .field("Value", 130.2) \
    .time(timestamp, WritePrecision.S)

# Write the data to InfluxDB
write_api.write(bucket=bucket, record=point)

# Close the client
client.close()

print("Data written to InfluxDB successfully")