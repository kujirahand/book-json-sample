import json, japanize_matplotlib
import matplotlib.pyplot as plt 
import re

INFILE = 'your_posts_fixed.json'

# FacebookのJSONファイルを読む --- (※1)
data = json.load(open(INFILE, 'r', encoding='utf-8'))
# 投稿からURLを収集する --- (※2)
total = 0
count_dic = {}
for p in data:
    # 投稿データ(data.post)がなければ飛ばす
    if 'data' not in p: continue
    if 'post' not in p['data'][0]: continue
    post = p['data'][0]['post']
    # 投稿の中にあるURLを調べる --- (※3)
    urls = re.findall(r'https?\:\/\/[a-zA-Z0-9\.\-\_]+', post)
    for url in urls:
        if url not in count_dic: count_dic[url] = 0
        count_dic[url] += 1
        total += 1
# カウントした内容を出力 --- (※4)
count_list = sorted(count_dic.items(), key=lambda v:v[1])
print(count_list)
# その他をまとめつつ、データをラベルとデータに分割 --- (※5)
labels, values = [], []
other = 0 # その他の数
for url, v in count_list:
    if v > total * 0.05: # 比率0.05以上ならまとめない
        labels.append(url)
        values.append(v)
    else:
        other += v
labels.append('その他')
values.append(other)
# グラフを描画 --- (※6)
plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title('言及しているURLの一覧')
plt.show()
