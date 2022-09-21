# クーポン発行システム
from flask import Flask, request, send_file
import os, pyqrcode, json, uuid, html

# 初期設定 --- (※1)
ROOT_DIR = os.path.dirname(__file__)
COUPON_JSON = os.path.join(ROOT_DIR, 'coupon.json')
QRCODE_PNG = os.path.join(ROOT_DIR, 'qrcode.png')
PORT_NO = 8888
ADMIN_PASSWORD='abcd' # パスワード
# Flaskを起動
app = Flask(__name__)

# 管理ページ
@app.route('/')
def index():
    # パラメータを得る --- (※2)
    param_pw = request.args.get('pw', '')
    if param_pw != ADMIN_PASSWORD:
        return "パスワードが違います"
    # クーポンの発行フォームを表示 --- (※3)
    return '''
    <html><meta charset="utf-8"><body>
    <h1>クーポンの発行</h1>
    <form action="/issue-coupon">条件を指定:<br>
    <textarea name="memo" rows="8" cols="60"></textarea><br>
    <input type="submit" value="発行">
    <input type="hidden" name="pw" value="{}">
    '''.format(html.escape(param_pw))

# クーポンの発行処理
@app.route('/issue-coupon')
def issue_coupon():
    # パラメータを得る --- (※4)
    param_pw = request.args.get('pw', '')
    param_memo = request.args.get('memo', '')
    if param_pw != ADMIN_PASSWORD or param_memo == '':
        return "パラメータが間違っています"
    # UUIDとURLを生成する --- (※5)
    id = str(uuid.uuid4())
    url = request.host_url + 'q?id=' + id
    # QRコードを作成 --- (※6)
    qrcode = pyqrcode.create(url)
    qrcode.png(QRCODE_PNG, scale=8)
    # JSONファイルにUUIDとメモを追記 ---(※7)
    data = {}
    if os.path.exists(COUPON_JSON):
        with open(COUPON_JSON, encoding='utf-8') as fp:
            data = json.load(fp)
    data[id] = {'memo': param_memo}
    with open(COUPON_JSON, 'w', encoding='utf-8') as fp:
        json.dump(data, fp)
    return '''
    <html><meta charset="utf-8"><body><h1>QRコード</h1>
    <img src="/qrcode.png?r={}"><br>{}</body></html>
    '''.format(id, url)

# PNGファイルを返す
@app.route('/qrcode.png')
def send_qrcode():
    return send_file(QRCODE_PNG, mimetype='image/png')

# クーポンの表示ページ
@app.route('/q')
def show_coupon():
    # パラメータを得る --- (※8)
    param_id = request.args.get('id', '')
    # JSONを読み出す --- (※9)
    with open(COUPON_JSON, encoding='utf-8') as fp:
        data = json.load(fp)
    if param_id not in data:
        return '不正なクーポンです'
    memo = data[param_id]['memo']
    return '''
    <html><meta charset="utf-8"><body>
    <h1>クーポンのご利用ありがとうございます</h1><hr>
    <h3>[利用条件]:<br>{}</h3><hr>id:{}</body></html>
    '''.format(html.escape(memo), html.escape(param_id))

if __name__ == '__main__': # サーバー起動
    app.run('0.0.0.0', PORT_NO, debug=True)
