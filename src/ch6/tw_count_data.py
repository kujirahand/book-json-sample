from datetime import datetime
import pytz, json

# 設定の指定
INFILE = 'tweet_fix.json'
OUTFILE_MONTH = 'tweet_month.json'
OUTFILE_HOUR = 'tweet_hour.json'
YEAR_FROM = 2018
YEAR_TO = 2022

# 月ごとの集計 - "年-月"の書式で辞書型を初期化 --- (※1a)
month_dic = {}
for y in range(YEAR_FROM, YEAR_TO+1):
    for m in range(1, 12+1):
        month_dic['{}-{:02d}'.format(y, m)] = 0
# 時間ごとの集計 - どの時間帯にツイートしているか --- (※1b)
hour_dic = {'{:02d}'.format(h):0 for h in range(0, 24)}

# JSONファイルを読む --- (※2)
data = json.load(open(INFILE, 'r', encoding='utf-8'))

# データを一つずつ数える --- (※3)
for line in data:
    tweet = line['tweet']
    # 日付を得る --- (※4)
    if 'created_at' not in tweet: continue
    created_at = tweet['created_at']
    # 文字列の日付をdatetimeで取得(Wed Jun 22 01:22:24 +0000 2022) --- (※5)
    t = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
    # 日本時間に変換 --- (※6)
    t = t.astimezone(pytz.timezone('Asia/Tokyo'))
    # 範囲外の年度をスキップ
    if not (YEAR_FROM <= t.year <= YEAR_TO): continue
    # カウントする --- (※7)
    month_dic[t.strftime('%Y-%m')] += 1
    hour_dic[t.strftime('%H')] += 1

# 結果を画面に出力 --- (※8)
print('月ごとの集計:')
print(month_dic)
print('時間ごとの集計:')
print(hour_dic)
# ファイルに保存 --- (※9)
json.dump(month_dic, open(OUTFILE_MONTH, 'w', encoding='utf-8'))
json.dump(hour_dic, open(OUTFILE_HOUR, 'w', encoding='utf-8'))
