import React from "react";
import './navbar.css';
import logo from '../images/navLogo.png'
const Navbar = () => {
    
    return (
        <nav>
            <div className="logo-container">
                <img className="logo" src={logo} alt="Logo"/>
                <p className="nav-title">Office Noise Monitor</p>
            </div>
            <ul className="nav-elements">
                <li>
                    <a href="/">Real-Time </a>
                </li>
                <li>
                    <a href="/">Historical Data</a>
                </li>
                <li>
                    <a href="/">Settings</a>
                </li>

            </ul>
        </nav>
    )
}
export default Navbar;