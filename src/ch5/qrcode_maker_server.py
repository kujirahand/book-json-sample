from flask import Flask, request, send_file
import os, pyqrcode, time, html

# 初期設定
ROOT_DIR = os.path.dirname(__file__)
PNG_FILE = os.path.join(ROOT_DIR, 'qrcode.png')
app = Flask(__name__) # Flaskを生成

@app.route('/')
def index():
    # パラメータを得る --- (※1)
    q = request.args.get('q', 'https://example.com')
    if q != '':
        # QRコードをファイルに保存 --- (※2)
        qrcode = pyqrcode.create(q)
        qrcode.png(PNG_FILE, scale=8)
    # HTMLの入力フォームを出力 --- (※3)
    return '''
        <html><meta charset="UTF-8"><body>
        <p><form action="/" method="GET">
        埋め込む文字列:
        <input type="text" name="q" size="60" value="{}">
        <input type="submit" value="生成">
        </form></p>
        <img src="/qrcode.png?r={}">
    '''.format(html.escape(q), time.time())

@app.route('/qrcode.png')
def send_qrcode(): # PNGファイルを出力 --- (※4)
    return send_file(PNG_FILE, mimetype='image/png')

if __name__ == '__main__': # サーバー起動 --- (※5)
    app.run('0.0.0.0', 8888, debug=True)
