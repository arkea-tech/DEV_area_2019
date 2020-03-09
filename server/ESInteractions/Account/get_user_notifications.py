
import json
from flask import Blueprint
from flask import request

from Components.elasticsearch_interface import ElasticSearchInterface

esi = ElasticSearchInterface()

get_user_notifs = Blueprint('get_user_notifs', __name__)


@get_user_notifs.route('/', methods=['GET'])
def action():
    """
    Endpoint that allows the client to create an account if the parameters passed are correct
    :return: json
    """
    if request.method == "GET":
        params = request.get_data()
        params = json.loads(params.decode('utf-8'))
        if esi.account_uuid_exists(params['uuid']) is False:
            return json.dumps({"status": 400, "msg": "Account does not exists"}, indent=4)
        notifs = esi.get_user_notifs(uuid=params['uuid'])
        return json.dumps({"status": 200, "msg": "Get user notifications success !", "data": notifs}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a GET request to use this endpoint"}, indent=4)
