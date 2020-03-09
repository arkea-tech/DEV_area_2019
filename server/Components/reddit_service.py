import praw

from Secrets.APIKeys import reddit_credentials as credentials

# Documentation: https://praw.readthedocs.io/en/latest/
# Classes: https://praw.readthedocs.io/en/latest/code_overview/praw_models.html


reddit = praw.Reddit(client_id=credentials['client_id'],
                     client_secret=credentials['client_secret'],
                     user_agent=credentials['user_agent'],
                     username=credentials['username'],
                     password=credentials['password'])

class Service:
    def __init__(self, name='', description='', actions=[], reactions=[]):
        self.name = name
        self.description = description
        self.actions = actions
        self.reactions = reactions

class Reddit(Service):
    def __init__(self):
        super().__init__(name='Reddit')
        self.actions = ["detect_new_subreddit_post", "detect_new_subreddit_comment", "detect_new_user_post", "detect_new_user_comment"]
        self.reactions = ['reply_submission', 'message_user']

    def get_subreddit_last_post(self, name):
        """
        Get this subreddit lastest submission. Can be compared with '==' and '!='
        :return: https://praw.readthedocs.io/en/latest/code_overview/models/submission.html
        """
        for submission in reddit.subreddit(name).new(limit=1):
            return submission

    def get_subreddit_last_comment(self, name):
        """
        Get this subreddit lastest comment. Can be compared with '==' and '!='
        :return: https://praw.readthedocs.io/en/latest/code_overview/models/comment.html
        """
        for comment in reddit.subreddit(name).comments(limit=1):
            return comment

    def get_user_last_post(self, username):
        """
        Get this user lastest submission. Can be compared with '==' and '!='
        :return: https://praw.readthedocs.io/en/latest/code_overview/models/submission.html
        """
        for submission in reddit.redditor(username).new(limit=1):
            return submission
        
    def get_user_last_comment(self, username):
        """
        Get this user lastest comment. Can be compared with '==' and '!='
        :return: https://praw.readthedocs.io/en/latest/code_overview/models/comment.html
        """
        for comment in reddit.redditor(username).comments.new(limit=1):
            return comment

    def reply_to_submission(self, link, body):
        """
        Reply to this submission
        Documentation: https://praw.readthedocs.io/en/latest/code_overview/models/submission.html#praw.models.Submission.reply
        """
        reddit.submission(url=link).reply(body)

    def message_user(self, username, subject, message):
        """
        Message this user
        Documentation: https://praw.readthedocs.io/en/latest/code_overview/models/redditor.html#praw.models.Redditor.message
        """
        reddit.redditor(username).message(subject, message)

    def get_body_from_post(self, post):
        """
        Get the content of a Reddit post
        """
        msg = post.selftext
        if msg == "":
            return post.url
        return msg

    def get_body_from_comment(self, comment):
        """
        Get the content of the last comment of a Reddit user
        """
        return comment.body
