import json
from pathlib import Path


def load_jobs(file_path):
    """读取 JSON 文件，返回岗位列表。"""
    with open(file_path, "r", encoding="utf-8") as file:
        jobs = json.load(file)

    return jobs


def count_categories(jobs):
    """统计各类别的岗位数量。"""
    counts = {}

    for job in jobs:
        category = job["category"]
        counts[category] = counts.get(category, 0) + 1

    return counts


def main():
    # 当前脚本位于 scripts 目录，上一级就是项目根目录
    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root / "data" / "jobs.json"

    jobs = load_jobs(data_path)
    counts = count_categories(jobs)

    print(f"岗位总数：{len(jobs)}")

    for category, count in counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()