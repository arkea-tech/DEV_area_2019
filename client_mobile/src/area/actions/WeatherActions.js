import React, { Component } from 'react';
import { View, TextInput, Picker } from 'react-native';
import PropTypes from 'prop-types';

export default class WeatherActions extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <View>
        <Picker
          selectedValue={this.props.reaction}
          onValueChange={this.props.updateReaction}>
          <Picker.Item label="Select..." value="" />
          <Picker.Item label="Detect weather" value="Detect weather" />
          <Picker.Item label="Detect temperature" value="Detect temperature" />
        </Picker>
        <TextInput
          placeholder="Enter city name"
          onChangeText={this.props.updateText}
          value={this.props._Text}
        />
      </View>
    );
  }
}

WeatherActions.propTypes = {
  _Text: PropTypes.string,
  updateText: PropTypes.func,
  reaction: PropTypes.string,
  updateReaction: PropTypes.func,
};
