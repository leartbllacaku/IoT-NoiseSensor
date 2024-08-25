import React, { useState, useEffect } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

const RealTimeChart = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/noise-data')
            .then(response => response.json())
            .then(data => {
                const formattedData = data.map(entry => [entry.timestamp, entry.noise_level]);
                setData(formattedData);
            });
    }, []);

    const options = {
        title: { text: 'Noise Levels' },
        xAxis: {
            categories: data.map(entry => entry[0]),
            title: { text: 'Time' },
            min: Math.max(data.length - 10, 0), // Display the last 10 data points
            max: data.length - 1, // Ensure the max is the last data point
            scrollbar: {
                enabled: true // Enable the scrollbar
            },
        },
        yAxis: {
            title: { text: 'Noise Level (dB)' }
        },
        series: [{
            name: 'Noise Level',
            data: data.map(entry => entry[1]),
            marker: {
                enabled: true
            },
            dataLabels: {
                enabled: true,
                format: '{y}',
                style: {
                    color: '#000',
                    fontSize: '12px',
                    fontWeight: 'bold'
                }
            }
        }],
        chart: {
            zoomType: 'x' // Allow zooming along the x-axis
        }
    };

    return (
        <HighchartsReact highcharts={Highcharts} options={options} />
    );
};

export default RealTimeChart;
