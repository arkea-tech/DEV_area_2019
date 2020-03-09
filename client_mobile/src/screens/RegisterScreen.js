import React, { memo, useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import BackButton from '../components/BackButton';
import Background from '../components/Background';
import Button from '../components/Button';
import Header from '../components/Header';
import Logo from '../components/Logo';
import TextInput from '../components/TextInput';
import { server, user } from '../core/data';
import { theme } from '../core/theme';
import { emailValidator, passwordValidator } from '../core/utils';

const RegisterScreen = ({ navigation }) => {
  const [email, setEmail] = useState({ value: '', error: '' });
  const [password, setPassword] = useState({ value: '', error: '' });
  const [passwordConfirmation, setPasswordConfirmation] = useState({
    value: '',
    error: '',
  });

  const _onSignUpPressed = () => {
    const emailError = emailValidator(email.value);
    const passwordError = passwordValidator(password.value);
    const passwordConfirmationError = passwordValidator(
      passwordConfirmation.value
    );

    if (emailError || passwordError || passwordConfirmationError) {
      setEmail({ ...email, error: emailError });
      setPassword({ ...password, error: passwordError });
      setPasswordConfirmation({
        ...passwordConfirmation,
        error: passwordConfirmationError,
      });
      return;
    }

    fetch(`http://${server.url}:8080/create_new_account/`, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email.value,
        password: password.value,
        confirm_password: passwordConfirmation.value,
      }),
    })
      .then(response => response.json())
      .then(responseJson => {
        if (responseJson.status === 200) {
          user.email = email.value;
          user.uuid = responseJson.uuid;
          navigation.navigate('Dashboard');
        } else {
          navigation.navigate('HomeScreen');
        }
      })
      .catch(error => {
        console.log(error);

        navigation.navigate('HomeScreen');
      });
  };

  return (
    <Background>
      <BackButton goBack={() => navigation.navigate('HomeScreen')} />

      <Logo />

      <Header>Welcome!</Header>

      <TextInput
        label="Email"
        returnKeyType="next"
        value={email.value}
        onChangeText={text => setEmail({ value: text, error: '' })}
        error={!!email.error}
        errorText={email.error}
        autoCapitalize="none"
        autoCompleteType="email"
        textContentType="emailAddress"
        keyboardType="email-address"
      />

      <TextInput
        label="Password"
        returnKeyType="next"
        value={password.value}
        onChangeText={text => setPassword({ value: text, error: '' })}
        error={!!password.error}
        errorText={password.error}
        autoCapitalize="none"
        secureTextEntry
      />

      <TextInput
        label="Confirm password"
        returnKeyType="done"
        value={passwordConfirmation.value}
        onChangeText={text =>
          setPasswordConfirmation({ value: text, error: '' })
        }
        error={!!passwordConfirmation.error}
        errorText={passwordConfirmation.error}
        autoCapitalize="none"
        secureTextEntry
      />

      <Button mode="contained" onPress={_onSignUpPressed} style={styles.button}>
        Sign Up
      </Button>

      <View style={styles.row}>
        <Text style={styles.label}>Already have an account? </Text>
        <TouchableOpacity onPress={() => navigation.navigate('LoginScreen')}>
          <Text style={styles.link}>Login</Text>
        </TouchableOpacity>
      </View>
    </Background>
  );
};

const styles = StyleSheet.create({
  label: {
    color: theme.colors.secondary,
  },
  button: {
    marginTop: 24,
  },
  row: {
    flexDirection: 'row',
    marginTop: 4,
  },
  link: {
    fontWeight: 'bold',
    color: theme.colors.primary,
  },
});

export default memo(RegisterScreen);
