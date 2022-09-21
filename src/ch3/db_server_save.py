from flask import Flask, request
from datetime import datetime
import kudb

# 初期設定 --- (※1)
dbfile = 'sensor.db'
app = Flask(__name__) # Flaskを生成

# サーバーのルートにアクセスがあった時 --- (※2)
@app.route('/')
def index():
    return "Please send data to /save."

# センサーの値を保存する --- (※3)
@app.route('/save')
def save():
    # 受信したデータを取り出す --- (※4)
    t = request.args.get('t', '') # 温度
    h = request.args.get('h', '') # 湿度
    c = request.args.get('c', '') # CPU温度
    if t == '' or h == '' or c == '': return 'False'
    dt = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    # 取得した値をデータベースに書き込む --- (※5)
    kudb.connect(dbfile)
    kudb.insert({
        'time': dt, 
        'temp': float(t), 
        'humi': float(h),
        'cpu': float(c),
    })
    return 'True'

if __name__ == '__main__': # サーバー起動 --- (※6)
    app.run('0.0.0.0', 8889, debug=True)
