import unittest
from excellent.config import *


class TestConfig(unittest.TestCase):
    data_path = "tests/config/"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_yml_file(self):
        conf = Config(self.data_path + "no_yml_file.yml")
        self.assertEqual(conf.read(), -1)

    def test_no_file(self):
        conf = Config(self.data_path + "no_file.yml")
        self.assertEqual(conf.read(), -2)

    def test_success_analyzer_and_action(self):
        conf = Config(self.data_path + "success_analyze_action.yml")
        self.assertEqual(conf.read(), 0)

    def test_success_analyzer(self):
        conf = Config(self.data_path + "success_analyze.yml")
        self.assertEqual(conf.read(), 0)

    def test_fail_analyzer(self):
        conf = Config(self.data_path + "fail_analyze.yml")
        self.assertEqual(conf.read(), 0)
        # TODO

    def test_success_action(self):
        conf = Config(self.data_path + "success_action.yml")
        self.assertEqual(conf.read(), 0)

    def test_fail_action(self):
        conf = Config(self.data_path + "fail_action.yml")
        self.assertEqual(conf.read(), 0)

#    def test_sample(self):
#        yaml.load("""
#        fruit:
#            - apple
#            - banana
#        """)
#        yaml.dump()
