
import json
from flask import Blueprint
from flask import request
from Components.youtube_service import Youtube

yt = Youtube()

get_channel_info = Blueprint('get_channel_info', __name__)


@get_channel_info.route('/', methods=['GET'])
def action():
    """
    Endpoint that allows the client to check if an account exists and/or is correct
    :return: json
    """
    if request.method == "GET":
        params = request.get_data()
        params = json.loads(params.decode('utf-8'))
        id = params['channel']
        if params['by_username'] and params['by_username'] is True:
            id = yt.get_channel_id_by_username(params['channel'])
        info = yt.get_latest_videos_by_channel_id(id, 1)
        if info[0] == 200:
            return json.dumps({"status": 200, "msg": "Getting channel info succeded", "data": info[1]}, indent=4)
        else:
            return json.dumps({"status": 400, "msg": "Could not find channel", "data": {}}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a GET request to use this endpoint"}, indent=4)

