from exceltp.define import *
from exceltp.email_sender import EmailAction
from exceltp.slack_webhook import SlackWebHook


class ActionManager:

    def __init__(self, action_conf):
        self.action = None
        self._parse_conf(action_conf)

    def _parse_conf(self, action_conf):
        if action_conf[ACTION_TYPE] == ACTION_EMAIL:
            self.action = EmailAction(action_conf[EMAIL_CONFIG])

        if action_conf[ACTION_TYPE] == ACTION_SLACK_WEBHOOK:
            self.action = SlackWebHook(action_conf[SLACK_WEBHOOK_CONFIG])

    def get_action_type(self):
        return self.action.get_type()

    def set_action(self, action):
        self.action = action

    def do_action(self, data):
        return self.action.do(data)
