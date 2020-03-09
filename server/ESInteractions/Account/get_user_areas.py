
import json
from flask import Blueprint
from flask import request

from Components.elasticsearch_interface import ElasticSearchInterface

esi = ElasticSearchInterface()


get_user_areas = Blueprint('get_user_areas', __name__)


@get_user_areas.route('/', methods=['GET'])
def action():
    """
    Endpoint that allows the client to create an account if the parameters passed are correct
    :return: json
    """
    if request.method == "GET":
        params = request.get_data()
        uuid = request.args.get('uuid')
        if esi.account_uuid_exists(uuid) is False:
            return json.dumps({"status": 400, "msg": "Account does not exists"}, indent=4)
        services = esi.get_user_services(uuid=uuid)
        return json.dumps({"status": 200, "msg": "Get user services success !", "data": services}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a GET request to use this endpoint"}, indent=4)
