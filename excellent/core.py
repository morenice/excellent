# -*- coding: utf-8 -*-
import sys
import getopt
import excellent
import excellent.config
import excellent.analyzer
import excellent.action_manager


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

    def process(self):
        print(" - process analyze ...")
        if self.analyzer.analyze():
            if self.analyzer.count_analyze_data() == 0:
                print("Complete")
                print("no action data. please confirm analyzed data...")
                return

            print(" - do action ...")
            self.action_manager.do_action(self.analyzer.get_analyze_data())
            print("Complete")


class ExcellentOpts:
    def parse_args(self, args):
        try:
            opts, args = getopt.getopt(args, "c:f:V")
        except:
            # show usage and return!!
            self.usage()
            return (None, None)

        conf_file = xls_file = ""
        for opt, arg in opts:
            if opt == "-V":
                # show version and return!!
                self.show_version()
                return (None, None)
            elif opt == "-c":
                conf_file = arg
            elif opt == "-f":
                xls_file = arg

        # need conf filename and excel filename
        if len(conf_file) == 0 or len(xls_file) == 0:
            # show usage and return!!
            self.usage()
            return (None, None)

        return (conf_file, xls_file)

    def usage(self):
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

    def show_version(self):
        print(excellent.__version__)


def main():
    ex_opts = ExcellentOpts()
    if len(sys.argv) <= 1:
        return ex_opts.usage()

    conf_file, xls_file = ex_opts.parse_args(sys.argv[1:])

    # show usage or version info. program exit.
    if conf_file is None and xls_file is None:
        return 0

    print(" - '%s' config file" % (conf_file))
    print(" - '%s' excel file " % (xls_file))

    print(" - read config file ...")
    config = excellent.config.Config(conf_file)
    if config.read() != 0:
        return 255

    print(" - prepare analyze and action ...")
    analyzer = excellent.analyzer.Analyzer(config.get_analyzer_conf())
    action_manager = excellent.action_manager.ActionManager(config.get_action_conf())

    print(" - validation excel file ... ")
    ex = Excellent(analyzer, action_manager)
    if ex.set_excel_file(xls_file) == False:
        return 255

    ex.process()
    return 0
