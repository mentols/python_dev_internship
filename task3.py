import json
from pprint import pprint

os_dict = {}

with open('task3/os_versions.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


for phone in data:
    for k, v in phone.items():
        for i in range(len(v)-1):
            if v[i][0:6] == 'Версия':
                if v[i + 1] in os_dict.keys():
                    os_dict[v[i + 1]] += 1
                else:
                    os_dict[v[i + 1]] = 1

d = dict(sorted(os_dict.items(), key=lambda item: item[1], reverse=True))
[print(k, '-', v) for k, v in d.items()]
