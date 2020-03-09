
import json
from flask import Blueprint
from flask import request

from Components.elasticsearch_interface import ElasticSearchInterface

esi = ElasticSearchInterface()

get_all_accounts = Blueprint('get_all_accounts', __name__)


@get_all_accounts.route('/', methods=['GET'])
def action():
    """
    Endpoint that return all accounts currently registered in ES
    :return: json
    """
    if request.method == "GET":
        esi.create_index('accounts')
        res = esi.es.search(index='accounts', body={})
        res = res['hits']['hits']
        lst = []
        for elem in res:
            lst.append(elem['_source'])
        return json.dumps({"status": 200, "accounts": lst}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a GET request to use this endpoint"}, indent=4)

