import React, { Component } from 'react';
import PropTypes from 'prop-types';

const Button = (props) => {
    return(
        <button
        className="button" 
        name={props.name}
        id={props.id}
        style={props.style}
        onClick={props.action}>
            {props.title}
        </button>
    );
};

Button.propTypes = {
    action: PropTypes.func,
    name: PropTypes.func,
    id: PropTypes.func,
    title: PropTypes.string,
    style: PropTypes.object
};

export default Button;
