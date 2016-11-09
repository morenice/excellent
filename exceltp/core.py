# -*- coding: utf-8 -*-
import sys
import getopt
import exceltp
import exceltp.config
import exceltp.analyzer
import exceltp.action_manager


class Excellent(object):
    def __init__(self, analyzer, action_manager):
        self.analyzer = analyzer
        self.action_manager = action_manager
        self.xls_filename = None

    def set_excel_file(self, xls_filename):
        if self.analyzer.set_excel_file(xls_filename):
            self.xls_filename = xls_filename
            return True
        return False

    def analyze(self):
        if self.analyzer.analyze():
            return self.analyzer.count_analyze_data()
        return -1

    def process(self):
        return self.action_manager.do_action(self.analyzer.get_analyze_data())


class ExcellentOpts:
    def __init__(self):
        self.conf_file = ""
        self.xls_file = ""
        self.show_template = False
        self.show_version = False

    def parse_args(self, args):
        try:
            opts, args = getopt.getopt(args, "c:f:V")
        except:
            return False

        for opt, arg in opts:
            if opt == "-V":
                self.show_version = True
                return True
            elif opt == "-c":
                self.conf_file = arg
            elif opt == "-f":
                self.xls_file = arg

        return True


def usage():
    print("""excellent is microsoft excel third party program.
compare and analyze the data in the excel file. notifies the user.

Available commands:

 -c yaml style configure file.
 -f xls or xlsx file.
 -V show version.

Usage:
\t%s -c [file] -f [file]
\t%s -V

Example:
 %s -c config.yml -f sample.xlsx
""" % (sys.argv[0], sys.argv[0], sys.argv[0])
          )


def show_version():
    print(exceltp.__version__)


def main():
    ex_opts = ExcellentOpts()
    if len(sys.argv) <= 1:
        usage()
        return 0

    if ex_opts.parse_args(sys.argv[1:]) is False:
        usage()
        return 255

    if ex_opts.show_version is True:
        show_version()
        return 0

    # need conf filename and excel filename
    if len(ex_opts.conf_file) == 0 or len(ex_opts.xls_file) == 0:
        print("Both settings -c and -f are required.")
        return 255

    print("* '%s' config file" % (ex_opts.conf_file))
    print("* '%s' excel file " % (ex_opts.xls_file))

    print("* read config file ...")
    config = exceltp.config.Config(ex_opts.conf_file)
    ret = config.read()
    if ret != 0:
        print("* complete: fail %d" % ret)
        return 255

    print("* prepare analyzer and action ...")
    analyzer = exceltp.analyzer.Analyzer(config.get_analyzer_conf())
    action_manager = \
        exceltp.action_manager.ActionManager(config.get_action_conf())

    print("* validation excel file ... ")
    exceltp_obj = Excellent(analyzer, action_manager)
    if exceltp_obj.set_excel_file(ex_opts.xls_file) is False:
        return 255

    print("* process analyze ...")
    analyze_count = exceltp_obj.analyze()
    if analyze_count < 0:
        print("* complete: failed to analyze.")
        return 255

    if analyze_count == 0:
        print("* complete: no action data.")
        return 0

    print("* do action ...")
    exceltp_obj.process()
    print("* complete")
    return 0
