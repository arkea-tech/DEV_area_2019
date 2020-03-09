import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';

import {
  Dashboard,
  ForgotPasswordScreen,
  HomeScreen,
  HostScreen,
  LoginScreen,
  NewAreaScreen,
  MyAreaScreen,
  RegisterScreen,
} from './screens';

const Router = createStackNavigator(
  {
    Dashboard,
    ForgotPasswordScreen,
    HomeScreen,
    HostScreen,
    LoginScreen,
    MyAreaScreen,
    NewAreaScreen,
    RegisterScreen,
  },
  {
    initialRouteName: 'HostScreen',
    headerMode: 'none',
  }
);

export default createAppContainer(Router);
