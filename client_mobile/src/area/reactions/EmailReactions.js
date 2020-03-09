import React, { Component } from 'react';
import { View, Text, TextInput, Picker, StyleSheet } from 'react-native';
import PropTypes from 'prop-types';

export default class EmailReactions extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <View>
        <Picker
          style={styles.right}
          selectedValue={this.props.reaction2}
          onValueChange={this.props.updateReaction2}>
          <Picker.Item label="Select..." value="" />
          <Picker.Item label="Send email" value="Send email" />
        </Picker>

        {this.props.reaction2 === 'Send email' && (
          <TextInput
            style={styles.right}
            placeholder="Enter Email Address"
            onChangeText={this.props.updateText2}
            value={this.props._Text2}
          />
        )}
      </View>
    );
  }
}

const styles = StyleSheet.create({
  left: {
    justifyContent: 'flex-start',
  },
  right: {
    justifyContent: 'flex-end',
  },
});

EmailReactions.propTypes = {
  _Text2: PropTypes.string,
  updateText2: PropTypes.func,
  reaction2: PropTypes.string,
  updateReaction2: PropTypes.func,
};
