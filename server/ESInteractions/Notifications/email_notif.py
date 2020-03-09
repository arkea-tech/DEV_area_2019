
import json
from flask import Blueprint
from flask import request
from Components.mailjet_service import MailNotif


notifier = MailNotif()

send_email_to_user = Blueprint('send_email_to_user', __name__)


@send_email_to_user.route('/', methods=['POST'])
def action():
    """
    Endpoint that allows the client to check if an account exists and/or is correct
    :return: json
    """
    if request.method == "POST":
        params = request.get_data()
        params = json.loads(params.decode('utf-8'))
        status = notifier.send_email_to(params["email"], params["subject"], params["text"])
        if status == 200:
            return json.dumps({"status": 200, "msg": "Email sent successfully"}, indent=4)
        else:
            return json.dumps({"status": 400, "msg": "Failed to send email"}, indent=4)
    else:
        return json.dumps({"status": 400, "msg": "You have to do a POST request to use this endpoint"}, indent=4)

