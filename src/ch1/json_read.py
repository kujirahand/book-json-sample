import json
# ファイルを読む
with open('test.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)
# 読み出したデータを表示
print(data[0]['name'], data[0]['age'])
print(data[1]['name'], data[1]['age'])
