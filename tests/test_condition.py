import unittest
from excellent.condition import *
from excellent.config import *
from openpyxl import Workbook


class TestConditionGroup(ConditionGroup):
    def get_condition_list(self):
        return condition_list


class ConditionGroupTestCase(unittest.TestCase):
    data_path = "tests/config/"
    group = None

    def setUp(self):
        config = Config(self.data_path + "success_analyze.yml")
        config.read()
        self.group = TestConditionGroup(config.get_analyzer_conf())

    def test_analyze_config(self):
        self.assertEqual(self.group.count(), 2)

        cond_list = self.group.get_condition_list()
        first = cond_list[0]
        self.assertEqual(first.get_column_name(), "a")

        second = cond_list[1]
        self.assertEqual(second.get_column_name(), "a")

    def test_success_match(self):
        wb = Workbook()
        ws1 = wb.create_sheet()
        ws['A3'] = '2016-04-10'
        self.assertEqual(self.group.match(), True)

    def test_fail_match(self):
        wb = Workbook()
        ws1 = wb.create_sheet()
        ws['A3'] = '2016-04-10'
        self.assertEqual(self.group.match(), False)
