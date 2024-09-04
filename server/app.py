# server/app.py
import sys
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

# Add the database directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database')))
from config import get_db  # type: ignore # Import the get_db function

app = Flask(__name__)
CORS(app)

# Get MongoDB database
db = get_db()

@app.route('/')
def home():
    return 'Hello, this is your noise monitoring dashboard!'

@app.route('/data')
def get_data():
    # Fetch the most recent data entry
    latest_entry = db.noise_data.find().sort('timestamp', -1).limit(1)
    entry = latest_entry.next()
    entry['_id'] = str(entry['_id'])  # Convert ObjectId to string
    entry['timestamp'] = entry['timestamp'].isoformat()  # Convert datetime to ISO 8601 string
    return jsonify(entry)

if __name__ == '__main__':
    app.run(debug=True)