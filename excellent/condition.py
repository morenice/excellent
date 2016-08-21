# -*- coding: utf-8 -*-
from abc import abstractmethod
from enum import Enum


class CondtionGroup():
    condition_list = []

    def __init__(self, conf):
        self.parse_conf(conf)

    def parse_conf(self):
        pass

    def _create_condition(self):
        pass

    def analyze(self):
        for condition in self.condition_list:
            condition.analyze()


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

    @abstractmethod
    def analyze(self):
        pass


class DateCondition(Condtion):
    condition = None
    value = 0

    def __init__(self, column_name, row_startline):
        self.column_type = ColumnType.date
        super().__init__(column_name, row_startline)

    def analyze(self):
        pass


# TODO
class IntCondition(Condtion):
    pass


# TODO
class StringCondition(Condtion):
    pass
