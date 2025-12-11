import json

with open('report_demo.html', 'r', encoding='utf-8') as report_reader:
    content = report_reader.read()

data = {
    "data": content
}

# 方法一：使用 json.dump() 直接写入文件（推荐）
with open('report.json', 'w', encoding='utf-8') as report_writer:
    json.dump(data, report_writer, ensure_ascii=False, indent=4)