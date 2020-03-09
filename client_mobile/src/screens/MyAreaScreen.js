import React, { memo, useState } from 'react';
import { ScrollView, Text } from 'react-native';
import Background from '../components/Background';
import Header from '../components/Header';
import Logo from '../components/Logo';
import BackButton from '../components/BackButton';
import Paragraph from '../components/Paragraph';
import { server, user } from '../core/data';
import Button from '../components/Button';
import { theme } from '../core/theme';

const MyAreaScreen = ({ navigation }) => {
  const [areas, setAreas] = useState('');

  const _delete_areas = () => {
    fetch(`http://${server.url}:8080/delete_user_areas/`, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        uuid: user.uuid,
      }),
    })
      .then(response => response.json())
      .then(responseJson => {
        if (responseJson.status === 200) {
          alert('Deleted the user Areas');
          setAreas('');
        } else {
          alert(`Could not delete the user Areas: ${responseJson.msg}`);
        }
      })
      .catch(error => {
        console.log(error);
      });
  };

  const _fetch_areas = () => {
    fetch(`http://${server.url}:8080/get_user_areas/?uuid=${user.uuid}`, {
      method: 'GET',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(responseJson => {
        if (responseJson.status === 200) {
          setAreas(JSON.stringify(responseJson.data, null, 4));
        } else {
          alert(`Could not get the user Areas: ${responseJson.msg}`);
        }
      })
      .catch(error => {
        console.log(error);
      });
  };

  _fetch_areas();

  return (
    <ScrollView>
      <Background>
        <BackButton goBack={() => navigation.navigate('Dashboard')} />

        <Logo />

        <Header>My Areas</Header>

        <Text
          style={{
            lineHeight: 20,
            color: theme.colors.secondary,
            margin: 10,
          }}>
          {areas}
        </Text>

        <Button mode="outlined" onPress={_delete_areas}>
          Delete Areas
        </Button>
      </Background>
    </ScrollView>
  );
};

export default memo(MyAreaScreen);
