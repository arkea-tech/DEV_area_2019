import React, { Component } from 'react';
import { View, Picker, TextInput } from 'react-native';
import PropTypes from 'prop-types';

export default class RedditActions extends Component {
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
          <Picker.Item
            label="Detect new subreddit post"
            value="Detect new subreddit post"
          />
          <Picker.Item
            label="Detect new subreddit comment"
            value="Detect new subreddit comment"
          />
          <Picker.Item
            label="Detect new user post"
            value="Detect new user post"
          />
          <Picker.Item
            label="Detect new user comment"
            value="Detect new user comment"
          />
        </Picker>
        {(this.props.reaction === 'Detect new subreddit post' ||
          this.props.reaction === 'Detect new subreddit comment') && (
          <TextInput
            placeholder="Enter subreddit name"
            onChangeText={this.props.updateText}
            value={this.props._Text}
          />
        )}
        {(this.props.reaction === 'Detect new user post' ||
          this.props.reaction === 'Detect new user comment') && (
          <TextInput
            placeholder="Enter reddit username"
            onChangeText={this.props.updateText}
            value={this.props._Text}
          />
        )}
      </View>
    );
  }
}

RedditActions.propTypes = {
  _Text: PropTypes.string,
  updateText: PropTypes.func,
  reaction: PropTypes.string,
  updateReaction: PropTypes.func,
};
