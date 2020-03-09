import React, {Component} from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
  } from "react-router-dom";

import Loginscreen from './login/Loginscreen'

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            loginPage: [],
            uploadScreen: []
        }
    }

    componentWillMount() {
        var loginPage = [];
        loginPage.push(<Loginscreen parentContext={this}/>);
        this.setState({
            loginPage: loginPage
        })
    }

    render() {
        return (
            <Router>
            <Switch>
                <Route path="/client.apk" component={() => {
                  window.location.replace(`http://${window.location.hostname}:8080/client.apk`);
                  return null;
                }} />
                <Route path="/">
                    <div className="App">
                        {this.state.loginPage}
                        {this.state.uploadScreen}
                    </div>
                </Route>
            </Switch>
          </Router>

        );
    }
}

export default App;
