import React, { Component } from "react";
import PropTypes from 'prop-types'
import '../styles/menu_button.css'

export default class MenuButton extends Component {
    render() {
        return (
            <button id="roundButton" onMouseDown={this.props.handleMouseDown}>
            </button>
        );
    }
}

MenuButton.propTypes = {
    handleMouseDown: PropTypes.func
};
