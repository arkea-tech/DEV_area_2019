import React, { Component } from 'react';
import PropTypes from 'prop-types';
import '../../styles/form.css'

const CheckBox = (props) => {
    return(
        <div>
            <label for={props.name} className="form-label-checkbox">
                {props.title}
                <div className="bottom-line-checkbox"></div>
            </label>
            <div className="checkbox-group">
                {
                    props.options.map(option => {
                        return (
                            <label className="checkbox-item" key={option}>
                                <input
                                className="checkbox-element"
                                id={props.name}
                                name={props.name}
                                onChange={props.handleChange}
                                value={option}
                                checked={props.selectedOptions.indexOf(option) > -1}
                                type="checkbox"/>
                                {option}
                            </label>
                        );
                    })
                }
            </div>
        </div>
    );
};

CheckBox.propTypes = {
    handleChange: PropTypes.func,
    options: PropTypes.arrayOf(PropTypes.string),
    selectedOptions: PropTypes.string,
    name: PropTypes.string,
    title: PropTypes.string
};

export default CheckBox;
