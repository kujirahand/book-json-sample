from flask import Flask, request
import os, json, hashlib

# 初期設定 --- (※1)
ROOT_DIR = os.path.dirname(__file__)
TICKET_JSON = os.path.join(ROOT_DIR, 'ticket.json')
PORT_NO = 8888
TOKEN_SALT = 'CprRbjI#uO_yt7kbcE' # a_make_qrcode.pyと同じものを指定

app = Flask(__name__) # Flaskを生成

@app.route('/')
def index():
    return show_html('スマートフォンのカメラでQRコードを読み込んでください。')

# QRコードの正当性をチェックする --- (※2)
@app.route('/check')
def check():
    # パラメータを得る --- (※3)
    param_no = request.args.get('no', '')
    param_token = request.args.get('token', '')
    try:
        no = int(param_no)
    except:
        return error_html('不正なチケットです。')
    # 正しいチケットかどうかを確認する --- (※4)
    data = []
    if os.path.exists(TICKET_JSON):
        with open(TICKET_JSON, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
    if no >= len(data): error_html('不正なチケットです。')
    # トークンの値を計算する --- (※5)
    password = data[no]['password']
    token_str = str(no) + '::' + password + '::' + TOKEN_SALT
    token_hash = hashlib.sha256(token_str.encode('utf-8')).hexdigest()
    if param_token != token_hash:
        return error_html('不正なチケットです。')
    # 正しいチケット - 利用回数を示す --- (※6)
    if 'times' not in data[no]: data[no]['times'] = 0
    data[no]['times'] += 1
    with open(TICKET_JSON, 'w', encoding='utf-8') as fp:
        json.dump(data, fp)
    return show_html('''
        <h1 class="title">正しいチケットです</h1>
        <h2 class="title">利用回数: {}</h2>
        <p>チケット番号: {}</p>
        <p>トークン: {}</p>
        '''.format(data[no]['times'], param_no, param_token))

def error_html(msg): # エラーを表示
    return show_html('<h1 class="title has-text-danger">'+msg+'</h1>')

def show_html(msg): # HTMLを表示
    return '''
    <html><meta charset="UTF-8">
    <meta name=”viewport” content=”width=device-width,initial-scale=1″>
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <body style="margin:0.5em">
        <div class="box">{}</div>
    </body></html>
    '''.format(msg)

if __name__ == '__main__': # サーバー起動
    app.run('0.0.0.0', PORT_NO, debug=True)
