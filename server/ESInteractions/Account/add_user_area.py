
import json
from flask import Blueprint
from flask import request

from Utils.checker import Checker
from Components.elasticsearch_interface import ElasticSearchInterface
from Components.area_preparer import Preparer

esi = ElasticSearchInterface()
preparer = Preparer()
checker = Checker()

add_user_area = Blueprint('add_user_area', __name__)


def fix_str(string):
    if '_' in string:
        return string
    name = string.lower()
    name = name.split(' ')
    name = '_'.join(name)
    return name


@add_user_area.route('/', methods=['POST'])
def action():
    """
    Endpoint that allows the client to add an AREA to an account
    :return: json
    """
    if request.method == "POST":
        params = request.get_data()
        params = json.loads(params.decode('utf-8'))
        if esi.account_uuid_exists(params['uuid']) is False:
            return json.dumps({"status": 400, "msg": "Account does not exists"}, indent=4)
        if checker.is_service_type_ok(params["service"]) is False:
            return json.dumps({"status": 400, "msg": "Unknown service... Please choose one of them: [youtube, weather, deezer, timer, mail, calendar, reddit, yammer]"}, indent=4)
        services = esi.get_user_services(params['uuid'])
        service_data = {'service': params['service'], 'action': fix_str(params['action']), 'action_data': params['action_data'],
                        'reaction': fix_str(params['reaction']), 'reaction_data': params['reaction_data'], 'enabled': True}
        try:
            service_data = preparer.prepare_service(service_data)
        except:
            service_data = {}
        if service_data == {}:
            return json.dumps({"status": 400, "msg": "An error while verifying the AREA, please check the form"}, indent=4)
        services.append(service_data)
        esi.es.update(index='accounts', id=params['uuid'], body={"doc": {"services": services}})
        esi.es.indices.refresh(index='accounts')
        return json.dumps({"status": 200, "msg": "AREA successfully created and added to your account !"}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a POST request to use this endpoint"}, indent=4)
