import sys
import getopt
from excel_analyzer import ExcelAnalyzer
from action_handler import ActionHandler


class Excellent:
    ExcelAnalyzer = None
    ActionHandler = None

    def __init__(self):
        pass

    def parse_getopt(*args):
        #getopt.getopt(sys.argv[1:], "abchi:o:", ["input=","output=","help"])
        getopt.getopt(args, "abchi:o:", ["input=","output=","help"])
        pass

    def read_configure(filename):
        pass


if __name__ == "__main__":
    print("Excellent")
