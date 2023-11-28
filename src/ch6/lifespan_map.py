import matplotlib.pyplot as plt
import japanmap
import json, re

INFILE = 'lifespan-ave.json'

# JSONデータを読み込む --- (※1)
data = json.load(open(INFILE, 'r', encoding='utf-8'))

# 最大値と最小値を求める --- (※2)
max_val = max([v for k,v in data.items()])
min_val = min([v for k,v in data.items()])
# 都道府県の平均寿命を色データに変換 --- (※3)
cmap = plt.get_cmap('coolwarm')
norm = plt.Normalize(vmin=min_val, vmax=max_val)
print(norm)
# 各都道府県の値を処理 --- (※4)
coldata = {}
for pname, age in data.items():
    coldata[pname] = '#' + bytes(cmap(norm(age), bytes=True)[:3]).hex()
    print(pname, age, coldata[pname])

# 日本地図に色を塗る --- (※5)
# plt.colorbar(mappable=plt.cm.ScalarMappable(norm=norm, cmap=cmap))
plt.imshow(japanmap.picture(coldata))
plt.show()
