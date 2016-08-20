from excel_analyzer import ExcelAnalyzer


class ConditionAnalyzer(ExcelAnalyzer):
    column_type = ""
    column_value = ""
    row_startline = 0


class DateCondition(ConditionAnalyzer):
    """ TODO!! first"""
    pass


class IntCondition(ConditionAnalyzer):
    pass


class StringCondition(ConditionAnalyzer):
    pass
