import os, pyqrcode, time, html
from PIL import Image, ImageDraw, ImageFilter
# 描画色を指定
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
# QRコードを描画する --- (※1)
def qrmake(savefile, data, width=300, artfile=None, draw_mode='photo'):
    # QRコードをテキストで得る --- (※2)
    qrcode = pyqrcode.create(data, error='H')
    text = qrcode.text(quiet_zone=0)
    # サイズを計算する -- (※3)
    lines = text.split('\n')
    dot = len(lines[0])
    w = int(width / dot) # 1マスの大きさ
    pad = ((width - (w * dot)) / 2) # 余白
    # 空の画像を作成 --- (※4)
    img = Image.new('RGBA', (width, width), WHITE)
    draw = ImageDraw.Draw(img)
    # QRコードを描画 --- (※5)
    for y, line in enumerate(lines):
        yy = y * w + pad
        for x, c in enumerate(list(line)):
            xx = x * w + pad
            if c == '1':
                draw.rectangle(((xx, yy), (xx+w, yy+w)), fill=BLACK)
    # 重ね合わせるアート画像を処理 --- (※6)
    if artfile is not None:
        artw = int(width * 0.3) # 画像サイズ30%が限界
        # 画像ファイルを読む --- (※7)
        with Image.open(artfile) as artimg:
            artimg = artimg.convert('RGBA')
            artimg.thumbnail((artw, artw)) # 比率変えずリサイズ
            aw, ah = artimg.size # 実際のサイズ
            if draw_mode == 'photo':
                # 丸く切り抜くためのマスクを準備 --- (※8)
                mask_im = Image.new('L', (aw, ah))
                mask_d = ImageDraw.Draw(mask_im)
                mask_d.ellipse((0, 0, aw, ah), fill=255)
                mask_im = mask_im.filter(ImageFilter.GaussianBlur(1))
                # 画像をマスク付きで重ね合わせる --- (※9)
                img.paste(artimg, ((width-aw)//2, (width-ah)//2), mask=mask_im)
            if draw_mode == 'logo': # 単純に重ね合わせる
                mask_im = Image.new('L', (aw, ah), color=255)
                img.paste(artimg, ((width-aw)//2, (width-ah)//2), mask=mask_im)
    img.save(savefile) # 画像を保存 --- (※10)

if __name__ == '__main__':
    qrmake('custom1.png', 'https://example.com', artfile='lemon.jpg')
    qrmake('custom2.png', 'https://example.com', artfile='logo.png', draw_mode='logo')

