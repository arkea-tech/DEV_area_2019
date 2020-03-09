import React, { Component, memo } from 'react';
import { ScrollView, View } from 'react-native';
import CalenderActions from '../area/actions/CalenderActions';
import DeezerActions from '../area/actions/DeezerActions.js';
import EmailReactions from '../area/reactions/EmailReactions';
import RedditActions from '../area/actions/RedditActions.js';
import ServicePicker2 from '../area/ServicePicker2';
import ServicePicker from '../area/ServicePicker';
import TimerActions from '../area/actions/TimerActions';
import WeatherActions from '../area/actions/WeatherActions';
import YoutubeActions from '../area/actions/YoutubeActions';
import Background from '../components/Background';
import BackButton from '../components/BackButton';
import Button from '../components/Button';
import Line from '../components/Line';
import Logo from '../components/Logo';
import GithubActions from '../area/actions/GithubActions';
import { server, user } from '../core/data';

class NewAreaScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
      reaction: '',
      service: '',
      reaction2: '',
      service2: '',
      _Text: '',
      _Text2: '',
    };

    this.updateService = this.updateService.bind(this);
    this.updateService2 = this.updateService2.bind(this);
    this.updateReaction = this.updateReaction.bind(this);
    this.updateReaction2 = this.updateReaction2.bind(this);
    this._addCorrectActions = this._addCorrectActions.bind(this);
    this._addCorrectReactions = this._addCorrectReactions.bind(this);
  }

  updateText = _Text => {
    this.setState({ _Text: _Text });
  };
  updateText2 = _Text2 => {
    this.setState({ _Text2: _Text2 });
  };
  updateService = service => {
    this.setState({ service: service });
  };

  updateService2 = service2 => {
    this.setState({ service2: service2 });
  };

  updateReaction = reaction => {
    this.setState({ reaction: reaction });
  };

  updateReaction2 = reaction2 => {
    this.setState({ reaction2: reaction2 });
  };

  _onPressButton() {
    if (
      this.state.service === '' ||
      this.state.reaction === '' ||
      this.state.reaction2 === '' ||
      this.state.service2 === ''
    ) {
      alert('Please select an action and a reaction');
    } else {
      fetch(`http://${server.url}:8080/add_user_area/`, {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          uuid: user.uuid,
          service: this.state.service.toLowerCase(),
          action: this.state.reaction,
          reaction: this.state.reaction2,
          action_data: {
            input: this.state._Text,
          },
          reaction_data: {
            input: this.state._Text2,
          },
        }),
      })
        .then(response => response.json())
        .then(responseJson => {
          if (responseJson.status === 200) {
            alert(
              `The ${this.state.service} AREA has been created; Linked action { ${this.state.reaction} } to reaction { ${this.state.reaction2} }`
            );
          } else {
            alert(
              `Could not create the ${this.state.service} AREA linking action { ${this.state.reaction} } to reaction { ${this.state.reaction2} }: ${responseJson.msg}`
            );
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  }

  render() {
    return (
      <ScrollView>
        <Background>
          <BackButton
            goBack={() => this.props.navigation.navigate('Dashboard')}
          />

          <Logo />

          <Line style={{ marginTop: 20, marginBottom: 20 }} />

          <View style={{ minWidth: '75%' }}>
            <ServicePicker
              service={this.state.service}
              updateService={this.updateService}
            />
            <View>{this._addCorrectActions()}</View>
          </View>

          <Line style={{ marginTop: 20, marginBottom: 20 }} />

          <View style={{ minWidth: '75%' }}>
            <ServicePicker2
              service2={this.state.service2}
              updateService2={this.updateService2}
            />
            <View>{this._addCorrectReactions()}</View>
          </View>

          <Button mode="contained" onPress={() => this._onPressButton()}>
            Create AREA
          </Button>
        </Background>
      </ScrollView>
    );
  }

  _addCorrectActions() {
    if (this.state.service === 'Calender') {
      return (
        <CalenderActions
          reaction={this.state.reaction}
          updateReaction={this.updateReaction}
          _Text={this.state._Text}
          updateText={this.updateText}
        />
      );
    } else if (this.state.service === 'Deezer') {
      return (
        <DeezerActions
          reaction={this.state.reaction}
          updateReaction={this.updateReaction}
          _Text={this.state._Text}
          updateText={this.updateText}
        />
      );
    } else if (this.state.service === 'Reddit') {
      return (
        <RedditActions
          reaction={this.state.reaction}
          updateReaction={this.updateReaction}
          _Text={this.state._Text}
          updateText={this.updateText}
        />
      );
    } else if (this.state.service === 'Timer') {
      return (
        <TimerActions
          reaction={this.state.reaction}
          updateReaction={this.updateReaction}
          _Text={this.state._Text}
          updateText={this.updateText}
        />
      );
    } else if (this.state.service === 'Weather') {
      return (
        <WeatherActions
          reaction={this.state.reaction}
          updateReaction={this.updateReaction}
          _Text={this.state._Text}
          updateText={this.updateText}
        />
      );
    } else if (this.state.service === 'Youtube') {
      return (
        <YoutubeActions
          reaction={this.state.reaction}
          updateReaction={this.updateReaction}
          _Text={this.state._Text}
          updateText={this.updateText}
        />
      );
    }
    else if (this.state.service === 'Github') {
      return (
        <GithubActions
          reaction={this.state.reaction}
          updateReaction={this.updateReaction}
          _Text={this.state._Text}
          updateText={this.updateText}
        />
      );
    }
  }

  _addCorrectReactions() {
    if (
      this.state.service2 === 'Calender' ||
      this.state.service2 === 'Deezer' ||
      this.state.service2 === 'Email' ||
      this.state.service2 === 'Timer' ||
      this.state.service2 === 'Weather' ||
      this.state.service2 === 'Youtube'
    ) {
      return (
        <EmailReactions
          reaction2={this.state.reaction2}
          updateReaction2={this.updateReaction2}
          _Text2={this.state._Text2}
          updateText2={this.updateText2}
        />
      );
    }
  }
}

export default memo(NewAreaScreen);
