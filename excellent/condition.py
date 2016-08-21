# -*- coding: utf-8 -*-
from abc import abstractmethod
from enum import Enum


class ConditionGroup():
    condition_list = []

    def __init__(self, conf):
        self._parse_conf(conf)

    def _parse_conf(self, data):
        pass

    def _create_condition(self):
        pass

    def match(self):
        match_result = True
        for condition in self.condition_list:
            # and logic in group
            match_result &= condition.match()
        return match_result

    def count(self):
        return len(self.condition_list)


class ColumnType(Enum):
   date = 0
   integer = 1
   string = 2


class Condtion(object):
    column_name = ""
    column_type = None
    row_startline = 0

    def __init__(self, column_name, row_startline):
        self.column_name = column_name
        self.row_startline = row_startline

    def get_column_name(self):
        return self.column_name

    def get_column_type(self):
        return self.column_type

    @abstractmethod
    def match(self, data):
        pass


class DateCondition(Condtion):
    condition = None
    value = 0

    def __init__(self, column_name, row_startline):
        self.column_type = ColumnType.date
        super().__init__(column_name, row_startline)

    def match(self, data):
        pass


# TODO
class IntCondition(Condtion):
    condition = None
    value = 0

    def __init__(self, column_name, row_startline):
        self.column_type = ColumnType.integer
        super().__init__(column_name, row_startline)

    def match(self, data):
        pass

# TODO
class StringCondition(Condtion):
    condition = None
    value = 0

    def __init__(self, column_name, row_startline):
        self.column_type = ColumnType.string
        super().__init__(column_name, row_startline)

    def match_data(self, data):
        pass
