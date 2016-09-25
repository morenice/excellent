import unittest
import datetime
import yaml
from exceltp.condition import *
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
            condition: today_equal
            value: -1
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
    def setUp(self):
        self.wb = Workbook()
        ws1 = self.wb.active
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

    def tearDown(self):
        del(self.wb)

    def test_match_type(self):
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 3
            condition: today_equal
            value: 3
"""
        date = datetime.datetime(2016, 5, 31)
        cond = create_condition(config_string, 'test', date)

        ws1 = self.wb.active
        self.assertEqual(cond.match(ws1['A1']), MatchResult.invalid_row)
        self.assertEqual(cond.match(ws1['A2']), MatchResult.invalid_row)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A20']), MatchResult.invalid_value)
        self.assertEqual(cond.match(ws1['B1']), MatchResult.invalid_column)
        self.assertEqual(cond.match(ws1['C1']), MatchResult.invalid_column)

    def test_today_equal_1(self):
        """ condition: today_equal
        ex) value : 3, cell == today + 3
        """
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: today_equal
            value: 3
"""
        date = datetime.datetime(2016, 5, 11)
        cond = create_condition(config_string, 'test', date)

        ws1 = self.wb.active
        self.assertEqual(cond.match(ws1['A2']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.match)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A5']), MatchResult.no_match)

    def test_today_equal_2(self):
        """ condition: today_equal
        ex) value : -3, cell == today -3
        """
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: today_equal
            value: -3
"""
        date = datetime.datetime(2018, 8, 20)
        cond = create_condition(config_string, 'test', date)

        ws1 = self.wb.active
        self.assertEqual(cond.match(ws1['A2']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A5']), MatchResult.match)

    def test_today_equal_3(self):
        """ condition: today_equal
        ex) value : 0, cell == today
        """
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: today_equal
            value: 0
"""
        date = datetime.datetime(2016, 5, 8)
        cond = create_condition(config_string, 'test', date)

        ws1 = self.wb.active
        self.assertEqual(cond.match(ws1['A2']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.match)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A5']), MatchResult.no_match)

    def test_today_range_in_1(self):
        """condition: today_range_in
        ex) value : 3, cell <= today + 3
        """
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: today_range_in
            value: 3
"""
        date = datetime.datetime(2016, 5, 10)
        cond = create_condition(config_string, 'test', date)

        ws1 = self.wb.active
        self.assertEqual(cond.match(ws1['A2']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.match)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A5']), MatchResult.no_match)

    def test_today_range_in_2(self):
        """ condition: today_range_in
        ex) value : -3, cell >= today -3
        """
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: today_range_in
            value: -3
"""
        date = datetime.datetime(2018, 8, 22)
        cond = create_condition(config_string, 'test', date)

        ws1 = self.wb.active
        self.assertEqual(cond.match(ws1['A2']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A5']), MatchResult.match)

    def test_today_range_in_3(self):
        """ condition: today_range_in
        ex) value : 0, cell == today
        """
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: today_range_in
            value: 0
"""
        date = datetime.datetime(2016, 5, 8)
        cond = create_condition(config_string, 'test', date)

        ws1 = self.wb.active
        self.assertEqual(cond.match(ws1['A2']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.match)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A5']), MatchResult.no_match)

    def test_today_range_over_1(self):
        """condition: today_range_over
        ex) value : 3, cell > today + 3
        """
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: today_range_over
            value: 3
"""
        date = datetime.datetime(2019, 5, 10)
        cond = create_condition(config_string, 'test', date)

        ws1 = self.wb.active
        self.assertEqual(cond.match(ws1['A2']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.match)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.match)
        self.assertEqual(cond.match(ws1['A5']), MatchResult.match)

    def test_today_range_over_2(self):
        """ condition: today_range_over
        ex) value : -3, cell < today -3
        """
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: today_range_over
            value: -3
"""
        date = datetime.datetime(2017, 6, 10)
        cond = create_condition(config_string, 'test', date)

        ws1 = self.wb.active
        self.assertEqual(cond.match(ws1['A2']), MatchResult.match)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.match)
        self.assertEqual(cond.match(ws1['A5']), MatchResult.match)

    def test_today_range_over_3(self):
        """ condition: today_range_over
        ex) value : 0, cell == today
        """
        config_string = """
        test:
            column_name: a
            column_type: date
            row_startline: 2
            condition: today_range_over
            value: 0
"""
        date = datetime.datetime(2016, 5, 8)
        cond = create_condition(config_string, 'test', date)

        # today_range_over
        # when value is 0, always no match
        ws1 = self.wb.active
        self.assertEqual(cond.match(ws1['A2']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A3']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A4']), MatchResult.no_match)
        self.assertEqual(cond.match(ws1['A5']), MatchResult.no_match)
