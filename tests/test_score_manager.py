import unittest
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from score_manager import ScoreBook


class TestScoreBook(unittest.TestCase):
    def setUp(self):
        self.book = ScoreBook()

    def test_add_and_count(self):
        self.book.add("张三", 92)
        self.book.add("李四", 78)
        self.assertEqual(self.book.count, 2)

    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            self.book.add("张三", 120)
        with self.assertRaises(ValueError):
            self.book.add("张三", -1)

    def test_average(self):
        self.book.add("张三", 90)
        self.book.add("李四", 80)
        self.assertAlmostEqual(self.book.average(), 85.0)

    def test_empty_average(self):
        with self.assertRaises(ValueError):
            self.book.average()

    def test_pass_rate(self):
        self.book.add("张三", 90)
        self.book.add("李四", 59)
        self.assertAlmostEqual(self.book.pass_rate(), 0.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
