"""学生成绩管理：录入、平均分、及格率。

实验项目：Git 协作实战的示例工程，代码本身保持简单，
重点在于演示版本创建、分支管理、合并与远程协作的完整流程。
"""


class ScoreBook:
    """一个班的学生成绩册。"""

    def __init__(self):
        self._students = []

    @property
    def count(self):
        return len(self._students)

    def add(self, name, score):
        """录入一条成绩，分数必须在 0~100 之间。"""
        if not 0 <= score <= 100:
            raise ValueError("成绩必须在 0~100 之间")
        self._students.append({"name": name, "score": score})

    def average(self):
        """全班平均分。"""
        if not self._students:
            raise ValueError("还没有录入任何成绩")
        return sum(s["score"] for s in self._students) / len(self._students)

    def pass_rate(self):
        """及格率，60 分及格。"""
        if not self._students:
            raise ValueError("还没有录入任何成绩")
        passed = sum(1 for s in self._students if s["score"] >= 60)
        return passed / len(self._students)

    def rank(self):
        """按分数从高到低排名，返回 [(名次, 姓名, 分数), ...]。"""
        ordered = sorted(self._students, key=lambda s: s["score"], reverse=True)
        return [(i, s["name"], s["score"]) for i, s in enumerate(ordered, 1)]


if __name__ == "__main__":
    book = ScoreBook()
    for name, score in [("张三", 92), ("李四", 78), ("王五", 55)]:
        book.add(name, score)
    print("人数:", book.count)
    print("平均分: %.1f" % book.average())
    print("及格率: %.0f%%" % (book.pass_rate() * 100))
