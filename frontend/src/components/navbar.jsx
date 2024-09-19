import React from "react";
import './navbar.css';
import logo from '../images/91.jfif';

const Navbar = () => {

    const openGrafana = () =>{
        const grafanaUrl = "http://localhost:3000/d/bdydftd315728f/real-time-data?orgId=1";
        window.open(grafanaUrl, '_blank');
    }
    return (
        <nav className="navbar">
            <div className="logo-container">
                <img className="logo" src={logo} alt="Logo"/>
                <a href="/" className="nav-title">Noise Monitor</a>
                </div>
            <ul className="nav-elements">
                <li><a href="/">Dashboard</a></li>
                <li><a href="/alerts">Alerts</a></li>
                <li><a href="/">Past Data</a></li>
                <button onClick={openGrafana} className="nav-button">Open Grafana</button>

            </ul>
        </nav>
    )
}

export default Navbar;
