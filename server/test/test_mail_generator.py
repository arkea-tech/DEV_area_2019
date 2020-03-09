
import unittest

from Utils.mail_generator import MailGenerator

mg = MailGenerator()


weather_mockup = {'temperature': {'temp': 11.23, 'temp_max': 12.22, 'temp_min': 10.0, 'temp_kf': None}, 'wind': {'speed': 8.2, 'deg': 240}, 'humidity': 62, 'sky': 'Clouds'}
weather_mini_mockup = {'title': 'The weather is changing in Paris', 'content': "<br>Hello,<br><br> We have detected that the weather is changing around Paris The temperature is now around 11.23°C and it's Clouds. <br><br>The wind speed is {'speed': 8.2, 'deg': 240} km/h and humidity is at 62%. <br><br>Best regards,<br>AREA Notifier"}
weather_global_mockup = {'title': 'Weather Summary for Paris', 'content': '<br>Hello,<br><br> Here is your weather summary for today in Paris.<br> The temperature is currently around 11.23°C. The minimal temperature planned for today is 10.0°C and the maximum is 12.22°C. <br><br>The wind speed is approximativly 8.2 km/h and the humidity level is at 62%. <br><br>Best regards,<br>AREA Notifier'}
channel_info_mockup = {'kind': 'youtube#channel', 'etag': '"Fznwjl6JEQdo1MGvHOGaz_YanRU/sBv1MqgSziMRuTmQ7uaHNap-pXA"', 'id': 'UCaNlbnghtwlsGF-KzAFThqA', 'snippet': {'title': 'ScienceEtonnante', 'description': 'Des vidéos pour raconter la science étonnante, amusante, passionnante et stupéfiante !\n\nRetrouvez moi aussi sur mon blog "Science étonnante" http://sciencetonnante.wordpress.com\nSoutenez-moi sur Tipeee : https://www.tipeee.com/science-etonnante', 'customUrl': 'scienceetonnante', 'publishedAt': '2011-01-04T19:46:19.000Z', 'thumbnails': {'default': {'url': 'https://yt3.ggpht.com/a/AGF-l78y7V9g14mK8St90ddJeOiD0eIwSWPZw3DQsQ=s88-c-k-c0xffffffff-no-rj-mo', 'width': 88, 'height': 88}, 'medium': {'url': 'https://yt3.ggpht.com/a/AGF-l78y7V9g14mK8St90ddJeOiD0eIwSWPZw3DQsQ=s240-c-k-c0xffffffff-no-rj-mo', 'width': 240, 'height': 240}, 'high': {'url': 'https://yt3.ggpht.com/a/AGF-l78y7V9g14mK8St90ddJeOiD0eIwSWPZw3DQsQ=s800-c-k-c0xffffffff-no-rj-mo', 'width': 800, 'height': 800}}, 'localized': {'title': 'ScienceEtonnante', 'description': 'Des vidéos pour raconter la science étonnante, amusante, passionnante et stupéfiante !\n\nRetrouvez moi aussi sur mon blog "Science étonnante" http://sciencetonnante.wordpress.com\nSoutenez-moi sur Tipeee : https://www.tipeee.com/science-etonnante'}, 'country': 'FR'}, 'contentDetails': {'relatedPlaylists': {'uploads': 'UUaNlbnghtwlsGF-KzAFThqA', 'watchHistory': 'HL', 'watchLater': 'WL'}}, 'statistics': {'viewCount': '53844317', 'commentCount': '0', 'subscriberCount': '833000', 'hiddenSubscriberCount': False, 'videoCount': '86'}}
video_mockup = {'title': 'La « température ressentie » : une arnaque ? ❄️🌡️🥶', 'description': 'La "température ressentie", est-ce que c\'est très scientifique comme idée ? En fait pas vraiment, mais c\'est une bonne occasion de parler des transferts de ...', 'publish_date': '2020-02-07T16:00:03.000Z'}
new_video_mail_mockup = {'title': "A new video of 'ScienceEtonnante' is available", 'content': '<br>Hello,<br><br> A new video has been posted on the ScienceEtonnante\'s channel ! <br><br>The video is named \'La « température ressentie » : une arnaque ? ❄️🌡️🥶\' and its description is: <br><br> \'La "température ressentie", est-ce que c\'est très scientifique comme idée ? En fait pas vraiment, mais c\'est une bonne occasion de parler des transferts de ...\' <br><br>Best regards,<br>AREA Notifier'}

class TestChecker(unittest.TestCase):

    def test_linebreak(self):
        self.assertEqual(mg.linebreak(), "<br><br>")

    def test_default(self):
        self.assertEqual(mg.default(), ["<br>Hello,<br><br>"])

    def test_signature(self):
        self.assertEqual(mg.signature(), "<br><br>Best regards,<br>AREA Notifier")

    def test_sentences_to_text(self):
        data = ["coucou", "test", "ok"]
        expected = "coucou test ok"
        self.assertEqual(mg.sentences_to_text(data), expected)

    def test_generate_timer_mail(self):
        mail = mg.generate_timer_mail()
        sentences = mg.default()
        sentences.append("The timer you've previously defined has ended.")
        sentences.append("<br>The REAction has been triggered !")
        sentences.append(mg.signature())
        expected = mg.sentences_to_text(sentences)
        self.assertEqual(mail, {'title': "Your timer has ended", 'content': expected})
        return

    def test_generate_minimal_weather_mail(self):
        mail = mg.generate_minimal_weather_mail(weather_mockup, 'Paris')
        self.assertEqual(mail, weather_mini_mockup)

    def test_generate_global_weather_mail(self):
        self.maxDiff = None
        mail = mg.generate_global_weather_mail(weather_mockup, 'Paris')
        self.assertEqual(mail, weather_global_mockup)

    # def test_generate_new_video_mail(self):
    #     self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
