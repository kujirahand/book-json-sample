from flask import Flask, request, session, redirect
import pyqrcode, io, base64, html, json, hashlib, secrets

PORT_NO = 8888
SECRET_KEY = 'n92aYUkg#ZFiFVv_zL' # トークン生成用
app = Flask(__name__)
app.secret_key = 'wiDbpbbV65XxyOSM'

@app.route('/')
def index_page():
    # 整理券発行フォームを表示するか？ --- (※1)
    name = request.args.get('name', '')
    if name == '': # フォームを表示 --- (※2)
        return '''
        <html><meta charset="utf-8"><body>
        <h1>整理券発行フォーム</h1>
        <form action="/" method="GET">
        お名前:<br>
        <input type="text" name="name" value="">
        <input type="submit" value="発行">
        </form>
        '''
    # QRコードに埋め込むデータを作成
    qno = session.get('qno', 1)
    salt = secrets.token_hex(8)
    s = (SECRET_KEY + name + salt).encode('utf-8')
    token = hashlib.sha256(s).hexdigest()
    data = json.dumps({'name': name, 'qno': qno, 'token': token, 'salt': salt})
    # QRコードをインメモリで作成 --- (※5)
    buf = io.BytesIO()
    pyqrcode.create(data).png(buf, scale=3)
    png = base64.b64encode(buf.getvalue()).decode("ascii")
    # 整理券番号を1つ進める
    session['qno'] = qno + 1
    # 会員証のHTMLを表示 --- (※6)
    return '''
    <html><meta charset="utf-8"><body>
    <h1>整理券:{qno}番 - {name}様</h1>
    <img src="data:image/png;base64,{png}" width="400">
    <br><br><br><hr><a href="/">戻る</a>
    </body></html>
    '''.format(name=html.escape(name), qno=qno, png=png)

if __name__ == '__main__':
    app.run('0.0.0.0', PORT_NO, debug=True)
