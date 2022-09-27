import json
from PIL import Image

# JSONデータを読み込む
infile = 'images/train-numimage.json'
with open(infile, 'r', encoding='utf-8') as fp:
    data = json.load(fp)

def export_csv(no):
    # 画像データを取り出す
    images = data['images'][no]
    csv = ''
    for y in range(28):
        cells = images[y*28:y*28+28]
        print(cells)
        csv += ','.join(map(lambda v:str(v), cells)) + '\n'
    # ファイルに保存
    open('images/{}.csv'.format(no), 'w').write(csv)
    # ラベル番号を表示
    print('label=', data['labels'][no])

# 適当に10枚取り出して出力
for no in range(10):
    export_csv(no)

