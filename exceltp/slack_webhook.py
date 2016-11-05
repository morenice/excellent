# -*- coding: utf-8 -*-
"""
curl base webhook
 - http://pycurl.sourceforge.net/doc/quickstart.html#retrieving-a-network-resource
 - sample(curl program)
   - curl -X POST --data-urlencode 'payload={"text":"test msg"}' URL
"""

import pycurl
import exceltp.action
from exceltp.define import *

try:
    # for python 3
    from urllib.parse import urlencode
except ImportError:
    # for python 2
    from urllib import urlencode


class SlackWebHook(exceltp.action.Action):

    def __init__(self, webhook_conf):
        self.action_type = ACTION_SLACK_WEBHOOK
        self._parse_conf(webhook_conf)

    def _parse_conf(self, webhook_conf):
        self.url = webhook_conf[SLACK_WEBHOOK_URL]
        self.msg = webhook_conf[SLACK_WEBHOOK_MSG]
        self.import_data = None
        if SLACK_WEBHOOK_IMPORT_DATA in webhook_conf:
            self.import_data = webhook_conf[SLACK_WEBHOOK_IMPORT_DATA]
            for i, data in enumerate(self.import_data):
                self.import_data[i] = str(data).upper()

    def _send(self, msg):
        c = pycurl.Curl()
        c.setopt(c.URL, self.url)

        postData = {'payload': '{"text":"' + msg + '"}'}
        postField = urlencode(postData)
        c.setopt(c.POSTFIELDS, postField)

        c.perform()
        c.close()

    def _make_replace_msg(self, data):
        # :data Workbook
        replaced_format_data = ""
        for row in data:
            for cell in row:
                if cell.value is None:
                    continue

                if self.import_data is None:
                    replaced_format_data += str(cell.value)
                    replaced_format_data += ' '
                    continue

                if cell.column.upper() in self.import_data:
                    replaced_format_data += str(cell.value)
                    replaced_format_data += ' '

            replaced_format_data += '\n'
        return replaced_format_data

    def do(self, data):
        # prepare replace word to value
        replace_msg = self._make_replace_msg(data)

        # replace import_data
        new_msg = self.msg.replace('$import_data', replace_msg)
        self._send(new_msg)
