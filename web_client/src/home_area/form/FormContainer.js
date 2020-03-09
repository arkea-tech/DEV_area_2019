import React, {Component} from 'react';
import PropTypes from 'prop-types';
import FormInput from './FormInput';
import FormCheckBox from './FormCheckBox';
import axios from "axios";
import '../styles/form.css';

export default class FormContainer extends Component {
    constructor() {
        super();
        this.state = {
            user: {
                action: '',
                reaction: '',
                inputAction: '',
                inputReaction: ''
            },
            nextForm: false,
            actionOptions: {
                Timer: ["Create timer", "Restart timers"],
                Weather: ["Detect weather", "Detect temperature", "Detect humidity", "Detect wind speed", "Detect wind direction"],
                Github: ["Detect new repository", "Detect new follower", "Detect new following"],
                Youtube: ["Detect new video", "Detect new subscriber", "Detect new comment", "Detect new like", "Detect new dislike", "Detect new view"],
                Reddit: ["Detect new subreddit post", "Detect new subreddit comment", "Detect new user post", "Detect new user comment"],
                Deezer: ["Detect new album", "Detect new artist fans", "Detect new playlist fans", "Detect new playlist track"]
            },
            reactionOptions: {
                Email: ["Send email"],
                Timer: ["Send email"],
                Weather: ["Send email"],
                Github: ["Send email"],
                Youtube: ["Send email"],
                Reddit: ["Send email"],
                Deezer: ["Send email"]
            },
            inputHintAction: {
                Timer: "Enter a time (in second)",
                Weather: "Enter a city",
                Youtube: "Enter a channel",
                Github: "Enter a repository/username",
                Reddit: "Enter a subreddit name/username",
                Deezer: "Enter an album/artist"
            },
            inputHintReaction: {
                Timer: "Enter your email adress",
                Email: "Enter your email adress",
                Weather: "Enter your email adress",
                Youtube: "Enter your email adress",
                Github: "Enter your email adress",
                Reddit: "Enter an email adress",
                Deezer: "Enter an email adress"
            },
        }
        this.handleFormSubmit = this.handleFormSubmit.bind(this);
        this.handleFormNext = this.handleFormNext.bind(this);
        this.handleClearForm = this.handleClearForm.bind(this);
        this.handleValueInput = this.handleValueInput.bind(this);
        this.handleSelectedCheckbox = this.handleSelectedCheckbox.bind(this);
    }

    handleFormSubmit(e) {
        const {clearListSelectedItems} = this.props;
        var uuid = localStorage.getItem('uuid');
        var params = {
            uuid: uuid,
            service: this.props.serviceAction.toLowerCase(),
            action: this.state.user.action,
            reaction: this.state.user.reaction,
            action_data: {input: this.state.user.inputAction},
            reaction_data: {input: this.state.user.inputReaction}
        };
        e.preventDefault();
        axios.post("http://localhost:8080/add_user_area/", params).then(
            function (response) {
                if (response.data.status === 200) {
                    alert("AREA created with success")
                } else if (response.data.status === 400) {
                    alert(response.data.msg)
                } else {
                    alert("An unknown error might have occured")
                }
            }
        ).catch(function (err) {
            alert(err)
        });
        clearListSelectedItems();
    }


    handleFormNext(e) {
        e.preventDefault();
        this.setState({
            nextForm: true
        });
    }

    handleClearForm(e) {
        let name = e.target.name;
        let id = e.target.id;

        e.preventDefault();
        this.setState(prevState => ({
            user: {
                ...prevState.user,
                [name]: '',
                [id]: ''
            }
        }));
    }

    handleValueInput(e) {
        let value = e.target.value;
        let name = e.target.name;

        this.setState(prevState => ({
            user: {...prevState.user, [name]: value}
        }), () => console.log(this.state.user));
    }

    handleSelectedCheckbox(e) {
        let actionSelected = e.target.value;
        let name = e.target.name;
        const {user} = this.state;

        if (user[name] == actionSelected) {
            actionSelected = '';
        }
        this.setState(prevState => ({
            user: {...prevState.user, [name]: actionSelected}
        }), console.log(user));
    }

    render() {
        const {user, nextForm, actionOptions, reactionOptions, inputHintAction, inputHintReaction} = this.state;
        const {serviceAction, serviceReaction} = this.props;

        return (
            <form className="form-container" onSubmit={this.handleFormSubmit}>
                {
                    !nextForm ?
                        <FormCheckBox
                            handleSelectedCheckbox={this.handleSelectedCheckbox}
                            handleClearForm={this.handleClearForm}
                            handleFormNext={this.handleFormNext}
                            actionsServices={actionOptions}
                            reactionsServices={reactionOptions}
                            userData={user}
                            serviceAction={serviceAction}
                            serviceReaction={serviceReaction}
                        />
                        :
                        <FormInput
                            handleValueInput={this.handleValueInput}
                            handleFormSubmit={this.handleFormSubmit}
                            handleClearForm={this.handleClearForm}
                            userData={user}
                            serviceAction={serviceAction}
                            serviceReaction={serviceReaction}
                            inputHintAction={inputHintAction}
                            inputHintReaction={inputHintReaction}
                        />
                }
            </form>
            //move down component above
            //<FormInput handleValueInput={this.handleValueInput}/>
        );
    }
};

FormCheckBox.propTypes = {
    serviceAction: PropTypes.string,
    serviceReaction: PropTypes.string,
    clearListSelectedItems: PropTypes.func
};
