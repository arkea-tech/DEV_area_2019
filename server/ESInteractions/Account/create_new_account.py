
import json
import random
from flask import Blueprint
from flask import request


from Components.elasticsearch_interface import ElasticSearchInterface

esi = ElasticSearchInterface()

create_new_account = Blueprint('create_new_account', __name__)


@create_new_account.route('/', methods=['POST'])
def action():
    """
    Endpoint that allows the client to create an account if the parameters passed are correct
    :return: json
    """
    if request.method == "POST":
        params = request.get_data()
        params = json.loads(params.decode('utf-8'))
        esi.create_index('accounts')
        if esi.account_already_exists(params['email']) is True:
            return json.dumps({"status": 400, "msg": "This email is already used, please use another one."}, indent=4)
        else:
            if params['password'] != params['confirm_password']:
                return json.dumps({"status": 400, "msg": "Passwords are not the same, please verify them."}, indent=4)
            key = '%030x' % random.randrange(16 ** 30)
            params['uuid'] = key
            params['notifications'] = ["Account created successfully !"]
            params['services'] = []
            params['access_tokens'] = {}
            del params['confirm_password']
            esi.es.index(index='accounts', id=key, body=params)
            esi.es.indices.refresh(index='accounts')
            return json.dumps({"status": 200, "msg": "Account created with success !", "uuid": key}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a POST request to use this endpoint"}, indent=4)
