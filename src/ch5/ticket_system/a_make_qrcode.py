from flask import Flask, request
import os, pyqrcode, json, secrets, hashlib

# 初期設定 --- (※1)
ROOT_DIR = os.path.dirname(__file__)
TICKET_JSON = os.path.join(ROOT_DIR, 'ticket.json')
QRCODE_DIR = os.path.join(ROOT_DIR, 'qrcode')
if not os.path.exists(QRCODE_DIR): os.mkdir(QRCODE_DIR)
PORT_NO = 8888
TOKEN_SALT = 'CprRbjI#uO_yt7kbcE' # ランダムな文字列を指定

# 静的ディレクトリを指定してFlaskを生成 --- (※2)
app = Flask(__name__, static_folder=QRCODE_DIR)

# 発券ボタンを表示する --- (※3)
@app.route('/')
def index():
    return show_html('''
    <h1 class="title">新規チケットの発券</h1>
    <a class="button" href="/issue">新規発行</a>
    ''')
# QRコードを発券する --- (※4)
@app.route('/issue')
def issue():
    # 既存のJSONデータを読み出す --- (※5)
    data = []
    if os.path.exists(TICKET_JSON):
        with open(TICKET_JSON, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
    no = len(data)
    # 不正対策用のトークンを生成する --- (※6)
    random_password = secrets.token_hex(16) # ランダムなパスワードを生成
    token_str = str(no) + '::' + random_password + '::' + TOKEN_SALT
    token_hash = hashlib.sha256(token_str.encode('utf-8')).hexdigest()
    # QRコードに埋め込むURLを決定する --- (※7)
    url = 'http://' + request.host + \
        '/check?no={}&token={}'.format(no, token_hash)
    # チケットのQRコードを生成 --- (※8)
    fname = '{}_{}.png'.format(no, token_hash)
    qrcode = pyqrcode.create(url)
    qrcode.png(os.path.join(QRCODE_DIR, fname), scale=8)
    # JSONファイルに情報を保存 --- (※9)
    data.append({'no': no, 'password': random_password})
    with open(TICKET_JSON, 'w', encoding='utf-8') as fp:
        json.dump(data, fp)
    # 画面にQRコードを表示する --- (※10)
    return show_html('''
    <h1 class="title">発券したチケット - {}番</h1>
    <img src="/qrcode/{}"><br>
    <p>QRコード: <input value="{}" size="60"></p>
    <a class="button" href="/">戻る</a>
    '''.format(no, fname, url))

def show_html(msg):
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
