/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React from 'react';
import Application from './src';
import { Provider } from 'react-native-paper';
import { theme } from './src/core/theme';

const App: () => React$Node = () => {
  return (
    <Provider theme={theme}>
      <Application />
    </Provider>
  );
};

export default App;
