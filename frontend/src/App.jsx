import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/navbar.jsx';
import RealTimeChart from './components/realTimeChart.jsx';
import AlertLogs from './components/alertLogs.jsx';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="real-time-chart-container">
          <Routes>
            <Route path="/" element={<RealTimeChart />} />
            <Route path="/alerts" element={<AlertLogs />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
