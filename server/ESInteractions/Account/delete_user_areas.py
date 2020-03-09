
import json
from flask import Blueprint
from flask import request

from Components.elasticsearch_interface import ElasticSearchInterface

esi = ElasticSearchInterface()


delete_user_area = Blueprint('delete_user_area', __name__)


@delete_user_area.route('/', methods=['POST'])
def action():
    """
    Endpoint that allows the client to delete all user's area
    :return: json
    """
    if request.method == "POST":
        params = request.get_data()
        params = json.loads(params.decode('utf-8'))
        if esi.account_uuid_exists(params['uuid']) is False:
            return json.dumps({"status": 400, "msg": "Account does not exists"}, indent=4)
        esi.delete_user_services(params['uuid'])
        return json.dumps({"status": 200, "msg": "Deleting user's AREAs..."}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a POST request to use this endpoint"}, indent=4)
