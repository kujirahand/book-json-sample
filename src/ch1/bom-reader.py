import json
with open('bom-test.txt', 'r', encoding='utf-8') as fp:
    # ファイルの内容を文字列に全部読む --- (※1)
    text = fp.read()
# 最初の1文字(2バイト)を確認してBOMなら読み飛ばす --- (※2)
if ord(text[0:1]) == 0xFEFF:
    text = text[1:] # 読み飛ばす
# JSON文字列をPythonのデータに変換 --- (※3)
data = json.loads(text)
print(data)

