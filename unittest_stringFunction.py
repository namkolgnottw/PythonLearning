from interview_hw import to_string
import unittest

class to_string_testcase(unittest.TestCase):

    def test_integer1(self):
        a = 9527
        ans = '9,527'
        self.assertEqual(to_string(a), ans)

    def test_integer2(self):
        a = 3345678
        ans = '3,345,678'
        self.assertEqual(to_string(a), ans)

    def test_negative_integer(self):
        a = -9527
        ans = '-9,527'
        self.assertEqual(to_string(a), ans)
      

    def test_float1(self):
        a = 1223.4444
        ans = '1,223.4444'
        self.assertEqual(to_string(a), ans)

    def test_negative_float(self):
        a = -1234.45
        ans = '-1,234.45'
        self.assertEqual(to_string(a), ans)




