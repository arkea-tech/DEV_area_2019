import React, { memo } from 'react';
import Button from '../components/Button';
import Background from '../components/Background';
import Header from '../components/Header';
import Logo from '../components/Logo';

const Dashboard = ({ navigation }) => (
  <Background>
    <Logo />

    <Header>Dashboard</Header>

    <Button mode="contained" onPress={() => navigation.navigate('NewAreaScreen')}>
      New Area
    </Button>

    <Button mode="contained" onPress={() => navigation.navigate('MyAreaScreen')}>
      My Areas
    </Button>

    <Button mode="outlined" onPress={() => navigation.navigate('HomeScreen')}>
      Logout
    </Button>
  </Background>
);

export default memo(Dashboard);
