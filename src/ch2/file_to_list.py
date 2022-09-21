import json
# ファイルから文字列を読み込む
with open('a_list.json', encoding='utf-8') as fp:
    json_str = fp.read()
# JSON文字列をPythonのデータにデシリアライズ
a_list = json.loads(json_str)
# 読み出したデータを表示
for s in a_list:
    print(s)

    
