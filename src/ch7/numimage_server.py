from flask import Flask, request, send_file
import joblib

# 学習済みの手書き数字のモデルを読み込む --- (※1)
app = Flask(__name__)
clf = joblib.load('images/numimage.model')

# HTMLファイルを出力する --- (※2)
@app.route('/')
def index():
    return send_file('numimage_test.html')

# 手書きデータを読み込んで判定を行って返す --- (※3)
@app.route('/api')
def api():
    q = request.args.get('q', '') # パラメータを得る
    if q == '': return '?'
    # 手書きデータを数値に変換 --- (※4)
    q_list = list(map(lambda v:int(v)*255, list(q)))
    # どの数字か分類する --- (※5)
    r_list = clf.predict([q_list[0:28*28]])
    return str(r_list[0]) # 結果を返す

if __name__ == '__main__':
    app.run('0.0.0.0', 8888, debug=True)

