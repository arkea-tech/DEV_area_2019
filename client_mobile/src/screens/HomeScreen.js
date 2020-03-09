import React, { memo } from 'react';
import BackButton from '../components/BackButton';
import Background from '../components/Background';
import Button from '../components/Button';
import Header from '../components/Header';
import Logo from '../components/Logo';
import Paragraph from '../components/Paragraph';

const HomeScreen = ({ navigation }) => (
  <Background>
    <BackButton goBack={() => navigation.navigate('HostScreen')} />

    <Logo />

    <Header>Action REAction</Header>

    <Paragraph>Automation platform of your digital life.</Paragraph>

    <Button mode="contained" onPress={() => navigation.navigate('LoginScreen')}>
      Login
    </Button>

    <Button
      mode="outlined"
      onPress={() => navigation.navigate('RegisterScreen')}>
      Sign Up
    </Button>
  </Background>
);

export default memo(HomeScreen);
