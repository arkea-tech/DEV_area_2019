import React, { Component } from "react";
import MenuButton from './MenuButton';
import Menu from './Menu';

export default class MenuContainer extends Component {

    constructor(props, context) {
        super(props, context);

        this.state = {
            visible: false
        };
        this.toggleMenu = this.toggleMenu.bind(this);
        this.handleMouseDown = this.handleMouseDown.bind(this);
    }

    toggleMenu() {
        this.setState({
            visible: !this.state.visible
        });
    }

    handleMouseDown(e) {
        this.toggleMenu();
        e.stopPropagation();
    }

    render() {
        return (
            <div className="MenuContainer">
                <MenuButton handleMouseDown={this.handleMouseDown}/>
                <Menu
                handleMouseDown={this.handleMouseDown}
                menuVisibility={this.state.visible}
                />
            </div>
        );
    }

};
