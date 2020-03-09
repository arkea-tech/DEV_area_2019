
import json
from flask import Blueprint
from flask import request
from Components.weather_service import Weather


w = Weather()

get_weather_for_city = Blueprint('get_weather_for_city', __name__)


@get_weather_for_city.route('/', methods=['GET'])
def action():
    """
    Endpoint that allows the client to check if an account exists and/or is correct
    :return: json
    """
    if request.method == "GET":
        params = request.get_data()
        params = json.loads(params.decode('utf-8'))
        forec = w.get_weather_for_city(params["city"])
        return json.dumps({"status": 200, "msg": "Getting forecast succeded", "data": forec}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a GET request to use this endpoint"}, indent=4)

