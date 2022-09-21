from flask import Flask, request, redirect
import json, os
from datetime import datetime

# 初期設定　--- (※1)
jsonfile = 'dht11.json' # 保存先のファイルを指定
app = Flask(__name__) # Flaskを生成

# アクセスがあったとき --- (※2)
@app.route('/')
def index():
    # 投稿されたデータを取得する --- (※3)
    t = request.args.get('t', '') # 温度
    h = request.args.get('h', '') # 湿度
    if t == '' or h == '': return 'False'
    dt = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    # 取得した値をJSONに書き込む --- (※4)
    data = []
    if os.path.exists(jsonfile):
        with open(jsonfile, encoding='utf-8') as fp:
            data = json.load(fp)
    data.append({
        'time': dt, 
        'temp': float(t), 
        'humi': float(h)
    })
    with open(jsonfile, 'w', encoding='utf-8') as fp:
        json.dump(data, fp)
    return 'True'

if __name__ == '__main__': # サーバー起動 --- (※5)
    app.run('0.0.0.0', 8787, debug=True)


