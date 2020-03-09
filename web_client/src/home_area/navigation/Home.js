import React, { Component } from 'react';

import MenuServices from '../configure_services/MenuServices'
import ListServices from '../user_services/ListServices'
import FormContainer from '../form/FormContainer'
import axios from "axios"

class Home extends Component {

    constructor()
    {
        super();
        this.state = {
            service: [
                {
                    id: 0,
                    title: 'Github',
                    selected: false,
                    key: 'service',
                    selectedFromList: false
                },
                {
                    id: 1,
                    title: 'Deezer',
                    selected: false,
                    key: 'service',
                    selectedFromList: false
                },
                {
                    id: 2,
                    title: 'Reddit',
                    selected: false,
                    key: 'service',
                    selectedFromList: false
                },
                {
                    id: 3,
                    title: 'Youtube',
                    selected: false,
                    key: 'service',
                    selectedFromList: false
                },
                {
                    id: 4,
                    title: 'Email',
                    selected: false,
                    key: 'service',
                    selectedFromList: false
                },
                {
                    id: 5,
                    title: 'Weather',
                    selected: false,
                    key: 'service',
                    selectedFromList: false
                },
                {
                    id: 6,
                    title: 'Timer',
                    selected: false,
                    key: 'service',
                    selectedFromList: false
                }
            ],
            selectedTotal: 0,
            sameId: -1,
            onlySelectedItems: []
        };
    }


    handleSameSelectedItem = () => {
        this.setState(prevState => ({selectedTotal: prevState.selectedTotal - 1}));
        //console.log(this.state.selectedTotal);
    }

    clearListSelectedItems = () => {
        const { service } = this.state;

        service.map(item => item.selectedFromList ? item.selectedFromList = !item.selectedFromList : null);
        this.setState({selectedTotal: 0, onlySelectedItems: []});
    }

    updateSelectedItems = () => {
        this.setState(prevState => {
            return prevState.selectedTotal !== 3 ?
            {selectedTotal: prevState.selectedTotal + 1} : {selectedTotal: 0}
        });
    }

    toggleSelected = (id, key) => {
        let temp = this.state[key];

        temp[id].selected = !temp[id].selected;
        this.setState({
            [key]: temp
        });
    }

    toggleSelectedFromList = (id, key) => {
        let temp = this.state[key];
        const { sameId } = this.state;

        sameId != id ? this.setState({sameId: id}) : this.handleSameSelectedItem();

        temp[id].selectedFromList = !temp[id].selectedFromList;
        this.setState({
            [key]: temp
        });
    }

    setSelectedServices = () => {
        this.state.service.forEach(item => {
            if (item.selectedFromList)
                this.state.onlySelectedItems.push(item.title);
        });
        this.state.onlySelectedItems = this.state.onlySelectedItems.filter(function(item, pos, self) {
            return self.indexOf(item) == pos;
        });
        //console.log(this.state.onlySelectedItems);
    }

    render()
    {
        this.setSelectedServices();

        return (
            <div className="Home">
                <MenuServices
                list={this.state.service}
                toggleItem={this.toggleSelected}
                />
                <ListServices
                list={this.state.service}
                toggleItem={this.toggleSelectedFromList}
                updateSelectedItems={this.updateSelectedItems}
                selectedTotal={this.state.selectedTotal}/>
                {this.state.selectedTotal == 2 ? <FormContainer serviceAction={this.state.onlySelectedItems[0]} serviceReaction={this.state.onlySelectedItems[1]}
                clearListSelectedItems={this.clearListSelectedItems}/> : null}
            </div>
        );
    }
}

export default Home;
