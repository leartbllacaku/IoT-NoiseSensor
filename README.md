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

## Running the Application
Open terminal in project directory and run the command:
  ```bash
    npm start


