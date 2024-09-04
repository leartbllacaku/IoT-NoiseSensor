from datetime import datetime, timedelta
import random
from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client.Noise_Monitor

# Start time
start_time = datetime.now().replace(hour=11, minute=14, second=0, microsecond=0)

# End time
end_time = start_time.replace(hour=12, minute=0)

# Generate and insert data
current_time = start_time
while current_time <= end_time:
    entry = {
        "timestamp": current_time,
        "value": random.randint(60, 80)
    }
    db.noise_data.insert_one(entry)
    current_time += timedelta(minutes=1)

print("Data inserted successfully")