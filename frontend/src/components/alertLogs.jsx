import React, { useState, useEffect } from 'react';
import Pagination from '../components/Pagination.jsx';
import './alertLogs.css';

const AlertLogs = () => {
    const [alerts, setAlerts] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [alertsPerPage] = useState(10);

    useEffect(() => {
        const fetchAlerts = async () => {
            try {
                const response = await fetch('http://localhost:5000/data');
                const data = await response.json();
                const filteredAlerts = data.filter(alert => alert.value > 70);
                const sortedAlerts = filteredAlerts.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
                setAlerts(sortedAlerts);
            } catch (error) {
                console.error('Error fetching alerts:', error);
            }
        };

        fetchAlerts();
    }, []);

    const indexOfLastAlert = currentPage * alertsPerPage;
    const indexOfFirstAlert = indexOfLastAlert - alertsPerPage;
    const currentAlerts = alerts.slice(indexOfFirstAlert, indexOfLastAlert);

    const formatTimestamp = (timestamp) => {
        const date = new Date(timestamp);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        return `${day}.${month}.${year} ${hours}:${minutes}`;
    };

    const handlePageChange = (pageNumber) => {
        setCurrentPage(pageNumber);
    };

    const exportToCSV = () => {
        const csvRows = [];
        const headers = ['Timestamp', 'Sound Level'];
        csvRows.push(headers.join(','));
    
        alerts.forEach(alert => {
            const row = [formatTimestamp(alert.timestamp), alert.value];
            csvRows.push(row.join(','));
        });
    
        const csvData = csvRows.join('\n');
        const blob = new Blob([csvData], { type: 'text/csv' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'alert_logs.csv';
        a.click();
        window.URL.revokeObjectURL(url);
    };

    return (
        <div className="alert-log-container">
            <div className="alert-log-header">
                <h2>Alert Log</h2>
                <button onClick={exportToCSV}>Download CSV</button>
            </div>
            <div className="alerts-list">
                {currentAlerts.length > 0 ? (
                    currentAlerts.map((alert, index) => (
                        <div key={index} className="alert-item">
                            <h4>ALERT: HIGH SOUND LEVEL</h4>
                            <p>Time: {formatTimestamp(alert.timestamp)}</p>
                            <p>Sound Level: {alert.value} dB</p>
                        </div>
                    ))
                ) : (
                    <p>No alerts recorded yet.</p>
                )}
            </div>
            <Pagination
                currentPage={currentPage}
                totalPages={Math.ceil(alerts.length / alertsPerPage)}
                onPageChange={handlePageChange}
            />
        </div>
    );
};

export default AlertLogs;
