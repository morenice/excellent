import unittest
from excellent.action_manager import *
from excellent.config import *


class ActionManagerTestCase(unittest.TestCase):

    def test_parse_email_conf(self):
        config_string = """
config_version: 0.1
action:
    type: email
    email_config:
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
        config = Config(None)
        config.read_raw_data(config_string)

        am = ActionManager(config.get_action_conf())
        self.assertEqual(am.get_action_type(), ACTION_EMAIL)
