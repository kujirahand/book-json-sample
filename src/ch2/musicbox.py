from flask import Flask, request, redirect
import json, os, platform, subprocess
import json2midi
# 初期設定　--- (※1)
root = os.path.dirname(__file__)
logfile = os.path.join(root, 'musicbox.json')
midifile = os.path.join(root, 'musicbox.mid')
print("MIDIファイル=", midifile)
app = Flask(__name__) # Flaskを生成

# ルートにアクセスした時に実行する処理を指定 --- (※2)
@app.route('/')
def index():
    return make_top_page_html()

# フォームから投稿した時 --- (※3)
@app.route('/play')
def form_write():
    # 投稿されたデータを取得する --- (※4)
    gakufu = []
    for row in range(32):
        c = int(request.args.get('g' + str(row), '-1'))
        note = (12 * 5 + c) if c != -1 else -1
        gakufu.append({'note': note, 'length': 240})
    with open(logfile, 'w', encoding='utf-8') as fp:
        json.dump(gakufu, fp)
    json2midi.save_to_midi(gakufu, midifile)
    play_midi(midifile)
    return redirect('/') # トップページに移動

def play_midi(midfile):
    # MIDIを再生する --- (※5)
    if platform.system() == 'Windows':
        os.system(midfile) # 関連付けで開く
    else:
        cmd = ['timidity', midfile]
        subprocess.call(cmd)

def make_top_page_html():
    # 鍵盤に見立てたラジオボックスをたくさん作る --- (※6)
    w, g = ('white', 'gray')
    colors = [w,g,w,g,w,w,g,w,g,w,g,w]
    mbox = '<table>'
    for row in range(32):
        s = '<tr>'
        for col in range(24):
            s += '''
            <td style='background-color:{};' border=1>
                <input type="radio" name="g{}" value="{}"'>
            </td>
            '''.format(colors[col%12], row, col)
        mbox += s + '</tr>\n'
        if row % 8 == 7: mbox += '<tr><td colspan="24"><tr>'
    mbox += '</table>'
    # HTMLを返す
    return '''
    <!DOCTYPE html><html><head><meta charset="UTF-8">
    <title>オルゴール</title>
    </head><body>
    <h1>オルゴール</h1>
    <form action="/play" method="GET">
    <input type="submit" value="再生"><br>{}
    </form></body></html>
    '''.format(mbox)

if __name__ == '__main__': # Webサーバーを起動 --- (※7)
    app.run('127.0.0.1', 8888, debug=True)
