# -*- coding: utf-8 -*-
import sys
import getopt
import openpyxl

import excellent
import excellent.config
import excellent.analyzer
import excellent.action


class Excellent(object):
    """ """
    analyzer = None
    action = None
    filename = None
    filedata = None

    def __init__(self, analyzer, action):
        self.analyzer = analyzer
        self.action = action

    def set_file(self, filename):
        # set filename and filedata
        self.filename = filename
        self.filedata = None

    def analyze(self):
        pass

    def do_action(self):
        pass


def parse_args(args):
    try:
        opts, args = getopt.getopt(args, "c:f:V")
    except:
        # show usage and program exit!
        usage()
        sys.exit(0)

    conf_file = xls_file = ""
    for opt, arg in opts:
        if opt == "-V":
            # show version and program exit!
            print(excellent.__version__)
            sys.exit(0)
        elif opt == "-c":
            conf_file = arg
        elif opt == "-f":
            xls_file = arg

    # need conf filename and excel filename
    if len(conf_file) == 0 or len(xls_file) == 0:
        # show usage and program exit!
        usage()
        sys.exit(0)

    return (conf_file, xls_file)


def usage():
    print("""
Usage: %s -c [file] -f [file]

 -c\tyaml style configure file.
 -f\txls or xlsx file.
 -V\tshow version.

Example:
 %s -c configure.yml -f target.xlsx
 %s -V
""" % (sys.argv[0], sys.argv[0], sys.argv[0])
          )


def validate_xls_file(xls_file):
    try:
        openpyxl.load_workbook(filename = xls_file)
    except Exception as e:
        print(e)
        return False
    return True


def main():
    # TODO : need return type!!
    if len(sys.argv) <= 1:
        return usage()

    conf_file, xls_file = parse_args(sys.argv[1:])
    if validate_xls_file(xls_file) == False:
        return -1

    config = excellent.Config(conf_file)
    if config.read() != 0:
        return -2
