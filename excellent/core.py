import sys
import getopt
from excel_analyzer import ExcelAnalyzer
from action_handler import ActionHandler


class Excellent(object):
    """ """
    analyzer = None
    action = None
    filename = None
    filedata = None

    def __init__(self, ana, act):
        self.analyzer = ana
        self.action = act

    def set_excelfile(self, filename):
        # set filename and filedata
        self.filename = filename
        self.filedata = None

    def analyze():
        pass

    def do_action():
        pass

    def _is_readable_excelfile(filename):
        pass


def parse_getopt(*args):
    #getopt.getopt(sys.argv[1:], "abchi:o:", ["input=","output=","help"])
    # configure, excel file,
    getopt.getopt(args, "abchi:o:", ["input=","output=","help"])
    pass

def print_help():
    pass

def read_excelfile(filename):
    pass

if __name__ == "__main__":
    print("Excellent")
