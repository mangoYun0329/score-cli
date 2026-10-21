import unittest
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from score_manager import ScoreBook


class TestRank(unittest.TestCase):
    def test_rank_order(self):
        book = ScoreBook()
        book.add("张三", 92)
        book.add("李四", 78)
        book.add("王五", 85)
        self.assertEqual(
            book.rank(),
            [(1, "张三", 92), (2, "王五", 85), (3, "李四", 78)],
        )

    def test_rank_empty(self):
        self.assertEqual(ScoreBook().rank(), [])

    def test_rank_tie(self):
        book = ScoreBook()
        book.add("张三", 90)
        book.add("李四", 90)
        book.add("王五", 80)
        self.assertEqual(
            book.rank(),
            [(1, "张三", 90), (1, "李四", 90), (3, "王五", 80)],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
