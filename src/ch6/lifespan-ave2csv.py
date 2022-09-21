import json

INFILE = 'lifespan-ave.json'
OUTFILE = 'liefespan-ave.csv'
# ファイルを読む
data = json.load(open(INFILE, 'r', encoding='utf-8'))
# 出力用のファイルを開く(SJISで保存)
with open(OUTFILE, 'w', encoding='SJIS') as fp:
    for pref, v in data.items():
        fp.write('{},{}\r\n'.format(pref, v))

