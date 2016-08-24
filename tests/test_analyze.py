import unittest
from excellent.analyzer import *
from excellent.condition import *
from excellent.config import *
from openpyxl import Workbook


class AnalyzerTestCase(unittest.TestCase):
    analyzer = None

    def setUp(self):
        config_string = """
config_version: 0.1
analyzer:
    condition_group: [group_a, group_b]
    group_a:
        condition_name: [test]
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: before_today
            value: 5
    group_b:
        condition_name: [test]
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: before_today
            value: 3
"""
        config = Config(None)
        config.read_raw_data(config_string)
        self.analyzer = Analyzer(config.get_analyzer_conf())

    def test_analyze_group_count(self):
        self.assertEqual(self.analyzer.count(), 2)

    def test_success_match(self):
        wb = Workbook()
        ws = wb.create_sheet()
        ws['A1'] = 'due-date'
        ws['A2'] = '2016-05-10'
        ws['A3'] = '2016-04-10'
        ws['A4'] = '2017-02-13'
        self.analyzer.set_excel_workbook(wb)
        self.assertEqual(self.analyzer.analyze(), True)

    def test_fail_match(self):
        wb = Workbook()
        ws = wb.create_sheet()
        ws['A1'] = 'due-date'
        ws['A2'] = 'hello'
        ws['A3'] = 'bye'
        self.assertEqual(self.analyzer.analyze(), False)
