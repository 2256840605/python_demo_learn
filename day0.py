# 定义一个读取job类别以及计数的函数
# 原始数据
jobs = [
    {"title": "Agent开发实习", "category": "Agent"},
    {"title": "RAG开发实习", "category": "RAG"},
    {"title": "LLM应用实习", "category": "Agent"},
]

def job_count(jobs):
    result={}
    for job in jobs:
        cat = job['category']
        if cat in result:
            result[cat] = result[cat]+1
        else:
            result[cat] = 1
    return result

print(job_count(jobs))
