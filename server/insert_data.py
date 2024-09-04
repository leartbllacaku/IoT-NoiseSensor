from datetime import datetime, timedelta
import random
import time
from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client.Noise_Monitor   

# Define the time range for data generation
start_time = datetime.now().replace(second=0, microsecond=0)
end_time = start_time.replace(hour=start_time.hour + 1)

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

print("Data insertion completed.")
