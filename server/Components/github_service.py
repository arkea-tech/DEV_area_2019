
import requests


class Github:

    def __init__(self):
        self.name = "Github"
        self.base_url = 'https://api.github.com'
        self.description = "This service is all about Github."
        self.actions = ["detect_new_repository", "detect_new_follower", "detect_new_following"]
        self.reactions = []

    def get_user_followers_number(self, username):
        r = requests.get(url=self.base_url + "/users/" + username)
        json = r.json()
        return json['followers']

    def get_user_repository_number(self, username):
        r = requests.get(url=self.base_url + "/users/" + username)
        json = r.json()
        return json['public_repos']

    def get_user_following_number(self, username):
        r = requests.get(url=self.base_url + "/users/" + username)
        json = r.json()
        return json['following']
