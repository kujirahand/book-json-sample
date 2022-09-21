import json
value = json.loads('null') # JSON の null を変換
# 変数 value が None かどうかを判定する
if value is None:
    print('値はnullでした')
else:
    print(value)

