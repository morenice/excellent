# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from email.message import EmailMessage
import smtplib
from exceltp.config_define import *


class Action:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.action_type = None

    @abstractmethod
    def do(self, data):
        pass

    def get_type(self):
        return self.action_type


class EmailAction(Action):
    def __init__(self, email_conf):
        self.action_type = ACTION_EMAIL
        self._parse_conf(email_conf)

    def _parse_conf(self, email_conf):
        self.email_from = email_conf[EMAIL_FROM]
        self.email_to = email_conf[EMAIL_TO]

        self.smtp_server = email_conf[EMAIL_SMTP].split(':')[0]
        self.smtp_port = int(email_conf[EMAIL_SMTP].split(':')[1])
        self.smtp_account = email_conf[EMAIL_SMTP_USER]
        self.smtp_password = email_conf[EMAIL_SMTP_PASSWD]

        self.subject = email_conf[EMAIL_SUBJECT]
        self.msg = email_conf[EMAIL_MSG]

    def _make_send_msg(self, data):
        # replace word to value
        replaced_format_data = ""
        for row in data:
            for cell in row:
                if cell.value is None:
                    continue
                replaced_format_data += str(cell.value)
                replaced_format_data += ' '
            replaced_format_data += '\n'

        # replace import_data
        new_msg = self.msg.replace('$import_data', replaced_format_data)
        return new_msg

    def _send(self, msg_content):
        # reference
        # - https://docs.python.org/3/library/email-examples.html
        send_msg = EmailMessage()
        send_msg['From'] = self.email_from

        # TODO: multiple 'email_to' => support list
        send_msg['To'] = self.email_to
        send_msg['Subject'] = self.subject
        send_msg.set_content(msg_content)

        s = smtplib.SMTP(self.smtp_server, self.smtp_port)

        # Hostname to send for this command defaults
        #  to the fully qualified domain name of the local host.
        s.ehlo()

        # Puts connection to SMTP server in TLS mode
        s.starttls()
        s.ehlo()

        s.login(self.smtp_account, self.smtp_password)
        s.set_debuglevel(1)

        s.send_message(send_msg)
        s.quit()

    def do(self, data):
        msg_content = self._make_send_msg(data)
        self._send(msg_content)
