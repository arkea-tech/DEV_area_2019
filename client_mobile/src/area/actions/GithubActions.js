import React, { Component } from 'react';
import { View, TextInput, Picker } from 'react-native';
import PropTypes from 'prop-types';

export default class GithubActions extends Component {
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
          <Picker.Item label="Detect new repository" value="Detect new repository" />
          <Picker.Item label="Detect new follower" value="Detect new follower" />
          <Picker.Item label="Detect new following" value="Detect new following" />
        </Picker>
        <TextInput
          placeholder="Enter Github Name"
          onChangeText={this.props.updateText}
          value={this.props._Text}
        />
      </View>
    );
  }
}

DeezerActions.propTypes = {
  _Text: PropTypes.string,
  updateText: PropTypes.func,
  reaction: PropTypes.string,
  updateReaction: PropTypes.func,
};
