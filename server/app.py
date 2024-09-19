import sys
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from datetime import datetime

# Add the database directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database')))
from config import get_db  # type: ignore # Import the get_db function

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random secret key for sessions
socketio = SocketIO(app, cors_allowed_origins="*")

# Get MongoDB database
db = get_db()

@app.route('/')
def home():
    return 'Hello, this is your noise monitoring dashboard!'

@app.route('/data')
def get_data():
    data = db.noise_data.find()
    formatted_data = []
    for entry in data:
        entry['_id'] = str(entry['_id'])  # Convert ObjectId to string
        entry['timestamp'] = entry['timestamp'].isoformat()  # Convert datetime to ISO 8601 string
        formatted_data.append(entry)
    return jsonify(formatted_data)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('connected', {'data': 'Connected to the server'})

def broadcast_data(data):
    """Emit real-time noise level data to all connected clients."""
    print('Broadcasting new data:', data)
    socketio.emit('new_data', data)

@app.route('/trigger_realtime')
def trigger_realtime():
    latest_data = db.noise_data.find().sort('timestamp', -1).limit(1)
    data_sent = False
    for entry in latest_data:
        entry['_id'] = str(entry['_id'])  # Convert ObjectId to string
        entry['timestamp'] = entry['timestamp'].isoformat()  # Convert datetime to ISO 8601 string
        print('Fetched latest data:', entry)  # Debugging statement
        broadcast_data(entry)  # Emit the data to all connected clients
        data_sent = True
    if not data_sent:
        print('No data found to send!')
    return jsonify({'message': 'Real-time data sent to clients!' if data_sent else 'No data found to send.'})

@app.route('/insert_test_data', methods=['POST'])
def insert_test_data():
    test_data = {
        'noise_level': request.json.get('noise_level', 50),
        'timestamp': datetime.now()
    }
    result = db.noise_data.insert_one(test_data)
    test_data['_id'] = str(result.inserted_id)
    test_data['timestamp'] = test_data['timestamp'].isoformat()
    print('Inserted test data:', test_data)  # Debugging statement
    broadcast_data(test_data)  # Emit the data to all connected clients
    return jsonify({'message': 'Test data inserted and broadcasted!', 'data': test_data})

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)