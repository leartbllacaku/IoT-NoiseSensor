import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import { io } from 'socket.io-client';
import axios from 'axios';
import './realTimeChart.css';

const ENDPOINT = 'http://localhost:5000/';

const RealTimeChart = () => {
    const [noiseLevel, setNoiseLevel] = useState(null);
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const threshold = 65;

    useEffect(() => {
        console.log('Initializing WebSocket connection');
        const socket = io(ENDPOINT);
    
        socket.on('connect', () => {
            console.log('Connected to WebSocket');
        });
    
        socket.on('new_data', (newData) => {
            console.log('Received new data:', newData);
            setNoiseLevel(newData.value);  
            setData(prevData => [...prevData, newData]);
            if (loading) setLoading(false);
        });
    
        socket.on('disconnect', () => {
            console.log('Disconnected from WebSocket');
        });
    
        return () => {
            console.log('Cleaning up WebSocket connection');
            socket.disconnect();
        };
    }, []);
    
    useEffect(() => {
        const interval = setInterval(async () => {
            try {
                const response = await axios.get(`${ENDPOINT}/trigger_realtime`);
                console.log(response.data.message);
            } catch (error) {
                console.error('Error triggering real-time data:', error);
            }
        }, 1000);

        return () => clearInterval(interval);
    }, []);

    const gaugeData = [{
        type: 'indicator',
        mode: 'gauge+number',
        value: noiseLevel || 0,
        number: {
            suffix: ' dB',
            font: {
                size: 45,
                color: 'black',
            },
        },
        gauge: {
            axis: { range: [0, 100] },
            bar: { color: 'darkblue' },
            bgcolor: 'lightgray',
            steps: [
                { range: [0, 50], color: 'lightgreen' },
                { range: [50, 80], color: 'yellow' },
                { range: [80, 100], color: 'red' },
            ],
        },
    }];

    const config = {
        displayModeBar: false, 
    };

    return (
        <div className="chart-container">
            <h2>Real-Time Noise Level</h2>
            {loading ? (
            <p className="loading-message">Connecting to data source. Please be patient...</p>
            ) : (
                <>
                    <Plot
                        data={gaugeData}
                        layout={{
                            width: 600,
                            height: 400,
                            margin: { t: 0, b: 0, l: 0, r: 0 },
                        }}
                        config={config} 
                    />
                    {noiseLevel > threshold && (
                        <p className="warning-message">
                            You are making too much noise.<br/>
                            Please be more quiet!
                        </p>
                    )}
                </>
            )}
        </div>
    );
};

export default RealTimeChart;
