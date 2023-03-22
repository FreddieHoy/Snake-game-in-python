import unittest
import convert


class TestConvert(unittest.TestCase):
    def test_convert(self):
        res1 = convert.doConvert(21)
        self.assertEqual(res1, [0, 0, 0, 1, 0, 1, 0, 1])

        res2 = convert.doConvert(5)
        self.assertEqual(res2, [0, 0, 0, 0, 0, 1, 0, 1])

        res3 = convert.doConvert(0)
        self.assertEqual(res3, [0, 0, 0, 0, 0, 0, 0, 0])
