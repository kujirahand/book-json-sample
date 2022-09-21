from datetime import datetime
import pytz, json
import json, japanize_matplotlib
import matplotlib.pyplot as plt

# 設定の指定
INFILE = 'tweet_fix.json'

# 変数の各時間を0で初期化 --- (※1)
hour_dic = {'{:02d}'.format(h):0 for h in range(0, 24)}
fav_dic = {'{:02d}'.format(h):0 for h in range(0, 24)}
ret_dic = {'{:02d}'.format(h):0 for h in range(0, 24)}
total = 0

# JSONファイルを読む --- (※2)
data = json.load(open(INFILE, 'r', encoding='utf-8'))

# データを一つずつ数える --- (※3)
for line in data:
    tweet = line['tweet']
    # 日付を得る --- (※4)
    if 'created_at' not in tweet: continue
    created_at = tweet['created_at']
    # 文字列の日付をdatetimeで取得して日本時間に変換
    t = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
    t = t.astimezone(pytz.timezone('Asia/Tokyo'))
    # カウントする --- (※5)
    fav_count = int(tweet['favorite_count']) # いいねの数
    ret_count = int(tweet['retweet_count']) # リツイートの数
    fav_dic[t.strftime('%H')] += fav_count
    ret_dic[t.strftime('%H')] += ret_count
    hour_dic[t.strftime('%H')] += 1
    total += 1

# 集計処理(時間ごとの平均を求める) --- (※6)
fav_list = []
for h in range(0, 24):
    hh = '{:02d}'.format(h)
    cnt = hour_dic[hh] # その時間の投稿回数
    fav = fav_dic[hh] # いいねの数
    ret = ret_dic[hh] # リツイートの数
    fv = (fav / cnt) if cnt > 0 else 0 # 平均を出す
    rv = (ret / cnt) if cnt > 0 else 0
    fav_list.append([hh, fv, rv])
    print(hh, '{}÷{}='.format(fav, cnt), fv, rv)    

# グラフを描画するためにデータをラベルと値に分ける --- (※7)
labels = [v[0] for v in fav_list]
fav_values = [v[1] for v in fav_list]
ret_values = [v[2] for v in fav_list]
# グラフ描画 --- (※8)
plt.subplot(2, 1, 1)
plt.title('時間別「いいね」の平均')
plt.bar(labels, fav_values)

plt.subplot(2, 1, 2)
plt.title('時間別「リツイート」の平均')
plt.bar(labels, ret_values)
plt.show()
