import React from "react";
import './navbar.css';
import logo from '../images/91.jfif';

const Navbar = () => {
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
            </ul>
        </nav>
    )
}

export default Navbar;
