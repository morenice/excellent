import unittest
from excellent.config import *


class TestConfig(unittest.TestCase):
    data_path = "tests/config/"

    def test_no_yml_file(self):
        conf = Config(self.data_path + "no_yml_file.yml")
        self.assertEqual(conf.read(), -1)

    def test_no_file(self):
        conf = Config(self.data_path + "no_file.yml")
        self.assertEqual(conf.read(), -2)

    def test_success_analyzer_and_action(self):
        conf = Config(self.data_path + "success_analyze_action.yml")
        self.assertEqual(conf.read(), 0)
        self.assertNotEqual(conf.get_analyzer_conf(), None)
        self.assertNotEqual(conf.get_action_conf(), None)

    def test_success_analyzer(self):
        conf = Config(self.data_path + "success_analyze.yml")
        self.assertEqual(conf.read(), 0)
        self.assertNotEqual(conf.get_analyzer_conf(), None)
        self.assertEqual(conf.get_action_conf(), None)

    def test_success_action(self):
        conf = Config(self.data_path + "success_action.yml")
        self.assertEqual(conf.read(), 0)
        self.assertEqual(conf.get_analyzer_conf(), None)
        self.assertNotEqual(conf.get_action_conf(), None)

    def test_fail_analyzer(self):
        conf = Config(self.data_path + "fail_analyze.yml")
        self.assertEqual(conf.read(), 0)
        self.assertEqual(conf.get_analyzer_conf(), None)
        self.assertEqual(conf.get_action_conf(), None)

    def test_fail_action(self):
        conf = Config(self.data_path + "fail_action.yml")
        self.assertEqual(conf.read(), 0)
        self.assertEqual(conf.get_analyzer_conf(), None)
        self.assertEqual(conf.get_action_conf(), None)
