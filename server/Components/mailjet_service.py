
from mailjet_rest import Client
from Secrets.APIKeys import mailjet as mj


class MailNotif:

    def __init__(self):
        self.name = "Mail"
        self.description = "This service is used mainly as a reaction service."
        self.actions = []
        self.reactions = [{'name': 'email_notification', 'description': 'An email is sent to the connected user'}]

    @staticmethod
    def send_email_to(email, subject, text):
        """
        Send an email to a specific email adress
        :param email: adress to send to
        :param subject: mail title
        :param text: mail content
        """
        mailjet = Client(auth=(mj['api_key'], mj['api_secret']), version='v3.1')
        data = {
          'Messages': [
            {
              "From": {
                "Email": "area.notifier@gmail.com",
                "Name": "AREA Notifier"
              },
              "To": [
                {
                  "Email": email,
                  "Name": "AREA User"
                }
              ],
              "Subject":  subject,
              "TextPart": text,
              "HTMLPart": text,
              "CustomID": "AppGettingStartedTest"
            }
          ]
        }
        result = mailjet.send.create(data=data)
        return result.status_code
