import json


# 读取JSON文件
def parse_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
