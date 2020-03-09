import React, {Component} from 'react';
import { NavLink } from 'react-router-dom';
import "../styles/navigation.css";

const Navigation = () => {
    return(
        <div>
            <h2>
                <NavLink exact to="/">
                    <button id="navigationButton">
                        Home
                    </button>
                </NavLink>
            </h2>
            <h2>
                <NavLink exact to="/MyArea">
                    <button id="navigationButton">
                        My AREA
                    </button>
                </NavLink>
            </h2>
        </div>
    );
}

export default Navigation;
