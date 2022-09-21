import json
from datetime import datetime

# 入力ファイルと出力ファイルを指定
IN_FILE = 'your_posts_fixed.json'
OUT_FILE = 'posts_per_month.json'
# いつからいつまでの統計をとるか
YEAR_FROM = 2018
YEAR_TO = 2022

# 月ごとの投稿数を数えるためにカウンタを初期化 --- (※1)
counter = {}
for year in range(YEAR_FROM, YEAR_TO+1):
    for month in range(1, 12+1):
        counter['%d-%02d' % (year, month)] = 0
# JSONファイルを読み込む --- (※2)
data = json.load(open(IN_FILE, 'r', encoding='utf-8'))
# データを一つずつ確認 --- (※3)
for line in data:
    # 投稿以外のデータを読み飛ばす --- (※4)
    if 'data' not in line: continue
    timestamp = line['timestamp']
    data = line['data']
    # 空のデータを読み飛ばす
    if len(data) == 0: continue
    if 'post' not in data[0]: continue
    post = data[0]['post']
    # タイムスタンプをdatetimeに変換 --- (※5)
    dt = datetime.fromtimestamp(timestamp)
    # datetimeを「年-月」に変換 --- (※6)
    dt_key = dt.strftime('%Y-%m')
    # 「年-月」ごとに投稿を数える --- (※7)
    if dt_key not in counter: continue # 範囲外なら数えない
    counter[dt_key] += 1 # カウント
# 結果をJSONで出力 --- (※8)
json.dump(counter, open(OUT_FILE, 'w', encoding='utf-8'))

