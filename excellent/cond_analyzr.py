from excel_analyzer import ExcelAnalyzer


class ConditionAnalyzer(ExcelAnalyzer):
    column_type = ""
    column_value = ""
    row_startline = 0


class IntCondition(ConditionAnalyzer):
    condition = ["==", "!=", "<=", "<", ">", ">="]
    value = -1

    def __init__(col_name, col_value, row_start):
        pass


class DateCondition(ConditionAnalyzer):
    pass


class StringCondition(ConditionAnalyzer):
    pass
