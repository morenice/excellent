import unittest
import exceltp.core


class TestExcellentOpts(exceltp.core.ExcellentOpts):
    def usage(self):
        pass

    def show_version(self):
        pass


class ExcellentOptsTest(unittest.TestCase):
    def test_success_opts(self):
        opts = TestExcellentOpts()
        input_args = ["-c", "option.yml", "-f", "excel.xls"]
        output1, output2 = opts.parse_args(input_args)
        self.assertEqual(output1, "option.yml")
        self.assertEqual(output2, "excel.xls")

    def test_wrong_opts_1(self):
        opts = TestExcellentOpts()
        input_args = ["-c", "-f", "excel.xls"]
        output1, output2 = opts.parse_args(input_args)
        self.assertEqual(output1, None)
        self.assertEqual(output2, None)

    def test_wrong_opts_2(self):
        opts = TestExcellentOpts()
        input_args = ["www", "naver", "com"]
        output1, output2 = opts.parse_args(input_args)
        self.assertEqual(output1, None)
        self.assertEqual(output2, None)
