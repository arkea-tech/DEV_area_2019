import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import React, {Component} from 'react';
import axios from 'axios';
import HomeArea from "../home_area/HomeArea.js";

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: ''
        }
    }

    handleClick(event) {
        var apiBaseUrl = "http://localhost:8080/is_account_ok/";
        var self = this;
        var payload = {
            "email": this.state.username,
            "password": this.state.password
        }
        axios.post(apiBaseUrl, payload)
            .then(function (response) {
                console.log(response);
                alert(response.data.msg);
                if (response.data.status === 200) {
                    localStorage.setItem('uuid', response.data.uuid);
                    console.log("Login successfull");
                    self.props.appContext.setState({loginPage: [], uploadScreen: [<HomeArea appContext={self.props.appContext}/>]})
                } else if (response.data.status === 400) {
                    console.log("Username or password don't match");
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    render() {
        return (
            <div>
                <MuiThemeProvider>
                    <div style={{textAlign: "center"}}>
                        <AppBar
                            title="Login"
                        />
                        <TextField
                            hintText="Enter your Username"
                            floatingLabelText="Username"
                            onChange={(event, newValue) => this.setState({username: newValue})}
                        />
                        <br/>
                        <TextField
                            type="password"
                            hintText="Enter your Password"
                            floatingLabelText="Password"
                            onChange={(event, newValue) => this.setState({password: newValue})}
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
export default Login;
