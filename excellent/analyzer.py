# -*- coding: utf-8 -*-
import excellent.condition
from excellent.config_define import *
from openpyxl import Workbook


class Analyzer:
    condition_group_list = []
    analyze_data = []
    excel_workbook = None

    def __init__(self, analyze_conf):
        if analyze_conf is not None:
            self._parse_conf(analyze_conf)

    def _parse_conf(self, conf):
        group_list = conf[CONDITION_GROUP]
        for group_name in group_list:
            group = self._create_group(conf[group_name])
            if group is None:
                continue

            self.condition_group_list.append(group)

    def _create_group(self, group_conf):
        return excellent.condition.ConditionGroup(group_conf)

    def set_excel_file(self, xls_filename):
        workbook = None

        try:
            workbook = openpyxl.load_workbook(filename = xls_filename)
        except Exception as e:
            print(e)

        if workbook is None:
            return False

        self.excel_workbook = workbook
        return True

    def set_excel_workbook(self, workbook):
        self.excel_workbook = workbook
        return True

    def analyze(self):
        if self.excel_workbook is None:
            return False

        active_ws = self.excel_workbook.wbactive

        # 'OR' logic per group
        for group in self.condition_group_list:
            if group.match() == True:
                return True
        return False

    def get_analyze_data(self):
        return self.analyze_data

    def add_condition_group(self, group):
        self.condition_group_list.append(group)

    def remove_condition_group(self, group):
        self.condition_group_list.remove(group)

    def count(self):
        return len(self.condition_group_list)
