import './App.css';
import React from 'react';
import Navbar from './components/navbar.jsx';
import RealTimeChart from './components/realTimeChart.jsx';

function App() {
  return (

    <div className="App">
      <Navbar />
      <div className="real-time-chart-container">
        <RealTimeChart className="real-time-chart" />

      </div>
    </div>
  );
}

export default App;
