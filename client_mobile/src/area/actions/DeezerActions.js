import React, { Component } from 'react';
import { View, TextInput, Picker } from 'react-native';
import PropTypes from 'prop-types';

export default class DeezerActions extends Component {
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
          <Picker.Item label="Detect new album" value="Detect new album" />
          <Picker.Item label="Detect new artist" value="Detect new artist" />
          <Picker.Item label="Detect new fans" value="Detect new fans" />
          <Picker.Item
            label="Detect new track in playlist"
            value="Detect new track in playlist"
          />
        </Picker>
        <TextInput
          placeholder="Enter Deezer Channel Name"
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
