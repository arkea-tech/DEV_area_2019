
import pyowm
from Secrets.APIKeys import owm as key


class Weather:

    def __init__(self):
        self.name = "Weather"
        self.description = "This service is all about weather broadcasting."
        self.actions = ["detect_weather", "detect_temperature", "detect_humidity", "detect_wind_speed", "detect_wind_direction"]
        self.reactions = []

    @staticmethod
    def get_dir_from_degree(degree):
        """
        Return direction based on degree
        :param degree: wind direction degree
        :return: direction
        """
        if 316 <= degree <= 360 or 0 <= degree <= 45:
            return "north"
        if 46 <= degree <= 135:
            return "east"
        if 136 <= degree <= 225:
            return "south"
        if 226 <= degree <= 315:
            return "west"

    def get_global_weather_for_city(self, city):
        """
        Return a global dictionary containing all important weather information
        :param city: city to get weather for
        """
        owm = pyowm.OWM(key['key'])
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        dct = {'temperature': w.get_temperature('celsius'), 'wind': w.get_wind(), 'humidity': w.get_humidity(), 'sky': w.get_status()}
        dct['wind']['dir'] = self.get_dir_from_degree(dct['wind']['deg'])
        return dct

    @staticmethod
    def get_weather_status_for_city(city):
        """
        Get the current weather sky status
        :param city: city name
        """
        owm = pyowm.OWM(key['key'])
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        dct = {'sky': w.get_status()}
        return dct

    def get_wind_for_city(self, city):
        """
        Get the wind information
        :param city: city name
        """
        owm = pyowm.OWM(key['key'])
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        dct = {'wind': w.get_wind()}
        dct['wind']['dir'] = self.get_dir_from_degree(dct['wind']['deg'])
        return dct

    @staticmethod
    def get_temperatures_for_city(city):
        """
        Get the current temperatures
        :param city: city name
        """
        owm = pyowm.OWM(key['key'])
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        dct = {'temperature': w.get_temperature('celsius')}
        return dct

    @staticmethod
    def get_humidity_for_city(city):
        """
        Get the current humidity level
        :param city: city name
        """
        owm = pyowm.OWM(key['key'])
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        dct = {'humidity': w.get_humidity()}
        return dct