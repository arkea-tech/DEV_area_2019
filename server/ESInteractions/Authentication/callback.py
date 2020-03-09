from flask import Blueprint
from flask import Request

callback = Blueprint('callback', __name__, url_prefix='/callback')

# OAuth2 @ https://github.com/reddit-archive/reddit/wiki/oauth2

# https://www.reddit.com/api/v1/authorize[.compact]
# ?client_id=CLIENT_ID
# &response_type=TYPE
# &state=RANDOM_STRING
# &redirect_uri=URI&duration=DURATION
# &scope=SCOPE_STRING


# Token retrieval
#
# https://www.reddit.com/api/v1/access_token
# Post request data: grant_type=authorization_code&code=CODE&redirect_uri=URI
#
# {
#     "access_token": Your access token,
#     "token_type": "bearer",
#     "expires_in": Unix Epoch Seconds,
#     "scope": A scope string,
#     "refresh_token": Your refresh token
# }

# Token refresh
#
# https://www.reddit.com/api/v1/access_token
# Post request data: grant_type=refresh_token&refresh_token=TOKEN
#
# {
#     "access_token": Your access token,
#     "token_type": "bearer",
#     "expires_in": Unix Epoch Seconds,
#     "scope": A scope string,
# }


@callback.route('/reddit', methods=['POST'])
def action():
    """
    Endpoint for Reddit OAuth2 application callback
    """
    if request.method == "POST":
        oauth2 = request.get_data()
        oauth2 = json.loads(params.decode('utf-8'))
