import matplotlib.pyplot as plt
import japanmap
import json, re

INFILE1 = 'lifespan-ref-1-1.tsv'
INFILE2 = 'lifespan-ref-1-2.tsv'

# TSVファイルを読み込み交通事故の項目を得る --- (※1)
def get_accident(fname):
    ao = {}
    with open(fname, 'r', encoding='utf-8') as f:
        tsv = f.read()
    for line in tsv.split('\n'):
        line = line.strip()
        if line == '': continue
        cells = line.split('\t')
        pref = cells[0] # 都道府県名
        # acci = float(cells[13]) # 交通事故の確率 --- (※1a)
        acci = float(cells[5]) # 脳血管疾患の確率
        ao[pref] = acci
    return ao

data = {}
man = get_accident(INFILE1)
woman = get_accident(INFILE2)
# 男女の平均を得る --- (※2)
for pref in man.keys():
    data[pref] = (man[pref] + woman[pref]) / 2

# 都道府県別データを色データに変換 --- (※3)
max_val = max([v for k,v in data.items()])
min_val = min([v for k,v in data.items()])
cmap = plt.get_cmap('coolwarm')
norm = plt.Normalize(vmin=min_val, vmax=max_val)
coldata = {}
for pname, age in data.items():
    coldata[pname] = '#' + bytes(cmap(norm(age), bytes=True)[:3]).hex()
    print(pname, age, coldata[pname])

# 日本地図に色を塗る --- (※4)
fig, ax = plt.subplots(1, 1)
ax.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False) 
plt.colorbar(plt.cm.ScalarMappable(norm, cmap))
plt.imshow(japanmap.picture(coldata))
plt.show()
