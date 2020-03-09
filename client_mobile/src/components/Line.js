import React, { memo } from 'react';
import { StyleSheet, View } from 'react-native';
import { theme } from '../core/theme';

const Line = ({ style }) => <View style={[styles.line, style]} />;

const styles = StyleSheet.create({
  line: {
    alignSelf: 'stretch',
    backgroundColor: theme.colors.secondary,
    height: 1,
  },
});

export default memo(Line);
