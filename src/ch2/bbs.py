from flask import Flask, request, redirect
import json, os, time, html
from datetime import datetime
# 初期設定　--- (※1)
logfile = 'bbs_log.json' # 保存先のファイルを指定
logdata = {'lastid': 0, 'logs': []}
app = Flask(__name__) # Flaskを生成

# ルートにアクセスした時に実行する処理を指定 --- (※2)
@app.route('/')
def index():
    return make_top_page_html()

# フォームから投稿した時 --- (※3)
@app.route('/write')
def form_write():
    # 投稿されたデータを取得する --- (※4)
    name = request.args.get('name', '')
    msg = request.args.get('msg', '')
    # パラメータのチェック --- (※5)
    if name == '' or msg == '': return 'パラメータの指定エラー'
    # データを保存 --- (※6)
    append_log({'name': name, 'msg': msg, 'time': time.time()})
    return redirect('/') # トップページに移動

# JSONファイルを読み込む --- (※7)
def load_log():
    global logdata
    if os.path.exists(logfile):
        with open(logfile, encoding='utf-8') as fp:
            logdata = json.load(fp)

# JSONファイルにデータを追記する --- (※8)
def append_log(record):
    logdata['lastid'] += 1
    record['id'] = logdata['lastid']
    logdata['logs'].append(record) # データを追記
    with open(logfile, 'w', encoding='utf-8') as fp:
        json.dump(logdata, fp) # ファイルに書き込む

def make_logs():
    # 書き込まれたログを元にしてHTMLを生成して返す --- (※9)
    s = ''
    for log in reversed(logdata['logs']):
        name = html.escape(log['name']) # 名前をHTMLに変換 --- (※10)
        msg = html.escape(log['msg']) # メッセージをHTMLに変換
        t = datetime.fromtimestamp(log['time']).strftime('%m/%d %H:%M')
        s += '''
        <div class="box">
            <div class="has-text-info">({}) {} さん</div>
            <div>{}</div>
            <div class="has-text-right is-size-7">{}</div>
        </div>
        '''.format(log['id'], name, msg, t)
    return s

def make_top_page_html():
    # 掲示板のメインページを生成して返す --- (※11)
    return '''
    <!DOCTYPE html><html><head><meta charset="UTF-8">
    <title>掲示板</title>
    <link rel="stylesheet" 
     href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    </head><body>
    <!-- タイトル -->
    <div class="hero is-dark"><div class="hero-body">
        <h1 class="title">掲示板</h1>
    </div></div>
    <!-- 書き込みフォーム -->
    <form class="box" action="/write" method="GET">
    <div class="field">
        <label class="label">お名前:</label>
        <div class="controll">
            <input class="input" type="text" name="name" value="名無し">
        </div>
    </div>
    <div class="field">
        <label class="label">メッセージ:</label>
        <div class="controll">
            <input class="input" type="text" name="msg">
        </div>
    </div>
    <div class="field">
        <div class="controll">
            <input class="button is-primary" type="submit" value="投稿">
        </div>
    </div>
    </form>
    ''' + make_logs() + '''</body></html>'''

if __name__ == '__main__': # Webサーバーを起動 --- (※12)
    load_log() # ログデータを読み込む
    app.run('127.0.0.1', 8888, debug=True)
