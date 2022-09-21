from flask import Flask, send_file
import sensor_graph2
import kudb

# 初期設定 --- (※1)
dbfile = 'sensor.db'
pngfile = 'db_sensor.png'
app = Flask(__name__) # Flaskを生成

# サーバーのルートにアクセスがあった時レポートを返す --- (※2)
@app.route('/')
def index():
    # HTML/JavaScriptで自動更新する画面を返す --- (※3)
    return """
    <html><meta charset="utf-8"><body>
        <h1>レポート(10秒に1回自動更新)</h1>
        <img id="g" style="width:99%"><br>
        <script>
        // グラフのリロードを行う
        function loadGraph() {
            const f = '/graph.png?r=' + (new Date()).getTime()
            document.getElementById('g').src = f
            console.log(f)
            setTimeout(()=>{ loadGraph() }, 1000 * 10)
        }
        loadGraph()
        </script>
    </body></html>
    """

# データベースから値を取り出しグラフを作成 --- (※4)
@app.route('/graph.png')
def graph_png():
    kudb.connect(dbfile)
    data = kudb.recent(100) # 最近の100件のみ処理
    sensor_graph2.draw_graph(data, pngfile)
    # 描画したファイルを出力 --- (※5)
    return send_file(pngfile, mimetype='image/png')

if __name__ == '__main__': # サーバー起動 --- (※6)
    app.run('0.0.0.0', 8888, debug=True)
