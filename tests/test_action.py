import unittest
import yaml
from openpyxl import Workbook
import datetime
import excellent.action
from excellent.config import *


class ActionEmailTestCase(unittest.TestCase):
    def create_action_email(self, config_string):
        email_config = yaml.load(config_string)
        return excellent.action.EmailAction(email_config)

    # TODO: email send test with mock object
    def test_do_email_action(self):
        config_string = """
        subject: please read!!
        from: t_account@hotmail.com
        to: to@test.com
        smtp: smtp.live.com:587
        smtp_account: t_account@hotmail.com
        smtp_password : ThisIsPassword
        msg: |
            hello
            expired time ...
            $import_data
            thank you
        import_data: |
            $B $C
"""
        email_act = excellent.action.EmailAction(yaml.load(config_string))

        # TODO: make data
        wb = Workbook()
        ws1 = wb.active
        ws1.title = "worksheet1"
        ws1['A1'] = 'Due date'
        ws1['A2'] = datetime.datetime(2085, 3, 23)
        ws1['A3'] = datetime.datetime(2016, 5, 8)
        ws1['A4'] = datetime.datetime(2017, 6, 14)
        ws1['A5'] = datetime.datetime(2018, 8, 23)
        ws1['B1'] = 'Name'
        ws1['B2'] = 'Tony'
        ws1['B3'] = 'Mike'
        ws1['B4'] = 'Lee'
        ws1['C1'] = 'Address'
        ws1['C2'] = 'None'
        ws1['C3'] = 'None'

        #email_act.do(data)
