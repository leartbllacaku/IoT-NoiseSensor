from datetime import datetime, timedelta
import random
import time
from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client.Noise_Monitor
db = client.Noise_Monitor   

# Start time
start_time = datetime.now().replace(hour=11, minute=14, second=0, microsecond=0)
# Define the time range for data generation
start_time = datetime.now().replace(second=0, microsecond=0)
end_time = start_time.replace(hour=start_time.hour + 1)

# End time
end_time = start_time.replace(hour=12, minute=0)

# Generate and insert data
# Initial time
current_time = start_time

while current_time <= end_time:
    entry = {
        "timestamp": current_time,
        "value": random.randint(60, 80)
    }
    db.noise_data.insert_one(entry)
    print(f"Inserted data: {entry}")

    time.sleep(10)  # Sleep for 10 seconds

    current_time += timedelta(minutes=1)

print("Data inserted successfully")
print("Data insertion completed.")