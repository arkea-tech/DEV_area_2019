
from datetime import datetime
import json

from Components.elasticsearch_interface import ElasticSearchInterface
from Components.gmail_service import MailNotif
from Components.weather_service import Weather
from Components.youtube_service import Youtube
from Components.reddit_service import Reddit
from Components.deezer_service import Deezer
from Components.github_service import Github

from Utils.mail_generator import MailGenerator

esi = ElasticSearchInterface()
mail = MailNotif()
w = Weather()
yt = Youtube()
mg = MailGenerator()
red = Reddit()
deezer = Deezer()
gh = Github()

class Updater:

    def update_timer_service(self, service):
        print("updating timer service")
        now = datetime.now()
        timer_end = datetime.strptime(service['action_data']['end_time'], "%d/%m/%Y %H:%M:%S")
        if now > timer_end:
            if service['reaction'] == 'send_email':
                generated = mg.generate_timer_mail()
                mail.send_email_to(service['reaction_data']['input'], generated['title'], generated['content'])
                service['enabled'] = False
        return service

    def update_youtube_service(self, service):
        print("updating youtube service")
        action = service['action']
        action_data = service['action_data']
        if action in yt.video_action:
            video_id = service['action_data']['video_id']
            if action == "detect_new_like":
                diff = yt.has_new_like(action_data['stats'], yt.get_video_stats(video_id))
                if diff != 0:
                    g = mg.generate_new_likes(yt.get_video_info_by_id(video_id), diff)
                    mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
            if action == "detect_new_dislike":
                diff = yt.has_new_dislike(action_data['stats'], yt.get_video_stats(video_id))
                if diff != 0:
                    g = mg.generate_new_dislikes(yt.get_video_info_by_id(video_id), diff)
                    mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
            if action == "detect_new_comment":
                diff = yt.has_new_comment(action_data['stats'], yt.get_video_stats(video_id))
                if diff != 0:
                    g = mg.generate_new_comments(yt.get_video_info_by_id(video_id), diff)
                    mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
            if action == "detect_new_view":
                diff = yt.has_new_view(action_data['stats'], yt.get_video_stats(video_id))
                if diff != 0:
                    g = mg.generate_new_views(yt.get_video_info_by_id(video_id), diff)
                    mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
            action_data['stats'] = yt.get_video_stats(video_id)
            service['action_data'] = action_data
            return service
        if action in yt.channel_action:
            channel_id = service['action_data']['channel_id']
            if action == "detect_new_subscriber":
                diff = yt.has_new_subscribers(action_data['stats'], yt.get_channel_stats(channel_id))
                if diff != 0:
                    g = mg.generate_new_subscribers(yt.get_channel_info_by_id(channel_id), diff)
                    mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
            if action == "detect_new_video":
                diff = yt.has_new_video(action_data['stats'], yt.get_channel_stats(channel_id))
                if diff is True:
                    g = mg.generate_new_video_mail(video=yt.get_latest_video(channel_id), channel=yt.get_channel_info_by_id(channel_id))
                    mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
            action_data['stats'] = yt.get_channel_stats(channel_id)
            service['action_data'] = action_data
            return service

    def update_weather_service(self, service):
        print("updating weather service")
        city = service['action_data']['city']
        weather = w.get_global_weather_for_city(city)
        action = service['action']
        data = service['action_data']['weather']
        if action == "detect_weather" and weather['sky'] != data['sky']:
            g = mg.generate_weather_status(weather, data, city)
            mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
        if action == "detect_temperature" and weather['temperature']['temp'] != data['temperature']['temp']:
            g = mg.generate_weather_temperature(weather, data, city)
            mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
        if action == "detect_wind_speed" and weather['wind']['speed'] != data['wind']['speed']:
            g = mg.generate_weather_wind_speed(weather, data, city)
            mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
        if action == "detect_wind_direction" and weather['wind']['deg'] != data['wind']['deg']:
            g = mg.generate_weather_wind_direction(weather, data, city)
            mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
        if action == "detect_humidity" and weather['humidity'] != data['humidity']:
            g = mg.generate_weather_humidy(weather, data, city)
            mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
        service['action_data']['weather'] = weather
        service['action_data']['last_update'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return service

    def update_mail_service(self, service):
        return

    def update_reddit_service(self, service):
        print("updating reddit service")
        action = service['action']
        action_data = service['action_data']
        if action == "detect_new_subreddit_post":
            last = red.get_subreddit_last_post(action_data['subreddit'])
            if len(action_data['title']) != len(last.title):
                g = mg.generate_new_sub_post(action_data['subreddit'], last.title)
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['title'] = last.title
        if action == "detect_new_subreddit_comment":
            last = red.get_subreddit_last_comment(action_data['subreddit'])
            if action_data['comment'] != red.get_body_from_comment(last):
                g = mg.generate_new_sub_comment(action_data['subreddit'], last)
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['comment'] = red.get_body_from_comment(last)
        if action == "detect_new_user_post":
            last = red.get_user_last_post(action_data['user'])
            if action_data['title'] != last.title:
                g = mg.generate_new_user_post(action_data['user'], last.title)
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['title'] = last.title
        if action == "detect_new_user_comment":
            last = red.get_user_last_comment(action_data['user'])
            if action_data['comment'] != red.get_body_from_comment(last):
                g = mg.generate_new_user_comment(action_data['user'], last)
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['comment'] = red.get_body_from_comment(last)
        service['action_data'] = action_data
        return service

    def update_github_service(self, service):
        print("updating github service")
        action = service['action']
        action_data = service['action_data']
        if action == "detect_new_repository":
            nbr = gh.get_user_repository_number(action_data['user'])
            if action_data['repo'] != nbr:
                g = mg.generate_new_repo(action_data['user'])
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['repo'] = nbr
        if action == "detect_new_follower":
            nbr = gh.get_user_followers_number(action_data['user'])
            if action_data['follower'] != nbr:
                g = mg.generate_new_follower(action_data['user'])
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['follower'] = nbr
        if action == "detect_new_following":
            nbr = gh.get_user_following_number(action_data['user'])
            if action_data['following'] != nbr:
                g = mg.generate_new_following(action_data['user'])
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['following'] = nbr
        service['action_data'] = action_data
        return service

    def update_deezer_service(self, service):
        print("updating deezer service")
        action_data = service['action_data']
        if service['action'] == "detect_new_album":
            nbr = deezer.get_nbr_album(action_data['artist'])
            if action_data['albums'] != nbr:
                g = mg.generate_new_album(action_data['artist'], nbr)
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['albums'] = nbr
        if service['action'] == "detect_new_artist_fans":
            nbr = deezer.get_nbr_fans_artist(action_data['artist'])
            if action_data['fans'] != nbr:
                g = mg.generate_new_artist_fans(action_data['artist'], nbr)
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['fans'] = nbr
        if service['action'] == "detect_new_playlist_track":
            nbr = deezer.get_tracks_playlist(action_data['playlist'])
            if action_data['tracks'] != nbr:
                g = mg.generate_tracks_playlist(action_data['playlist'], nbr)
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['tracks'] = nbr
        if service['action'] == "detect_new_playlist_fans":
            nbr = deezer.get_nbr_fans_playlist(action_data['playlist'])
            if action_data['fans'] != nbr:
                g = mg.generate_fans_playlist(action_data['playlist'], nbr)
                mail.send_email_to(service['reaction_data']['input'], g['title'], g['content'])
                action_data['fans'] = nbr
        service['action_data'] = action_data
        return service

    def service_switcher(self, service):
        switcher = {
            "timer": self.update_timer_service,
            "weather": self.update_weather_service,
            "youtube": self.update_youtube_service,
            "mail": self.update_mail_service,
            "github": self.update_github_service,
            "reddit": self.update_reddit_service,
            "deezer": self.update_deezer_service
        }
        return switcher.get(service, lambda: "Invalid service")

    def update_service(self, service):
        service_name = service['service']
        service_update_function = self.service_switcher(service_name)
        return service_update_function(service)

    def update_user_services(self, uuid):
        services = esi.get_user_services(uuid)
        new_services = []
        for index, elem in enumerate(services):
            if elem['enabled'] is True:
                updated_service = self.update_service(elem)
                new_services.append(updated_service)
            else:
                new_services.append(elem)
        esi.update_user_services(uuid, new_services)

    def update_users_services(self):
        esi.create_index('accounts')
        users = esi.get_user_uuids()
        print("Updating users' AREAs")
        for user in users:
            self.update_user_services(user)
