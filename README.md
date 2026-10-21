# score-cli 学生成绩管理

一个用于演示 Git 协作开发流程的小型 Python 工程。

## 功能

- 录入学生成绩（0~100 分）
- 统计全班平均分
- 统计及格率（60 分及格）

## 使用方法

```bash
python src/score_manager.py
```

## 运行测试

```bash
python -m unittest discover -s tests -v
```

## 协作流程

本项目采用 GitHub Flow：

1. 每个需求或缺陷先在 Issue 中登记；
2. 从 `main` 拉出 `feature/*` 或 `fix/*` 分支开发；
3. 提交前本地跑通单元测试，推送后创建 Pull Request；
4. 至少一名同伴 Review 后合并到 `main`，并删除临时分支。

当前版本：v0.2
