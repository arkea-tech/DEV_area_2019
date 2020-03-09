import React, { Component } from "react";
import { NavLink } from 'react-router-dom';
import "../styles/menu.css";
import Navigation from '../navigation/Navigation';

export default class Menu extends Component {
    render() {
        var visibility = "hide";

        if (this.props.menuVisibility) {
            visibility = "show";
        }
        return (
            <div id="flyoutMenu"
            className={visibility}
            onClick={this.props.handleMouseDown}>
                <Navigation/>
            </div>
        );
    }
}
