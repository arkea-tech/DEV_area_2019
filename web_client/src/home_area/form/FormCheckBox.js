import React, { Component } from 'react';
import PropTypes from 'prop-types';
import CheckBox from './ui_blocks/CheckBox';
import Button from './ui_blocks/Button';
import BorderWrapper from 'react-border-wrapper';

export default class FormCheckBox extends Component {
    render()
    {
        const { handleSelectedCheckbox, handleClearForm, handleFormNext, actionsServices, reactionsServices, userData, serviceAction, serviceReaction } = this.props;

        return (
        <div className="form-checkbox">
            <BorderWrapper borderColour="#0065A6" borderWidth="3px" innerPadding="30px" borderRadius="30px">
                <div className="form-checkbox-action">
                    <CheckBox name="action" title={`Action - ${serviceAction} :`} handleChange={handleSelectedCheckbox} options={actionsServices[serviceAction]}
                    selectedOptions={userData.action}/>
                </div>
                <div className="form-checkbox-reaction">
                    <CheckBox name="reaction" title={`Reaction - ${serviceReaction} :`} handleChange={handleSelectedCheckbox} options={reactionsServices[serviceReaction]}
                    selectedOptions={userData.reaction}/>
                </div>
                <Button title="Next" action={handleFormNext}/>
                <Button title="Clear" name="action" id="reaction" action={handleClearForm}/>
            </BorderWrapper>
        </div>
        );
    };
};

FormCheckBox.propTypes = {
    handleSelectedCheckbox: PropTypes.func,
    handleClearForm: PropTypes.func,
    handleFormNext: PropTypes.func,
    actionsServices: PropTypes.shape({
        Timer: PropTypes.arrayOf(PropTypes.string),
        Weather: PropTypes.arrayOf(PropTypes.string),
        Calendar: PropTypes.arrayOf(PropTypes.string),
        Youtube: PropTypes.arrayOf(PropTypes.string),
        Deezer: PropTypes.arrayOf(PropTypes.string),
        Twitter: PropTypes.arrayOf(PropTypes.string)
    }),
    reactionsServices: PropTypes.shape({
        Email: PropTypes.arrayOf(PropTypes.string),
        Timer: PropTypes.arrayOf(PropTypes.string),
        Weather: PropTypes.arrayOf(PropTypes.string),
        Calendar: PropTypes.arrayOf(PropTypes.string),
        Youtube: PropTypes.arrayOf(PropTypes.string),
        Deezer: PropTypes.arrayOf(PropTypes.string),
        Twitter: PropTypes.arrayOf(PropTypes.string)
    }),
    userData: PropTypes.shape({
        action: PropTypes.string,
        reaction: PropTypes.string,
        inputAction: PropTypes.string,
        inputReaction: PropTypes.string
    }),
    serviceAction: PropTypes.string,
    serviceReaction: PropTypes.string
};
