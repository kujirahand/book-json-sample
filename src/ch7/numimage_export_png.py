import json
from PIL import Image

# JSONデータを読み込む --- (※1)
infile = 'images/train-numimage.json'
with open(infile, 'r', encoding='utf-8') as fp:
    data = json.load(fp)

def export_png(no):
    # 画像データを取り出す --- (※2)
    images = data['images'][no]
    # PILでピクセルデータを描画 --- (※3)
    img = Image.new('L', (28, 28))
    for y in range(28):
        for x in range(28):
            c = 255 - images[y * 28 + x] # --- (※3a)
            img.putpixel((x, y), c)
    # ファイルに保存 --- (※4)
    img.save('images/{}.png'.format(no))
    # ラベル番号を表示 --- (※5)
    print('label=', data['labels'][no])

# 適当に10枚取り出して出力 --- (※6)
for no in range(10):
    export_png(no)

