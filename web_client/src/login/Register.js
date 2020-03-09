import React, {Component} from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import axios from 'axios';
import Login from './Login';

class Register extends Component {
    constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: '',
            confirm_password: ''
        }
    }

    handleClick(event) {
        var apiBaseUrl = "http://localhost:8080/create_new_account/";
        console.log("values", this.state.email, this.state.password, this.state.confirm_password);
        var self = this;
        var payload = {
            "email": this.state.email,
            "password": this.state.password,
            "confirm_password": this.state.confirm_password
        };
        axios.post(apiBaseUrl, payload)
            .then(function (response) {
                console.log(response);
                alert(response.data.msg);
                if (response.data.status === 200) {
                    var loginscreen = [];
                    loginscreen.push(<Login parentContext={this}/>);
                    var loginmessage = "Not Registered yet ? Go to registration !";
                    self.props.parentContext.setState({
                        loginscreen: loginscreen,
                        loginmessage: loginmessage,
                        buttonLabel: "Register",
                        isLogin: true
                    });
                } else if (response.data.status === 400) {
                    console.log("The passwords don't match");
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    render() {
        return (
            <div style={{textAlign: "center"}}>
                <MuiThemeProvider>
                    <div>
                        <AppBar
                            title="Register"
                        />
                        <TextField
                            hintText="Enter your Email"
                            type="email"
                            floatingLabelText="Email"
                            onChange={(event, newValue) => this.setState({email: newValue})}
                        />
                        <br/>
                        <TextField
                            type="password"
                            hintText="Enter your Password"
                            floatingLabelText="Password"
                            onChange={(event, newValue) => this.setState({password: newValue})}
                        />
                        <br/>
                        <TextField
                            type="password"
                            hintText="Enter your Password again"
                            floatingLabelText="Confirm your password"
                            onChange={(event, newValue) => this.setState({confirm_password: newValue})}
                        />
                        <br/>
                        <RaisedButton label="Submit" primary={true} style={style}
                                      onClick={(event) => this.handleClick(event)}/>
                    </div>
                </MuiThemeProvider>
            </div>
        );
    }
}

const style = {
    margin: 15,
};
export default Register;
