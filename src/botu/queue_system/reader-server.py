from flask import Flask, request, send_file
import pyqrcode, io, base64, html, json, hashlib, secrets

PORT_NO = 8888
SECRET_KEY = 'n92aYUkg#ZFiFVv_zL' # トークン生成用
app = Flask(__name__)

@app.route('/')
def index_page():
    return send_file('reader.html', mimetype='text/html; charset=UTF-8')

if __name__ == '__main__':
    app.run('0.0.0.0', PORT_NO, debug=True)
