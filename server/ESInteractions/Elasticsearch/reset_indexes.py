
import json
from flask import Blueprint
from flask import request

from Components.elasticsearch_interface import ElasticSearchInterface

esi = ElasticSearchInterface()

reset_indexes = Blueprint('reset_indexes', __name__)


@reset_indexes.route('/', methods=['POST'])
def action():
    """
    Endpoint that resets the index 'accounts' (BACKEND ONLY / NOT FOR CLIENT)
    :return: json
    """
    if request.method == "POST":
        params = request.get_data()
        esi.reset_index('accounts')
        return json.dumps({"status": 200, "msg": "Index reset with success !"}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a POST request to use this endpoint"}, indent=4)
