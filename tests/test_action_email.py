import unittest
from unittest.mock import MagicMock
import yaml
from openpyxl import Workbook
import datetime
import exceltp.email_sender
from exceltp.config import *


class ActionEmailTestCase(unittest.TestCase):

    def test_do_email_configure(self):
        config_string = """
        subject: please read!!
        from: t_account@hotmail.com
        to: to@test.com
        smtp: smtp.live.com:587
        smtp_account: t_account@hotmail.com
        smtp_password : ThisIsPassword
        import_data : [a, b, e]
        msg: |
            hello
            expired time ...
            $import_data
            thank you
"""
        email_act = exceltp.email_sender.EmailAction(yaml.load(config_string))
        self.assertNotEqual(email_act.smtp_server, None)
        self.assertNotEqual(email_act.smtp_account, None)
        self.assertEqual(email_act.import_data[0], 'A')
        self.assertEqual(email_act.import_data[1], 'B')
        self.assertEqual(email_act.import_data[2], 'E')

    def test_do_email_action(self):
        config_string = """
        subject: please read!!
        from: t_account@hotmail.com
        to: to@test.com
        smtp: smtp.live.com:587
        smtp_account: t_account@hotmail.com
        smtp_password : ThisIsPassword
        import_data : [a,b]
        msg: |
            hello
            expired time ...
            $import_data
            thank you
"""
        email_act = exceltp.email_sender.EmailAction(yaml.load(config_string))

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

        email_act.do = MagicMock(return_value=True)
        self.assertEqual(email_act.do([row for row in ws1.rows]), True)

    def test_make_import_data(self):
        config_string = """
        subject: please read!!
        from: t_account@hotmail.com
        to: to@test.com
        smtp: smtp.live.com:587
        smtp_account: t_account@hotmail.com
        smtp_password : ThisIsPassword
        import_data : [a,b]
        msg: |
            hello
            expired time ...
            $import_data
            thank you
"""
        email_act = exceltp.email_sender.EmailAction(yaml.load(config_string))

        wb = Workbook()
        ws1 = wb.active
        ws1.title = "worksheet1"
        ws1['A2'] = datetime.datetime(2085, 3, 23)
        ws1['B2'] = 'Tony'
        ws1['C2'] = 'Seoul'

        msg = email_act._make_replace_msg(ws1)
        self.assertEqual(msg, '\n2085-03-23 00:00:00 Tony \n')
