import json

# キノコのCSVデータを読み出す --- (※1)
text = open('mushroom.csv', 'r').read()

# CSVを読んでラベルとデータに分割 --- (※2)
labels = []
data = []
for line in text.split('\n'):
    cells = line.split(',')
    if len(cells) != 23: continue
    labels.append(cells[0]) # 0列目が答えラベル
    data.append(cells[1:]) # 1列目以降がデータ

# データの各列をOne-hotに変換 --- (※3)
for col in range(len(data[0])):
    # 各列にいくつのデータがあるか確認する --- (※4)
    cnt = 0
    dic = {}
    for row in data:
        v = row[col]
        if v not in dic:
            dic[v] = cnt
            cnt += 1
    # One-hot形式に変換 --- (※5)
    for row in data:
        v = dic[row[col]]
        if cnt == 2: # 0と1で表現できる
            row[col] = [v]
        else:
            val = [0] * cnt
            val[v] = 1
            row[col] = val
print(data[0]) # --- (※6)

# 各列のOne-hotデータを結合して1次元にする --- (※7)
result = []
for row in data:
    line = []
    for cells in row:
        line.extend(cells)
    result.append(line)
print(len(result[0]), '>', result[0]) # --- (※8)
print(result[1])
print(result[2])
# データをファイルに保存 --- (※9)
with open('mushroom_onehot.json', 'w', encoding='utf-8') as fp:
    json.dump({'labels': labels, 'data': result}, fp, indent=2)

