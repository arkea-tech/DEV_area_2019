from youtube import API
from Secrets.APIKeys import youtube as yt
from datetime import datetime, timedelta
import json

api = API(client_id=yt['client_id'], client_secret=yt['client_secret'], api_key=yt['key'])


class Youtube:

    def __init__(self):
        self.name = "Youtube"
        self.description = "This service is all about weather broadcasting."
        self.video_action = ["detect_new_like", "detect_new_dislike", "detect_new_comment", "detect_new_view"]
        self.channel_action = ["detect_new_video", "detect_new_subscriber"]
        self.actions = self.video_action + self.channel_action
        self.reactions = []

    @staticmethod
    def get_channel_info_by_id(channel_id):
        """
        Return information about a channel based on id
        :param channel_id: id of youtube channel
        :return: information about channel
        """
        c = api.get('channels', id=channel_id, part='snippet,contentDetails,statistics')
        if len(c['items']) == 0:
            return 400, "Channel not found"
        data = c['items'][0]
        return data

    @staticmethod
    def get_video_info_by_id(video_id):
        """
        Return information about a youtube video
        :param video_id: id of youtube video
        :return: information about video
        """
        c = api.get('videos', id=video_id, part='snippet,contentDetails,statistics')
        if len(c['items']) == 0:
            return []
        return c['items'][0]

    @staticmethod
    def get_latest_videos_by_channel_id(channel_id, last_n):
        """
        Get the last n videos of a channel
        :param channel_id: id of channel
        :param last_n: last n videos to get
        :return: the last n videos posted by channel
        """
        latests = api.get('search', channelId=channel_id, part='snippet,id', order='date', maxResults=5)
        if len(latests['items']) == 0:
            return 400, "Channel not found"
        latests_videos = []
        i = 0
        for elem in latests['items']:
            if i == last_n:
                break
            video = elem['snippet']
            video['publish_date'] = video['publishedAt']
            latests_videos.append(video)
            i = i + 1
        return latests_videos

    @staticmethod
    def get_latest_video(channel_id):
        """
        Get the very last video of a channel
        :param channel_id: id of channel
        :return: last video information
        """
        latests = api.get('search', channelId=channel_id, part='snippet,id', order='date', maxResults=1)
        if len(latests['items']) < 1:
            return None
        last_video = latests['items'][0]['snippet']
        last_video['publish_date'] = last_video['publishedAt']
        return last_video

    @staticmethod
    def get_channel_id_by_username(username="ScienceEtonnante"):
        """
        Get a channel_id based on channel name
        :param username: channel name
        :return: channel information
        """
        c = api.get('channels', forUsername=username, part='snippet,contentDetails,statistics')
        if len(c['items']) == 0:
            return -1
        return c['items'][0]['id']

    @staticmethod
    def search_channel_by_name(channel_name):
        """
        Search a channel
        :param channel_name: name of the channel
        :return: channel information if found
        """
        videos = api.get('search', q=channel_name, type='channel', safeSearch='strict')
        if len(videos['items']) > 0:
            return videos['items'][0]
        return []

    @staticmethod
    def search_video_by_name(video_name):
        """
        Search a video
        :param video_name: name of video
        :return: video information if found
        """
        videos = api.get('search', q=video_name, type='video', safeSearch='strict')
        if len(videos['items']) > 0:
            return videos['items'][0]
        return []

    @staticmethod
    def get_channel_stats(channel_id):
        """
        Get statistics of a channel
        :param channel_id: id of channel
        :return: stats
        """
        c = api.get('channels', id=channel_id, part='statistics')
        if len(c['items']) == 0:
            return {}
        return c['items'][0]['statistics']

    @staticmethod
    def get_video_stats(video_id):
        """
        Get statistics of a youtube video
        :param video_id: id of video
        :return: stats
        """
        video_info = api.get('videos', id=video_id, part='statistics')
        if len(video_info['items']) > 0:
            return video_info['items'][0]['statistics']
        return {}

    @staticmethod
    def has_new_subscribers(previous, recent):
        """
        Return the difference of subscribers since last check
        :param previous: previous stats retrieved
        :param recent: latest stats retrieved
        :return: difference of subscribers
        """
        return int(recent['subscriberCount']) - int(previous['subscriberCount'])

    @staticmethod
    def has_new_video(previous, recent):
        """
        Return the difference of subscribers since last check
        :param previous: previous stats retrieved
        :param recent: latest stats retrieved
        :return: true/false
        """
        if int(previous['videoCount']) != int(recent['videoCount']):
            return True
        return False

    @staticmethod
    def has_new_like(previous, recent):
        """
        Return the difference of subscribers since last check
        :param previous: previous stats retrieved
        :param recent: latest stats retrieved
        :return: difference of likes
        """
        return int(recent['likeCount']) - int(previous['likeCount'])

    @staticmethod
    def has_new_dislike(previous, recent):
        """
        Return the difference of subscribers since last check
        :param previous: previous stats retrieved
        :param recent: latest stats retrieved
        :return: difference of dislikes
        """
        return int(recent['dislikeCount']) - int(previous['dislikeCount'])

    @staticmethod
    def has_new_view(previous, recent):
        """
        Return the difference of subscribers since last check
        :param previous: previous stats retrieved
        :param recent: latest stats retrieved
        :return: difference of views
        """
        return int(recent['viewCount']) - int(previous['viewCount'])

    @staticmethod
    def has_new_comment(previous, recent):
        """
        Return the difference of subscribers since last check
        :param previous: previous stats retrieved
        :param recent: latest stats retrieved
        :return: difference of subscribers
        """
        return int(recent['commentCount']) - int(previous['commentCount'])

    @staticmethod
    def is_video_new(video, last_update=datetime.now()-timedelta(weeks=1)):
        """
        Check if a new video has been uploaded since last time we checked
        :param video: video information
        :param last_update: last update time
        :return: true/false
        """
        pub_at = video['publish_date'].replace('T', ' ')
        pub_at = pub_at[0:19]
        pub_at = datetime.strptime(pub_at, "%Y-%m-%d %H:%M:%S")
        return pub_at > last_update
