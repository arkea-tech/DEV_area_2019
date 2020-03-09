import React, { Component } from 'react';
import { View, Text, TextInput, Picker } from 'react-native';
import PropTypes from 'prop-types';

export default class TimerActions extends Component {
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
          <Picker.Item label="Create timer" value="Create timer" />
          <Picker.Item label="Restart timers" value="Restart timers" />
        </Picker>
        {this.props.reaction === 'Create timer' && (
          <TextInput
            placeholder="Enter time in seconds"
            onChangeText={this.props.updateText}
            value={this.props._Text}
          />
        )}
      </View>
    );
  }
}

TimerActions.propTypes = {
  _Text: PropTypes.string,
  updateText: PropTypes.func,
  reaction: PropTypes.string,
  updateReaction: PropTypes.func,
};
