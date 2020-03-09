
from datetime import datetime, timedelta

from Components.elasticsearch_interface import ElasticSearchInterface
from Components.weather_service import Weather
from Components.youtube_service import Youtube
from Components.reddit_service import Reddit
from Components.github_service import Github
from Components.deezer_service import Deezer

INPUT = "input"

class Preparer:

    def prepare_service(self, service):
        """
        Redirect service to specific service preparation function
        """
        if service['service'] == 'timer':
            return self.prepare_timer_area(service)
        if service['service'] == 'weather':
            return self.prepare_weather_area(service)
        if service['service'] == 'youtube':
            return self.prepare_youtube_area(service)
        if service['service'] == 'reddit':
            return self.prepare_reddit_area(service)
        if service['service'] == 'github':
            return self.prepare_github_area(service)
        if service['service'] == 'deezer':
            return self.prepare_deezer_area(service)
        if service['service'] == 'yammer':
            return self.prepare_yammer_area(service)
        return {}

    @staticmethod
    def prepare_youtube_area(service):
        """
        Prepare the data to be usable when checking for updates
        :param service: service to prepare
        """
        yt = Youtube()
        action_data = service['action_data']
        if service['action'] in yt.video_action:
            video = yt.search_video_by_name(action_data[INPUT])
            if video == []:
                return None
            action_data['video'] = action_data[INPUT]
            action_data['video_id'] = video['id']['videoId']
            action_data['stats'] = yt.get_video_stats(video['id']['videoId'])
        if service['action'] in yt.channel_action:
            channel = yt.search_channel_by_name(action_data[INPUT])
            if channel == []:
                return None
            action_data['channel'] = action_data[INPUT]
            action_data['channel_id'] = channel['id']['channelId']
            action_data['stats'] = yt.get_channel_stats(channel['id']['channelId'])
        if service['action'] not in yt.actions:
            return {}
        action_data['last_update'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        service['action_data'] = action_data
        return service

    @staticmethod
    def prepare_timer_area(service):
        """
        Prepare the data to be usable when checking for updates
        :param service: service to prepare
        """
        action_data = service['action_data']
        curr_time = datetime.now()
        try:
            sec = int(action_data[INPUT])
        except Exception as e:
            print("invalid timer time")
            sec = 60
        timer_end = curr_time + timedelta(seconds=sec)
        action_data['end_time'] = timer_end.strftime("%d/%m/%Y %H:%M:%S")
        service['action_data'] = action_data
        return service

    @staticmethod
    def prepare_weather_area(service):
        """
        Prepare the data to be usable when checking for updates
        :param service: service to prepare
        """
        w = Weather()
        action_data = service['action_data']
        if service['action'] in w.actions:
            weather = w.get_global_weather_for_city(action_data[INPUT])
            action_data['weather'] = weather
            action_data['city'] = action_data[INPUT]
        else:
            return {}
        action_data['last_update'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        service['action_data'] = action_data
        return service

    @staticmethod
    def prepare_github_area(service):
        gh = Github()
        action_data = service['action_data']
        if service['action'] == "detect_new_repository":
            user = action_data[INPUT]
            action_data['user'] = user
            repo_nbr = gh.get_user_repository_number(user)
            action_data['repo'] = repo_nbr
        if service['action'] == "detect_new_follower":
            user = action_data[INPUT]
            action_data['user'] = user
            repo_nbr = gh.get_user_followers_number(user)
            action_data['follower'] = repo_nbr
        if service['action'] == "detect_new_following":
            user = action_data[INPUT]
            action_data['user'] = user
            repo_nbr = gh.get_user_following_number(user)
            action_data['following'] = repo_nbr
        if service['action'] not in gh.actions:
            return {}
        action_data['last_update'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        service['action_data'] = action_data
        return service

    @staticmethod
    def prepare_reddit_area(service):
        """
        Prepare the data to be usable when checking for updates
        :param service: service to prepare
        """
        red = Reddit()
        action_data = service['action_data']
        if service['action'] == "detect_new_subreddit_post":
            post = red.get_subreddit_last_post(action_data[INPUT])
            action_data['subreddit'] = action_data[INPUT]
            action_data['title'] = post.title
        if service['action'] == "detect_new_subreddit_comment":
            comment = red.get_subreddit_last_comment(action_data[INPUT])
            action_data['subreddit'] = action_data[INPUT]
            action_data['comment'] = red.get_body_from_comment(comment)
        if service['action'] == "detect_new_user_post":
            post = red.get_user_last_post(action_data[INPUT])
            action_data['user'] = action_data[INPUT]
            action_data['title'] = post.title
        if service['action'] == "detect_new_user_comment":
            comment = red.get_user_last_comment(action_data[INPUT])
            action_data['user'] = action_data[INPUT]
            action_data['comment'] = red.get_body_from_comment(comment)
        if service['action'] not in red.actions:
            return {}
        action_data['last_update'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        service['action_data'] = action_data
        return service

    @staticmethod
    def prepare_deezer_area(service):
        deezer = Deezer()
        action_data = service['action_data']
        if service['action'] == "detect_new_album":
            artist = action_data[INPUT]
            album_nbr = deezer.get_nbr_album(artist)
            action_data['artist'] = artist
            action_data['albums'] = album_nbr
        if service['action'] == "detect_new_artist_fans":
            artist = action_data[INPUT]
            fans = deezer.get_nbr_fans_artist(artist)
            action_data['artist'] = artist
            action_data['fans'] = fans
        if service['action'] == "detect_new_playlist_track":
            playlist = action_data[INPUT]
            tracks = deezer.get_tracks_playlist(playlist)
            action_data['playlist'] = playlist
            action_data['tracks'] = tracks
        if service['action'] == "detect_new_playlist_fans":
            playlist = action_data[INPUT]
            fans = deezer.get_nbr_fans_playlist(playlist)
            action_data['playlist'] = playlist
            action_data['fans'] = fans
        if service['action'] not in deezer.actions:
            return {}
        action_data['last_update'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        service['action_data'] = action_data
        return service

    @staticmethod
    def prepare_yammer_area(service):
        return