from Secrets.APIKeys import deezer
import requests
import json
from datetime import datetime, timedelta


class Deezer :

    def __init__(self):
        self.name = "Deezer"
        self.description = "THis service is for deezer music."
        self.base_url = 'https://api.deezer.com/'
        self.actions = ["detect_new_album", "detect_new_artist_fans", "detect_new_playlist_track", "detect_new_playlist_fans"]

    def get_nbr_album(self, artist):
        response = requests.get(("https://api.deezer.com/search/artist?q=" + artist))
        lodos = json.loads(response.text)
        return lodos['data'][0]['nb_album']

    def get_nbr_fans_artist(self, artist):
        response = requests.get(("https://api.deezer.com/search/artist?q=" + artist))
        lodos = json.loads(response.text)
        return lodos['data'][0]['nb_fan']

    def get_tracks_playlist(self, playlist):
        response = requests.get("https://api.deezer.com/search/playlist?q=" + playlist)
        lodos = json.loads(response.text)
        return lodos['data'][0]['nb_tracks']

    def get_nbr_fans_playlist(self, playlist):
        response = requests.get("https://api.deezer.com/search/playlist?q=" + playlist)
        lodos = json.loads(response.text)
        playlist = lodos['data'][0]
        response = requests.get("https://api.deezer.com/playlist/" + str(playlist['id']))
        lodos = json.loads(response.text)
        return lodos['fans']
