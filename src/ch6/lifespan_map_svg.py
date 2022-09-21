import matplotlib.pyplot as plt
from japanmap import picture, pref_map, pref_names
import json, re

INFILE = 'lifespan-ave.json'
OUTFILE = 'lifespan-ave.svg'

# JSONデータを読み込む --- (※1)
data = json.load(open(INFILE, 'r', encoding='utf-8'))

# 都道府県の平均寿命を色データに変換 --- (※2)
max_val = max([v for k,v in data.items()])
min_val = min([v for k,v in data.items()])
cmap = plt.get_cmap('coolwarm')
norm = plt.Normalize(vmin=min_val, vmax=max_val)
coldata = {}
for pname, age in data.items():
    coldata[pname] = '#' + bytes(cmap(norm(age), bytes=True)[:3]).hex()
    print(pname, age, coldata[pname])

# 都道府県番号順にデータを並べる --- (※3)
values = []
for i in range(1, 48):
    key = re.sub('[都府県]$', '', pref_names[i])
    values.append(coldata[key])

# SVGで出力する --- (※4)
svg = pref_map(range(1,48), cols=values, tostr=True)
# SVGのサイズと枠線を修正
svg = svg.replace('<svg ', '<svg  width="2048" height="2048" ')
svg = svg.replace('<path ', '<path style="stroke: gray; stroke-width: 0.001" ')
with open(OUTFILE, 'w', encoding='utf-8') as fp:
    fp.write(svg)
