import unittest
import exceltp.core


class ExcellentOptsTest(unittest.TestCase):
    def test_success_opts(self):
        opts = exceltp.core.ExcellentOpts()
        input_args = ["-c", "option.yml", "-f", "excel.xls"]
        opts.parse_args(input_args)
        self.assertEqual(opts.conf_file, "option.yml")
        self.assertEqual(opts.xls_file, "excel.xls")

    def test_wrong_opts_1(self):
        opts = exceltp.core.ExcellentOpts()
        input_args = ["-c", "-f", "excel.xls"]
        opts.parse_args(input_args)
        self.assertEqual(opts.conf_file, "-f")
        self.assertEqual(opts.xls_file, "")

    def test_wrong_opts_2(self):
        opts = exceltp.core.ExcellentOpts()
        input_args = ["www", "naver", "com"]
        opts.parse_args(input_args)
        self.assertEqual(opts.conf_file, "")
        self.assertEqual(opts.xls_file, "")

    def test_version_option(self):
        opts = exceltp.core.ExcellentOpts()
        input_args = ["-V"]
        opts.parse_args(input_args)
        self.assertEqual(opts.show_version, True)
