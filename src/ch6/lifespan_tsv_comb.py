import json

INFILE = 'lifespan.tsv'
OUTFILE = 'lifespan-ave.json'

# 男女別の値を得る --- (※1)
man, woman = {}, {} # 辞書型変数を初期化
# TSVファイルを開いて読む --- (※2)
text = open(INFILE, 'r', encoding='utf-8').read()
for line in text.split('\n'):
    # タブで値を区切って変数に代入 --- (※3)
    key_m,val_m,key_w,val_w = line.split('\t')
    # 辞書型データのキーに代入 --- (※4)
    man[key_m] = float(val_m)
    woman[key_w] = float(val_w)

# 男女平均を求める --- (※5)
ave = {}
for key in man.keys():
    ave[key] = (man[key] + woman[key]) / 2
    print(key, ave[key])

# 結果をJSONで保存する --- (※6)
with open(OUTFILE, 'w', encoding='utf-8') as fp:
    json.dump(ave, fp, ensure_ascii=False, indent=2)

