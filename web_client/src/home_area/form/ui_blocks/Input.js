import React, { Component } from 'react';
import PropTypes from 'prop-types';

const Input = (props) => {
    return (
        <div className="form-group">
            <label htmlFor={props.name} className="form-label-input">
                {props.title}
                <div className="bottom-line-input"></div>
            </label>
            <input
            className="input-group"
            id={props.name}
            name={props.name}
            type={props.type}
            value={props.value}
            onChange={props.handleChange}
            placeholder={props.placeholder}
            />
        </div>
    );
};

Input.propTypes = {
    handleChange: PropTypes.func,
    name: PropTypes.string,
    title: PropTypes.string,
    value: PropTypes.string,
    type: PropTypes.string,
    placeholder: PropTypes.string
};

export default Input;
