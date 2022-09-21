import json
lines = []
# y方向、x方向の二重ループを利用して座標を生成する --- (※1)
for y in range(10):
    if y % 3 == 2: continue
    for x in range(10):
        if x % 3 == 2: continue
        # 起点を計算 --- (※2)
        x1 = x * 50 + 30
        y1 = y * 50 + 30
        x2 = x1 + 50
        y2 = y1 + 50
        # 三角形を描画する --- (※3)
        lines.append([x1, y1, x2, y2])
        lines.append([x2, y2, x1, y2])
        lines.append([x1, y2, x1, y1])
# ファイルへJSONを保存 --- (※4)
with open('drawtool.json', 'w') as fp:
    json.dump(lines, fp)
