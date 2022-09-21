import json
# 表示したいデータ
data = { '名前': '鈴木', '趣味': ['読書', 'プログラミング', '盆栽']}
# 分かりやすくJSONを出力
print(json.dumps(
    data, 
    indent=4, 
    ensure_ascii=False))

