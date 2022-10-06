import base64
infile = 'image.png'
# 画像ファイルを読み込む
with open(infile, 'rb') as fp:
    bin_data = fp.read()
# Base64にエンコード
enc = base64.b64encode(bin_data)
b64str = enc.decode('utf-8')
print(b64str)

