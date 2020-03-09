import React, { memo, useState } from 'react';
import Background from '../components/Background';
import Button from '../components/Button';
import Header from '../components/Header';
import Logo from '../components/Logo';
import Paragraph from '../components/Paragraph';
import TextInput from '../components/TextInput';
import { server } from '../core/data';
import { urlValidator } from '../core/utils';

const HostScreen = ({ navigation }) => {
  const [url, setUrl] = useState({ value: '', error: '' });

  const _onButtonPressed = () => {
    const urlError = urlValidator(url.value);

    if (urlError) {
      setUrl({ ...url, error: urlError });
      return;
    }

    server.url = url.value;

    navigation.navigate('HomeScreen');
  };

  return (
    <Background>
      <Logo />

      <Header>Action REAction</Header>

      <Paragraph>Automation platform of your digital life.</Paragraph>

      <TextInput
        label="Host"
        returnKeyType="done"
        value={url.value}
        onChangeText={text => setUrl({ value: text, error: '' })}
        error={!!url.error}
        errorText={url.error}
        defaultValue="Server address"
        autoCapitalize="none"
      />

      <Button mode="contained" onPress={_onButtonPressed}>
        Ok
      </Button>
    </Background>
  );
};

export default memo(HostScreen);
