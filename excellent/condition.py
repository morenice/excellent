# -*- coding: utf-8 -*-
from abc import abstractmethod
from enum import Enum
from excellent.config_define import *


class ConditionGroup():
    group_name = ""
    condition_list = []

    def __init__(self, group_conf):
        self._parse_conf(group_conf)

    def _parse_conf(self, conf):
        for cond_name in conf[CONDITION_NAME]:
            cond = self._create_condition(conf[cond_name])
            if cond is not None:
                self.condition_list.append(cond)

    def _create_condition(self, cond_conf):
        if cond_conf[COLUMN_TYPE] == ColumnType.date.name:
            cond = DateCondition(cond_conf)
        elif cond_conf[COLUMN_TYPE] == ColumnType.integer.name:
            cond = IntCondition(cond_conf)
        elif cond_conf[COLUMN_TYPE] == ColumnType.string.name:
            cond = StringCondition(cond_conf)

        return cond

    def count(self):
        return len(self.condition_list)

    def match(self, row_data):
        match_result = True
        for condition in self.condition_list:
            # 'AND" logic per condition
            match_result &= condition.match()
        return match_result


class ColumnType(Enum):
   date = 0
   integer = 1
   string = 2


class Condtion(object):
    column_name = ""
    column_type = None
    row_startline = 0
    condition = None
    value = None

    def __init__(self, cond_conf):
        self.column_name = cond_conf[COLUMN_NAME]
        self.row_startline = cond_conf[ROW_STARTLINE]
        self.condition = cond_conf[CONDITION]
        self.value = cond_conf[CONDITION_VALUE]

    def get_column_name(self):
        return self.column_name

    def get_column_type(self):
        return self.column_type

    @abstractmethod
    def match(self, data):
        pass


class DateCondition(Condtion):

    def __init__(self, cond_conf):
        self.column_type = ColumnType.date
        super().__init__(cond_conf)

    def match(self, data):
        pass


# TODO
class IntCondition(Condtion):

    def __init__(self, column_name, row_startline):
        self.column_type = ColumnType.integer
        super().__init__(column_name, row_startline)

    def match(self, data):
        pass


# TODO
class StringCondition(Condtion):

    def __init__(self, column_name, row_startline):
        self.column_type = ColumnType.string
        super().__init__(column_name, row_startline)

    def match_data(self, data):
        pass
