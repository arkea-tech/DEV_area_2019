from flask import Flask
from flask import send_file
from flask import request
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

import json
import sys
import random
import datetime
import atexit
from time import sleep

from Components.elasticsearch_interface import ElasticSearchInterface
from Components.updater_service import Updater

from ESInteractions.Account.create_new_account import create_new_account
from ESInteractions.Account.get_all_accounts import get_all_accounts
from ESInteractions.Account.is_account_ok import is_account_ok
from ESInteractions.Elasticsearch.reset_indexes import reset_indexes
from ESInteractions.Weather.get_weather_for_city import get_weather_for_city
from ESInteractions.Notifications.email_notif import send_email_to_user
from ESInteractions.Youtube.get_channel_info import get_channel_info
from ESInteractions.Account.add_user_area import add_user_area
from ESInteractions.Account.get_user_areas import get_user_areas
from ESInteractions.Account.refresh_user_areas import update_user_area
from ESInteractions.Account.get_user_notifications import get_user_notifs
from ESInteractions.Account.link_access_token_to_account import link_access_token
from ESInteractions.Account.delete_user_areas import delete_user_area

from about_json import about as info

sys.stdout.flush()

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['JSON_SORT_KEYS'] = False

updater = Updater()


def update():
    updater.update_users_services()


scheduler = BackgroundScheduler()
scheduler.add_job(func=update, trigger="interval", seconds=60)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


# List all the endpoints here
endpoints = [
    (create_new_account, '/create_new_account'),
    (get_all_accounts, '/get_all_accounts'),
    (reset_indexes, '/reset_indexes'),
    (is_account_ok, '/is_account_ok'),
    (get_weather_for_city, '/get_weather_for_city'),
    (send_email_to_user, '/send_email_to_user'),
    (get_channel_info, '/get_latest_videos'),
    (add_user_area, '/add_user_area'),
    (get_user_areas, '/get_user_areas'),
    (update_user_area, '/update_user_area'),
    (get_user_notifs, '/get_user_notifs'),
    (link_access_token, '/link_access_token'),
    (delete_user_area, '/delete_user_areas')
]


@app.route('/')
def home():
    """
    Home page of API, join this URL to setup Elasticsearch on client-side
    :return: message
    """
    esi = ElasticSearchInterface()
    # Add the line below for every indexes that have to be created (atm, only 'accounts')
    esi.create_index('accounts')
    return json.dumps({"msg": "Welcome on the home of the AREA RestAPI"}, indent=4)


@app.route('/about.json')
def about():
    """
    Page that describes all services of our project
    :return: about.json
    """
    info['client']['host'] = request.remote_addr
    info['server']['current_time'] = int(datetime.datetime.now().timestamp())
    return json.dumps(info, indent=4), {'Content-Type': 'application/json'}


@app.route('/client.apk')
def mobile():
    """
    Redirect for the client_web
    :return: file
    """
    return send_file('/shared/client.apk')


for module, link in endpoints:
    app.register_blueprint(module, url_prefix=link)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
    print("Server is running")
