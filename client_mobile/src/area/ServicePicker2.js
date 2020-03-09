import React, { Component } from 'react';
import { View, Text, Picker, StyleSheet } from 'react-native';
import PropTypes from 'prop-types';
import { theme } from '../core/theme';

export default class ServicePicker2 extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <View>
        <Text style={styles.name}>Reaction</Text>
        <Picker
          selectedValue={this.props.service2}
          onValueChange={this.props.updateService2}>
          <Picker.Item label="Select..." value="" />
          <Picker.Item label="Calender" value="Calender" />
          <Picker.Item label="Deezer" value="Deezer" />
          <Picker.Item label="Email" value="Email" />
          <Picker.Item label="Timer" value="Timer" />
          <Picker.Item label="Weather" value="Weather" />
          <Picker.Item label="Youtube" value="Youtube" />
        </Picker>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  name: {
    alignSelf: 'center',
    color: theme.colors.primary,
    fontSize: 20,
  },
});

ServicePicker2.propTypes = {
  service2: PropTypes.string,
  updateService2: PropTypes.func,
};
