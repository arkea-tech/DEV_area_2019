
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


user = "area.notifier.2020@gmail.com"
pw = "areanotifier"

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
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = email
        msg.attach(MIMEText(text, 'html'))
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, pw)
        server.sendmail(user, email, msg.as_string())
        server.close()
        return True
