# Project

The Noise Monitoring System is designed to continuously track and analyze sound levels in an office environment. Utilizing a Raspberry Pi and a microphone, the system captures real-time audio data and processes it to monitor decibel levels across various areas in the office. This data is displayed on a dashboard, providing visual feedback on the current noise levels. If the sound level exceeds a predefined threshold, the system triggers an alert.

The backend of the system is powered by a Flask server, which handles data processing and communication between the Raspberry Pi and the React.js-based dashboard. The project also includes a data storage component for logging days when the noise exceeds the set limits, allowing for historical analysis and long-term monitoring of the office's acoustic environment. This system aims to create a more comfortable and productive workspace by ensuring noise levels are kept within acceptable limits.

## Setup Instructions

To run this application locally, you'll need to set up both the backend and frontend environments. Follow the steps below to install the required dependencies and get everything up and running.

### Backend (Python)

1. **Install Python Libraries**

   Ensure you have Python installed. Then, install the required libraries by running the following command:

   ```bash
   pip install pymongo flask flask_cors


2. **Configuration**

Configure your environment variables and MongoDB connection settings. Update the config.py file or your chosen configuration method with the following details:

***MongoDB connection string***

***Any additional environment-specific settings***

### Frontend (React)

1. **Install Python Libraries**

    Ensure you have Node.js and npm installed on your machine. You can download and install them from <a href="https://nodejs.org/en" target="_blank">Here</a>.

2. **Install React Dependencies**

   Navigate to the frontend directory and install the necessary dependencies with:

   ```bash
     npm install

3. **Running the application**

   Navigate to the project directory, and run the command below:

   ```bash
     npm start
   
### Important Notes ###
   1. Ensure the Flask server is always running to save the data received from the Raspberry Pi.
   2. The Raspberry Pi must be connected to the internet to send data to the server.


## Update
We have switched from MongoDB to InfluxDB for storing noise data. You will need to have InfluxDB set up for the system to work. You can do this using Docker or Powershell:

- **Docker Setup:** Set up an InfluxDB instance using Docker by following the official InfluxDB Docker documentation.
  
- **Powershell Setup:** Alternatively, you can install InfluxDB natively through Powershell.

The system includes an `mqtt_subscriber.py` script that retrieves data from the Raspberry Pi and stores it in the InfluxDB database. It communicates with the Raspberry Pi using the SSH protocol.

For visualization, Grafana is used to display the data in real-time on a dashboard.

### Required Installations:
1. **InfluxDB** (Set up using Docker or locally)
2. **Grafana** (For data visualization)
3. **MQTT Broker** (To handle message transfers between the Raspberry Pi and the backend)
4. **Python Libraries:** `influxdb-client`, `paramiko` (for SSH communication)

Ensure these are installed and correctly configured to ensure the system works seamlessly.







