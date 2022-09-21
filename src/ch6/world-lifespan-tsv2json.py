from itertools import count
import json, re

INFILE = 'world-lifespan.tsv'
OUTFILE = 'world-lifespan.json'

# TSVファイルを読み込む --- (※1)
data = {}
text = open(INFILE, 'r', encoding='UTF-8').read()
for line in text.split('\n'):
    line = line.strip()
    cells = line.split('\t')
    if len(cells) <= 6: continue # 無効なデータを飛ばす --- (※2)
    country = cells[0]
    lifespan_s = cells[6]
    if lifespan_s == '' or lifespan_s == '-': continue
    # 国名にあるカッコを削って一般的な名称に直す --- (※3)
    country = re.sub('\(.+\)', '', country).strip()
    lifespan = float(lifespan_s)
    data[country] = lifespan

# JSON形式で保存 --- (※4)
with open(OUTFILE, 'w', encoding='utf-8') as fp:
    json.dump(data, fp, ensure_ascii=False, indent=2)

# 余命が長い順に並び替えて上位10件を出力 --- (※5)
life_list = sorted([[k, v] for k,v in data.items()],
                   key=lambda v: v[1], reverse=True)
for rank, row in enumerate(life_list[0:10]):
    print('{:2d}位 {} ({}才)'.format(rank+1, row[0], row[1]))




