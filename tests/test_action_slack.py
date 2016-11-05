import unittest
import yaml
import exceltp.slack_webhook
from exceltp.config import *
from unittest.mock import MagicMock
from openpyxl import Workbook
import datetime


class ActionSlackWebHookTestCase(unittest.TestCase):

    def test_webhook_configure(self):
        config_string = """
        url: https://hooks.slack.com/services/ttttt
        import_data: [b, c, d]
        msg: |
            please check data.
            $import_data
"""
        webhook = exceltp.slack_webhook.SlackWebHook(yaml.load(config_string))
        self.assertEqual(webhook.url, 'https://hooks.slack.com/services/ttttt')
        self.assertEqual(webhook.import_data[0], 'B')
        self.assertEqual(webhook.import_data[1], 'C')
        self.assertEqual(webhook.import_data[2], 'D')

    def test_do_webhook_action(self):
        config_string = """
        url: https://hooks.slack.com/services/T02Q9oaHvG
        import_data: [a, b]
        msg: |
            please check data.
            $import_data
"""
        webhook = exceltp.slack_webhook.SlackWebHook(yaml.load(config_string))

        wb = Workbook()
        ws1 = wb.active
        ws1.title = "worksheet1"
        ws1['A2'] = datetime.datetime(2085, 3, 23)
        ws1['A3'] = datetime.datetime(2016, 5, 8)
        ws1['A4'] = datetime.datetime(2017, 6, 14)
        ws1['B2'] = 'Tony'
        ws1['B3'] = 'Mike'
        ws1['B4'] = 'Lee'
        ws1['C2'] = 'Seoul'
        ws1['C3'] = 'London'
        ws1['C4'] = 'New York'

        webhook.do = MagicMock(return_value=True)
        self.assertEqual(webhook.do([row for row in ws1.rows]), True)
