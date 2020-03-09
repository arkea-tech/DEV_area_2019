import React, { Component } from 'react';
import { View, Text, Picker, StyleSheet } from 'react-native';
import PropTypes from 'prop-types';
import { theme } from '../core/theme';

export default class ServicePicker extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <View>
        <Text style={styles.name}>Action</Text>
        <Picker
          selectedValue={this.props.service}
          onValueChange={this.props.updateService}>
          <Picker.Item label="Select..." value="" />
          <Picker.Item label="Calender" value="Calender" />
          <Picker.Item label="Deezer" value="Deezer" />
          <Picker.Item label="Reddit" value="Reddit" />
          <Picker.Item label="Timer" value="Timer" />
          <Picker.Item label="Weather" value="Weather" />
          <Picker.Item label="Youtube" value="Youtube" />
          <Picker.Item label="Github" value="Github" />
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

ServicePicker.propTypes = {
  service: PropTypes.string,
  updateService: PropTypes.func,
};
