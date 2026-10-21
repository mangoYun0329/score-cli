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
        """按分数从高到低排名；同分并列，下一名次顺延（如 1、1、3）。"""
        ordered = sorted(self._students, key=lambda s: s["score"], reverse=True)
        ranked = []
        for i, s in enumerate(ordered):
            tied = i > 0 and s["score"] == ordered[i - 1]["score"]
            place = ranked[-1][0] if tied else i + 1
            ranked.append((place, s["name"], s["score"]))
        return ranked

    def export_csv(self, path):
        """把全部成绩导出为 CSV 文件，返回导出的记录条数。"""
        with open(path, "w", encoding="utf-8-sig", newline="") as f:
            f.write("姓名,分数\n")
            for s in self._students:
                f.write("%s,%s\n" % (s["name"], s["score"]))
        return self.count


if __name__ == "__main__":
    book = ScoreBook()
    for name, score in [("张三", 92), ("李四", 78), ("王五", 55)]:
        book.add(name, score)
    print("人数:", book.count)
    print("平均分: %.1f" % book.average())
    print("及格率: %.0f%%" % (book.pass_rate() * 100))
