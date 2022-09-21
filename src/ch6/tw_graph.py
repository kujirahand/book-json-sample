import json, japanize_matplotlib
import matplotlib.pyplot as plt 

INFILE_MONTH = 'tweet_month.json'
INFILE_HOUR = 'tweet_hour.json'
YEAR_FROM = 2018
YEAR_TO = 2022

# 集計データをファイルから読む --- (※1)
month_dic = json.load(open(INFILE_MONTH, 'r', encoding='utf-8'))
hour_dic = json.load(open(INFILE_HOUR, 'r', encoding='utf-8'))

# 月ごとのデータをラベルとデータに分割 --- (※2)
labels,values,x = [], [], []
for y in range(YEAR_FROM, YEAR_TO+1):
    for m in range(1, 12+1):
        key = '{}-{:02d}'.format(y, m)
        labels.append(key)
        values.append(month_dic[key])
        x.append(key if m == 1 else '')

# 左側に縦棒グラフを描画 --- (※3)
plt.subplot(1, 2, 1)
plt.bar(labels, values)
plt.xticks(x, rotation=0)
plt.title('Twitterで月ごとの投稿数')

# 時間帯ごとのデータをラベルとデータに分割 --- (※4)
x, y = [], []
for h in range(0, 24):
    # 7時から順に並べる
    key = '{:02d}'.format((h + 7) % 24) # --- (※4a)
    x.append(key + '時')
    y.append(hour_dic[key])

# 右側に横棒グラフを描画 --- (※5)
plt.subplot(1, 2, 2) # 右の棒グラフを描画
plt.barh(list(reversed(x)), list(reversed(y)))
plt.title('Twitterで時間ごとの投稿数')
plt.show()
