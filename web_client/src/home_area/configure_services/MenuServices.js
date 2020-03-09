import React, { Component } from 'react';
import PropTypes from 'prop-types'
import Dropdown from './Dropdown'

class MenuServices extends Component {
    
    render()
    {
        return (
            <div className="MenuServices">
                <Dropdown
                    titleHelper="Service"
                    title="Select services"
                    list={this.props.list}
                    toggleItem={this.props.toggleItem}
                />
            </div>
        );
    }

};

MenuServices.propTypes = {
    list: PropTypes.arrayOf(PropTypes.shape({
        id: PropTypes.number,
        title: PropTypes.string,
        selected: PropTypes.bool,
        key: PropTypes.string
    })),
    toggleItem: PropTypes.func
};

export default MenuServices;
