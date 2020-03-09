import React, { Component } from 'react';
import { View, TextInput, Picker } from 'react-native';
import PropTypes from 'prop-types';

export default class YoutubeActions extends Component {
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
          <Picker.Item label="Detect new video" value="Detect new video" />
          <Picker.Item label="Detect new comment" value="Detect new comment" />
          <Picker.Item label="Detect new like" value="Detect new like" />
          <Picker.Item label="Detect new dislike" value="Detect new dislike" />
          <Picker.Item label="Detect new view" value="Detect new view" />
        </Picker>
        <TextInput
          placeholder="Enter Youtube Channel Name"
          onChangeText={this.props.updateText}
          value={this.props._Text}
        />
      </View>
    );
  }
}

YoutubeActions.propTypes = {
  _Text: PropTypes.string,
  updateText: PropTypes.func,
  reaction: PropTypes.string,
  updateReaction: PropTypes.func,
};
