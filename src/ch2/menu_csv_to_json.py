import json, csv
infile = 'excel-menu-norm.csv'
outfile = 'excel-menu-norm.json'
# CSVファイルを読み込む --- (※1)
items = []
with open(infile, 'r', encoding='utf-8') as fp:
    reader = csv.reader(fp)
    # CSVを毎行読む --- (※2)
    for i, row in enumerate(reader):
        if i == 0: continue # ヘッダ行は飛ばす --- (※3)
        # 変数を振り分ける --- (※4)
        name, price, mtype = row
        # 辞書型でメニューを追加 --- (※5)
        items.append({
            'name': name, 
            'price': int(price), 
            'mtype': mtype
        })
# JSONにシリアライズ ---- (※6)
json_s = json.dumps(items, indent=4, ensure_ascii=False)
print(json_s)
# ファイルに保存 --- (※7)
with open(outfile, 'w', encoding='utf-8') as fp:
    fp.write(json_s)
