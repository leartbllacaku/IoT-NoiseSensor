from flask import Flask, render_template, jsonify
from flask_cors import CORS
import webbrowser
import threading

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, this is your noise monitoring dashboard!'


@app.route('/dashboard')
def dashboard():
    dummy_data = {
        'noise_levels': [40, 55, 70, 65, 80],
        'timestamps': ['10:00', '10:15', '10:30', '10:45', '11:00'],
        'status': "Normal"
    }
    return jsonify(dummy_data)

@app.route('/api/noise-data')
def get_noise_data():
    data=[
        {"timestamp": "10:00", "noise_level": 40},
        {"timestamp": "10:02", "noise_level": 55},
        {"timestamp": "10:04", "noise_level": 70},
        {"timestamp": "10:06", "noise_level": 65},
        {"timestamp": "10:08", "noise_level": 80},
        {"timestamp": "10:10", "noise_level": 40},
        {"timestamp": "10:12", "noise_level": 55},
        {"timestamp": "10:14", "noise_level": 70},
        {"timestamp": "10:16", "noise_level": 65},
        {"timestamp": "10:18", "noise_level": 80},
        {"timestamp": "10:20", "noise_level": 40},
        {"timestamp": "10:22", "noise_level": 55},
        {"timestamp": "10:24", "noise_level": 70},
        {"timestamp": "10:26", "noise_level": 65},
        {"timestamp": "10:28", "noise_level": 80},
        {"timestamp": "10:30", "noise_level": 40},
        { "timestamp": "10:32", "noise_level": 55},
        {"timestamp": "10:34", "noise_level": 70},
        {"timestamp": "10:36", "noise_level": 65},
        {"timestamp": "10:38", "noise_level": 80},
        {"timestamp": "10:40", "noise_level": 40},
        {"timestamp": "10:42", "noise_level": 55},
        {"timestamp": "10:44", "noise_level": 70},
        {"timestamp": "10:46", "noise_level": 65},
        {"timestamp": "10:48", "noise_level": 80},
        {"timestamp": "10:50", "noise_level": 40},
        {"timestamp": "10:52", "noise_level": 55},
        {"timestamp": "10:54", "noise_level": 70},
    ]
    return jsonify(data)

def open_browser():
    webbrowser.open_new('http://localhost:3000')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()  # Open the browser after 1 second
    app.run(debug=True) 