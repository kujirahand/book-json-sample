from flask import Flask, request, redirect, send_file
import json, os
from datetime import datetime
import sensor_graph

# 初期設定　--- (※1)
jsonfile = 'sensor.json'
pngfile = 'sensor.png'
app = Flask(__name__) # Flaskを生成

# サーバーのルートにアクセスがあった時 --- (※2)
@app.route('/')
def index():
    return "/save or <a href='/graph'>/graph</a>"

# JSONファイルを元にグラフを描画 --- (※3)
@app.route('/graph')
def graph():
    sensor_graph.draw_file(jsonfile, pngfile)
    # 描画したファイルを出力 --- (※4)
    return send_file(pngfile, mimetype='image/png')

# センサーの値を保存する --- (※5)
@app.route('/save')
def save():
    # 投稿されたデータを取得する --- (※6)
    t = request.args.get('t', '') # 温度
    h = request.args.get('h', '') # 湿度
    c = request.args.get('c', '') # CPU温度
    if t == '' or h == '' or c == '': return 'False'
    dt = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    # 取得した値をJSONに書き込む --- (※7)
    data = []
    if os.path.exists(jsonfile):
        with open(jsonfile, encoding='utf-8') as fp:
            data = json.load(fp)
    data.append({
        'time': dt, 
        'temp': float(t), 
        'humi': float(h),
        'cpu': float(c),
    })
    with open(jsonfile, 'w', encoding='utf-8') as fp:
        json.dump(data, fp)
    return 'True'

if __name__ == '__main__': # サーバー起動 --- (※8)
    app.run('0.0.0.0', 8889, debug=True)

