import unittest
import datetime
import yaml
from excellent.condition import *
from openpyxl import Workbook


def create_condition(config_string, cond_name, criteria_date):
    condition_conf = yaml.load(config_string)
    cond = DateCondition(cond_name, condition_conf[cond_name])
    cond.set_criteria_date(criteria_date)
    return cond


class ConditionGroupTestCase(unittest.TestCase):

    def test_group_function(self):
        group = ConditionGroup("group1", None)

        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: days_ago
            value: 1
"""
        date = datetime.datetime(2016, 5, 14)
        cond = create_condition(config_string, 'test', date)

        group.add_condition(cond)

        wb = Workbook()
        ws1 = wb.active
        ws1.title = "worksheet1"
        ws1['A1'] = 'Due date'
        ws1['A2'] = datetime.datetime(2010, 7, 21)
        ws1['A3'] = datetime.datetime(2016, 5, 15)
        ws1['A4'] = datetime.datetime(2017, 6, 21)
        ws1['B1'] = 'Name'
        ws1['B2'] = 'Tony'
        ws1['B3'] = 'Mike'
        ws1['B4'] = 'Lee'

        self.assertEqual(group.match(ws1.rows[2]), True)
        self.assertEqual(group.match(ws1.rows[3]), False)

    def test_group_function_and_operation(self):
        # TODO: 'AND' logic testing with multiple condition
        # 1 group and 2 condition
        pass


class DateConditionTestCase(unittest.TestCase):

    def test_days_ago_function1(self):
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: days_ago
            value: 5
"""
        date = datetime.datetime(2016, 5, 16)
        cond = create_condition(config_string, 'test', date)

        wb = Workbook()
        ws1 = wb.active
        ws1.title = "worksheet1"
        ws1['A1'] = 'Due date'
        ws1['A2'] = datetime.datetime(2010, 7, 21)
        ws1['A3'] = datetime.datetime(2016, 5, 21)
        ws1['A4'] = datetime.datetime(2017, 6, 21)
        ws1['B1'] = 'Name'
        ws1['B2'] = 'Tony'
        ws1['B3'] = 'Mike'
        ws1['B4'] = 'Lee'

        self.assertEqual(cond.match(ws1['A1']), MatchResult.invalid_row)
        self.assertEqual(cond.match(ws1['A2']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.match)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['B1']), MatchResult.invalid_column)

    def test_days_ago_function2(self):
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 4
            condition: days_ago
            value: 2
"""
        date = datetime.datetime(2085, 3, 21)
        cond = create_condition(config_string, 'test', date)

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

        self.assertEqual(cond.match(ws1['A1']), MatchResult.invalid_row)
        self.assertEqual(cond.match(ws1['A2']), MatchResult.invalid_row)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.invalid_row)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A20']), MatchResult.invalid_value)
        self.assertEqual(cond.match(ws1['B1']), MatchResult.invalid_column)
        self.assertEqual(cond.match(ws1['C1']), MatchResult.invalid_column)
