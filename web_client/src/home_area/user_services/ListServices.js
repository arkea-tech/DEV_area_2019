import React, { Component } from 'react'
import PropTypes from 'prop-types'
import BorderWrapper from 'react-border-wrapper'
import FontAwesome from 'react-fontawesome'
import '../styles/list_services.css'

export default class ListServices extends Component {
    render()
    {
        const { list, toggleItem, selectedTotal, updateSelectedItems } = this.props;

        return (
            <div className="ListServices">
                <BorderWrapper borderColour="#0065A6" borderWidth="3px" innerPadding="30px" borderRadius="30px">
                        <h2 className="header-services">
                            Services :
                            <div className="bottom-line"></div>
                        </h2>
                        <ul className="list-group">
                            {
                                list.map(item => ( item.selected ?
                                    <li id="list-item" key={item.id}
                                    onClick={() => { toggleItem(item.id, item.key); updateSelectedItems() }}>
                                        <a href="#">
                                            {
                                                item.selectedFromList && selectedTotal != 3 ?
                                                    <div id="check-item">
                                                        {item.title}
                                                        <FontAwesome id="check-list" name="check"/>
                                                    </div>
                                                : item.title
                                            }
                                        </a>
                                    </li> : null
                                ))
                            }
                        </ul>
                </BorderWrapper>
            </div>
        );
    }
};

ListServices.propTypes = {
    list: PropTypes.arrayOf(PropTypes.shape({
        id: PropTypes.number,
        title: PropTypes.string,
        selected: PropTypes.bool,
        key: PropTypes.string
    })),
    toggleItem: PropTypes.func,
    selectedTotal: PropTypes.number,
    updateSelectedItems: PropTypes.func
};
