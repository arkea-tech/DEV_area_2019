
import requests
import json

from Secrets.APIKeys import yammer_credentials


class YammerService:

    def __init__(self, access_token=yammer_credentials['dev_token']):
        self.header = {'Authorization': 'Bearer ' + access_token}
        self.base_url = 'https://www.yammer.com/api/v1/'
        self.me = self.get_me()
        self.groups = self.get_user_groups()

    def generate_url(self, suffix):
        """
        Generate a Yammer API endpoint adress
        :param suffix: endpoint name
        """
        return self.base_url + suffix

    def make_get(self, url, body=None):
        """
        Make a get request on address
        :param url: url to make get request on
        :param body: parameters to pass to request
        :return: response of api
        """
        if body is None:
            body = {}
        return requests.get(url=url, json=body, headers=self.header)

    def make_post(self, url, body=None):
        """
        Make a post request on address
        :param url: url to make post request on
        :param body: parameters to pass to request
        :return: response of api
        """
        if body is None:
            body = {}
        return requests.post(url=url, json=body, headers=self.header)

    def get_me(self):
        """
        Return information about the current connection user
        :return: user information
        """
        url = self.generate_url('users/current.json')
        res = self.make_get(url).json()
        return res

    def get_feed(self):
        """
        Return feed of connected user
        :return: user's feed
        """
        url = self.generate_url('messages/my_feed.json')
        res = self.make_get(url, {'limit': 1}).json()
        return res

    def has_new_followers(self, previous):
        """
        Check if the user has new follower
        :return: true/false
        """
        if self.me['stats']['following'] != previous:
            return True
        return False

    def has_new_following(self, previous):
        """
        Check if user has followed new persons
        :return: true/false
        """
        if self.me['stats']['followers'] != previous:
            return True
        return False

    def is_feed_new(self, last_message):
        """
        Check if the user's feed is new based on last message
        :param last_message: lastest message of feed
        :return: true/false
        """
        feed = self.get_feed()['messages']
        if feed[0]['body']['plain'] != last_message:
            return True
        return False

    def get_group_id_from_name(self, name):
        """
        Return the id of a group based on name
        :param name: group name
        :return: id of group
        """
        groups = self.get_user_groups()
        for group in groups:
            if group['name'] == name:
                return group['id']
        return None

    def post_message_in_group(self, message, group_id='15769182208'):
        """
        Post a message in a group
        :param message: message to write
        :param group_id: id of group to post message in
        :return: ok/ko
        """
        url = self.generate_url('messages.json')
        body = {'body': message, 'group_id': group_id}
        res = self.make_post(url, body).json()
        print(json.dumps(res, indent=4))
        if len(res['messages']) > 0:
            print("Message written in group")
            return "OK"
        print("Failed to write message in group")
        return "KO"

    def get_user_group_names(self):
        """
        Get names of user's groups
        :return: names of user's groups
        """
        groups = []
        for group in self.groups:
            groups.append(group['name'])
        return groups

    def is_user_in_group(self, name):
        """
        Check if the user is part of a group based on name
        :param name: name of group
        :return: true/false
        """
        for group in self.groups:
            if group['name'] == name:
                return True
        return False

    def get_user_groups(self):
        """
        Get all user's groups
        :return: all user's groups
        """
        url = self.generate_url('groups/for_user/{}.json'.format(self.me['id']))
        res = self.make_get(url).json()
        groups = []
        for group in res:
            groups.append({'id': group['id'],
                           'name': group['full_name'],
                           'network_id': group['network_id'],
                           'stats': group['stats']})
        return groups
