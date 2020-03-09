
import json
import re

from Components.github_service import Github


gh = Github()

class MailGenerator:

    # Misc

    def __init__(self):
        self.yt_logo = {'url': "https://etapes.com/app/uploads/2017/08/1504100047.jpg", 'width': '50%', 'height': '50%'}
        self.weather_logo = {'url': "https://images-eu.ssl-images-amazon.com/images/I/41wkG24yDkL.png", 'width': '100%', 'height': '100%'}
        self.reddit_logo = {'url': 'https://upload.wikimedia.org/wikipedia/fr/thumb/5/58/Reddit_logo_new.svg/1200px-Reddit_logo_new.svg.png', 'width': '100%', 'height': '100%'}
        self.github_logo = {'url': "https://www.pngitem.com/pimgs/m/128-1280162_github-logo-png-cat-transparent-png.png", 'width': '100%',
                             'height': '100%'}
        self.deezer_logo = {'url': "https://www.itespresso.fr/wp-content/uploads/2013/11/deezer-logo-1280x720.jpg", 'width': '100%',
                             'height': '100%'}
        self.yammer_logo = {'url': 'https://freevectorlogo.net/wp-content/uploads/2012/10/yammer-logo-vector-400x400.png',
                            'width': '170%',
                            'height': '170%'}

    @staticmethod
    def linebreak():
        return "<br><br>"

    @staticmethod
    def default():
        return ["<br>Hello,<br><br>"]

    @staticmethod
    def signature():
        return "<br><br>Best regards,<br>AREA Notifier<br>"

    @staticmethod
    def sentences_to_text(content):
        return " ".join(content)

    def remove_html(self, msg):
        p = re.compile(r'<.*?>')
        return p.sub('', msg)

    # Timer

    def generate_timer_mail(self):
        title = "Your timer has ended"
        sentences = self.default()
        sentences.append("The timer you've previously defined has ended.")
        sentences.append("<br>The REAction has been triggered !")
        sentences.append(self.signature())
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def add_image(self, img):
        return '<br><img src="{}" width="{}" height="{}">'.format(img['url'], img['width'], img['height'])

    # Deezer

    def generate_fans_playlist(self, playlist, fans):
        title = "New fans for playlist '{}'".format(playlist)
        sentences = self.default()
        sentences.append("New fans have been detected for a playlist you're following !<br>")
        sentences.append("Now the playlist counts <b>{}</b> fans.".format(fans))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.deezer_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_tracks_playlist(self, playlist, tracks):
        title = "New tracks added for playlist '{}'".format(playlist)
        sentences = self.default()
        sentences.append("New tracks have been added to the playlist: <b>'{}'</b> !<br>".format(playlist))
        sentences.append("Now, the number of tracks is <b>{}</b> fans.".format(tracks))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.deezer_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_album(self, artist, albums):
        title = "{} has released a new album".format(artist)
        sentences = self.default()
        sentences.append("{} has just released a new album !<br>")
        sentences.append("Now the artist have <b>{}</b> albums.".format(albums))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.deezer_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_artist_fans(self, artist, fans):
        title = "New fans are following '{}'".format(artist)
        sentences = self.default()
        sentences.append("New fans have been detected for the artist named '{}' !<br>".format(artist))
        sentences.append("The number of fans is now around <b>{}</b> fans.".format(fans))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.deezer_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    # Reddit

    def generate_new_sub_post(self, subreddit, post):
        title = "New subreddit post detected"
        sentences = self.default()
        sentences.append("A new post in subreddit <b>'{}'</b> have been detect !<br>".format(subreddit))
        sentences.append("This brand new post is untitled: <b>{}</b>.".format(post))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.reddit_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_sub_comment(self, subreddit, comment):
        title = "New subreddit comment detected"
        sentences = self.default()
        sentences.append("A new comment in subreddit <b>'{}'</b> have been detect !<br>".format(subreddit))
        sentences.append("This new comment is: <b>{}</b>.".format(comment))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.reddit_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_user_post(self, user, post):
        title = "User '{}' has written a new post".format(user)
        sentences = self.default()
        sentences.append("The user <b>'{}'</b> have posted a new message !<br>".format(user))
        sentences.append("Here is his post title: <b>{}</b>.".format(post))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.reddit_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_user_comment(self, user, comment):
        title = "User '{}' has written a new comment".format(user)
        sentences = self.default()
        sentences.append("The user <b>'{}'</b> have posted a new comment !<br>".format(user))
        sentences.append("This is the comment he just posted: <b>{}</b>.".format(comment))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.reddit_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    # GitHub

    def generate_new_repo(self, user):
        title = "A new repository have been created"
        sentences = self.default()
        sentences.append("User <b>'{}'</b> have created a new repository !<br>".format(user))
        sentences.append("Now, this user have <b>{}</b> repositories.".format(gh.get_user_repository_number(user)))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.github_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_follower(self, user):
        title = "'{}' have a new follower".format(user)
        sentences = self.default()
        sentences.append("User <b>'{}'</b> just got a brand new follower !<br>".format(user))
        sentences.append("Now, this user have <b>{}</b> followers.".format(gh.get_user_followers_number(user)))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.github_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_following(self, user):
        title = "'{}' just followed a new user".format(user)
        sentences = self.default()
        sentences.append("User <b>'{}'</b> just followed a new GitHub user !<br>".format(user))
        sentences.append("Now, this user is now following <b>{}</b> users.".format(gh.get_user_following_number(user)))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.github_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    # Weather

    def generate_weather_status(self, weather_new, weather_before, city):
        title = "The weather is changing around " + city
        sentences = self.default()
        sentences.append("We have detected that the weather is changing around <b>{}</b>.<br>".format(city))
        sentences.append("Last time we checked the sky, the status was <b>{}</b>.".format(weather_before['sky']))
        sentences.append("<br>Now the status is <b>{}</b>.".format(weather_new['sky']))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.weather_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_weather_wind_speed(self, weather_new, weather_before, city):
        title = "Wind speed changes detected around " + city
        sentences = self.default()
        sentences.append("We have detected that the wind speed is changing in <b>{}</b>.<br>".format(city))
        sentences.append("When we last checked, the wind speed was around <b>{}km/h</b>.".format(weather_before['wind']['speed']))
        sentences.append("<br>Now it's about <b>{}km/h</b>.".format(weather_new['wind']['speed']))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.weather_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_weather_wind_direction(self, weather_new, weather_before, city):
        title = "Wind direction has changed in " + city
        sentences = self.default()
        sentences.append("We have detected that the wind direction degree has changed around <b>{}</b>.<br>".format(city))
        sentences.append("Last time we checked, the wind was going towards <b>{}°</b>.".format(weather_before['wind']['deg']))
        sentences.append("<br>The next direction degree is <b>{}°</b>.".format(weather_new['wind']['deg']))
        sentences.append("Which means the wind is going <b>{}</b>".format(weather_new['wind']['dir']))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.weather_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_weather_temperature(self, weather_new, weather_before, city):
        title = "Temperature is evolving around " + city
        sentences = self.default()
        sentences.append("We have detected that the weather is changing around <b>{}</b>.<br>".format(city))
        sentences.append("Last time we checked the temperatures, it was around <b>{}°C</b>.".format(weather_before['temperature']['temp']))
        sentences.append("<br>Now the temperature is <b>{}°C</b>.".format(weather_new['temperature']['temp']))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.weather_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_weather_humidy(self, weather_new, weather_before, city):
        title = "Humidity changes detected in " + city
        sentences = self.default()
        sentences.append("We have detected that the humidity level is changing around <b>{}</b>.<br>".format(city))
        sentences.append("Last time we checked the humidity, the percentage was <b>{}%</b>.".format(weather_before['sky']))
        sentences.append("<br>The new humidity percentage is now <b>{}%</b>.".format(weather_new['sky']))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.weather_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    # Youtube

    def generate_new_video_mail(self, video, channel):
        channel_info = channel['snippet']
        title = "A new video of '{}' is available".format(channel_info['title'])
        sentences = self.default()
        sentences.append("A new video has been posted on <b>{}'s</b> channel !".format(channel_info['title']))
        sentences.append("<br><br>The video is named <b>'{}'</b> and its description is: <br><br>".format(video['title']))
        sentences.append("<b>'{}'</b>".format(video['description']))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.yt_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_subscribers(self, channel, diff):
        title = "New subscribers detected for channel '{}'".format(channel['snippet']['title'])
        sentences = self.default()
        sentences.append("<b>{}</b> new subscribers have been detected since last check.".format(diff))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.yt_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_likes(self, video, diff):
        title = "New likes detected for video '{}'".format(video['snippet']['title'])
        sentences = self.default()
        sentences.append("<b>{}</b> new likes have been detected since last check.".format(diff))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.yt_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_comments(self, video, diff):
        title = "New comments detected for video '{}'".format(video['snippet']['title'])
        sentences = self.default()
        sentences.append("<b>{}</b> new comments have been detected since last check.".format(diff))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.yt_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_dislikes(self, video, diff):
        title = "New dislikes detected for video '{}'".format(video['snippet']['title'])
        sentences = self.default()
        sentences.append("<b>{}</b> new dislikes have been detected since last check.".format(diff))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.yt_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}

    def generate_new_views(self, video, diff):
        title = "New views detected for video '{}'".format(video['snippet']['title'])
        sentences = self.default()
        sentences.append("<b>{}</b> new views have been detected since last check.".format(diff))
        sentences.append(self.signature())
        sentences.append(self.add_image(self.yt_logo))
        return {'title': title, 'content': self.sentences_to_text(sentences)}
