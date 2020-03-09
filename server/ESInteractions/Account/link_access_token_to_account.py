
import json
from flask import Blueprint
from flask import request
import requests

from Utils.checker import Checker
from Components.elasticsearch_interface import ElasticSearchInterface
from Secrets.APIKeys import yammer_credentials

esi = ElasticSearchInterface()

link_access_token = Blueprint('link_access_token', __name__)


@link_access_token.route('/', methods=['POST'])
def action():
    """
    Endpoint that link an access token of a service to a user
    :return: json
    """
    if request.method == "POST":
        params = request.get_data()
        params = json.loads(params.decode('utf-8'))
        esi.create_index('accounts')
        if esi.account_uuid_exists(params['uuid']) is False:
            return json.dumps({"status": 400, "msg": "This account does not exist, please use another one."}, indent=4)
        else:
            if Checker().is_service_type_ok(params['service']) is False:
                return json.dumps({"status": 400, "msg": "Unknown service."},
                                  indent=4)
            user = esi.get_user_from_uuid(params['uuid'])
            if params['service'] == "yammer":
                auth_token = params['access_token']
                url = "https://www.yammer.com/oauth2/access_token.json?client_id={}&client_secret={}&code={}".format(
                    yammer_credentials['client_id'],
                    yammer_credentials['client_secret'],
                    auth_token
                )
                r = requests.get(url=url)
                data = r.json()
                user['access_tokens']["{}".format(params['service'])] = data['access_token']['token']
            else:
                user['access_tokens']["{}".format(params['service'])] = params['access_token']
            esi.update_user_tokens(params['uuid'], user['access_tokens'])
            return json.dumps({"status": 200, "msg": "Access token linked with success !"}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a POST request to use this endpoint"}, indent=4)
