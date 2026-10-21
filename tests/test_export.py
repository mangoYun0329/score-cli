import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from score_manager import ScoreBook


class TestExport(unittest.TestCase):
    def test_export_csv(self):
        book = ScoreBook()
        book.add("张三", 92)
        book.add("李四", 78)
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "scores.csv")
            self.assertEqual(book.export_csv(path), 2)
            with open(path, encoding="utf-8-sig") as f:
                lines = f.read().strip().splitlines()
        self.assertEqual(lines[0], "姓名,分数")
        self.assertEqual(len(lines), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
