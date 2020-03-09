import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import MenuContainer from './sliding_menu/MenuContainer';
import MyArea from './navigation/MyArea';
import Home from './navigation/Home';

class HomeArea extends Component {

    render()
    {
        return (
            <div className="HomePage">
                <BrowserRouter>
                    <div>
                        <MenuContainer/>
                        <Switch>
                            <Route path='/MyArea' component={MyArea}/>
                            <Route path='/' component={Home}/>
                        </Switch>
                    </div>
                </BrowserRouter>
            </div>
        );
    }
};

export default HomeArea;
