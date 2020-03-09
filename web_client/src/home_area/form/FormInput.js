import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Input from './ui_blocks/Input';
import Button from './ui_blocks/Button';
import BorderWrapper from 'react-border-wrapper';
//import '../styles/form_input.css'

export default class FormInput extends Component {
    render()
    {
        const { handleValueInput, handleFormSubmit, handleClearForm, userData,
        serviceAction, serviceReaction, inputHintAction, inputHintReaction } = this.props;

        return (
        <div className="form-input">
            <BorderWrapper borderColour="#0065A6" borderWidth="3px" innerPadding="30px" borderRadius="30px">
                <div className="form-input-action">
                    <Input
                    title={`Action - ${userData.action} :`}
                    value={userData.inputAction}
                    name={'inputAction'}
                    type={'text'}
                    placeholder={inputHintAction[serviceAction]}
                    handleChange={handleValueInput}
                    />
                </div>
                <div className="form-input-reaction">
                    <Input
                    title={`Reaction - ${userData.reaction} :`}
                    value={userData.inputReaction}
                    name={'inputReaction'}
                    type={'text'}
                    placeholder={inputHintReaction[serviceReaction]}
                    handleChange={handleValueInput}
                    />
                </div>
                <Button title="Submit" action={handleFormSubmit}/>
                <Button title="Clear" name="inputReaction" id="inputAction" action={handleClearForm}/>
            </BorderWrapper>
        </div>
        );
    }
};

FormInput.propTypes = {
    handleValueInput: PropTypes.func,
    handleFormSubmit: PropTypes.func,
    handleClearForm: PropTypes.func,
    userData: PropTypes.shape({
        action: PropTypes.string,
        reaction: PropTypes.string,
        inputAction: PropTypes.string,
        inputReaction: PropTypes.string
    }),
    inputHintAction: PropTypes.shape({
        Timer: PropTypes.arrayOf(PropTypes.string),
        Weather: PropTypes.arrayOf(PropTypes.string),
        Calendar: PropTypes.arrayOf(PropTypes.string),
        Youtube: PropTypes.arrayOf(PropTypes.string),
        Deezer: PropTypes.arrayOf(PropTypes.string),
        Twitter: PropTypes.arrayOf(PropTypes.string)
    }),
    inputHintReaction: PropTypes.shape({
        Email: PropTypes.arrayOf(PropTypes.string),
        Timer: PropTypes.arrayOf(PropTypes.string),
        Weather: PropTypes.arrayOf(PropTypes.string),
        Calendar: PropTypes.arrayOf(PropTypes.string),
        Youtube: PropTypes.arrayOf(PropTypes.string),
        Deezer: PropTypes.arrayOf(PropTypes.string),
        Twitter: PropTypes.arrayOf(PropTypes.string)
    }),
    serviceAction: PropTypes.string,
    serviceReaction: PropTypes.string
};
