from datetime import datetime, timedelta
import random
import time
from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['Noise_Monitor']

# Start time
start_time = datetime.now().replace(second=0, microsecond=0)
print(f"Start time: {start_time}")

# End time (1 hour later)
end_time = start_time + timedelta(hours=1)
print(f"End time: {end_time}")

# Generate and insert data
# Initial time
current_time = start_time

while current_time <= end_time:
    entry = {
        "timestamp": current_time,
        "value": random.randint(60, 80)
    }
    try:
        db.noise_data.insert_one(entry)
        print(f"Inserted data: {entry}")
    except Exception as e:
        print(f"Error inserting data: {e}")

    time.sleep(10)  # Sleep for 10 seconds

    current_time += timedelta(minutes=1)

print("Data inserted successfully")
print("Data insertion completed.")