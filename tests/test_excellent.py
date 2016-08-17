import excellent
import unittest

class TestExcellent(unittest.TestCases):
    def setUp():
        pass

    def tearDown():
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
