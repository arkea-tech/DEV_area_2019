import React, { Component } from 'react';
import { View, TextInput } from 'react-native';
import PropTypes from 'prop-types';

export default class CalenderActions extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <View>
        <TextInput
          placeholder="Enter Date xx/xx/xx"
          onChangeText={this.props.updateText}
          value={this.props._Text}
        />
      </View>
    );
  }
}

CalenderActions.propTypes = {
  _Text: PropTypes.string,
  updateText: PropTypes.func,
};
