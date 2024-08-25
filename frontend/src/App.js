import './App.css';
import React from 'react';
import Navbar from './components/navbar';
import Dashboard from './components/dashboard';
import RealTimeChart from './components/realTimeChart';

function App() {
  return (

    <div className="App">
      <Navbar />
      {/* <Dashboard /> */}
      <div className="real-time-chart-container">
        <RealTimeChart className="real-time-chart" />
        <RealTimeChart className="real-time-chart" />
        <RealTimeChart className="real-time-chart" />
        <RealTimeChart className="real-time-chart" />

      </div>
    </div>
  );
}

export default App;
