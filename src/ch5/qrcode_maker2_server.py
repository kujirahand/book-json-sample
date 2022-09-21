from flask import Flask, request, send_file
import os, time, html
import qrcode_custom # --- (※1)

# 初期設定 --- (※2)
ROOT_DIR = os.path.dirname(__file__)
PNG_FILE = os.path.join(ROOT_DIR, 'qrcode.png')
app = Flask(__name__) # Flaskを生成

@app.route('/')
def index():
    # パラメータを得る --- (※3)
    q = request.args.get('q', 'https://example.com')
    f = request.args.get('f', 'lemon.jpg')
    m = request.args.get('m', 'photo')
    if not os.path.exists(f): f = 'lemon.jpg'
    # QRコードを生成してファイルに保存 --- (※4)
    qrcode_custom.qrmake(PNG_FILE, q, artfile=f, draw_mode=m)
    # HTMLの入力フォームを出力 --- (※5)
    return '''
        <html><meta charset="UTF-8"><body>
        <div style="padding:1em;"><form action="/" method="GET">
        埋め込む文字列:
        <input type="text" name="q" size="60" value="{}"><br>
        画像ファイル名:
        <input type="text" name="f" size="60" value="{}"><br>
        描画方法(photo|logo):
        <input type="text" name="m" size="30" value="{}">
        <input type="submit" value="生成"></form>
        <img src="/qrcode.png?r={}"></div>
        </body></html>
    '''.format(html.escape(q), html.escape(f), 
            html.escape(m), time.time())

@app.route('/qrcode.png')
def send_qrcode(): # PNGファイルを出力
    return send_file(PNG_FILE, mimetype='image/png')

if __name__ == '__main__': # サーバー起動
    app.run('0.0.0.0', 8888, debug=True)
