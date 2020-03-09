
import json
from flask import Blueprint
from flask import request

from Components.elasticsearch_interface import ElasticSearchInterface

esi = ElasticSearchInterface()

is_account_ok = Blueprint('is_account_ok', __name__)


@is_account_ok.route('/', methods=['POST'])
def action():
    """
    Endpoint that allows the client to check if an account exists and/or is correct
    :return: json
    """
    if request.method == "POST":
        params = request.get_data()
        params = json.loads(params.decode('utf-8'))
        res = esi.es.search(index='accounts', body={})
        res = res['hits']['hits']
        for elem in res:
            if elem['_source']['email'] == params['email'] and elem['_source']['password'] == params['password']:
                return json.dumps({"status": 200, "msg": "Account is correct", "uuid": elem['_source']['uuid']}, indent=4)
        return json.dumps({"status": 400, "msg": "Account doesn't exist or email/password is incorrect"}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a POST request to use this endpoint"}, indent=4)

