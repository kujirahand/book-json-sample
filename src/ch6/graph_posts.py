import json, japanize_matplotlib
import matplotlib.pyplot as plt 

INFILE = 'posts_per_month.json'

# JSONファイルを読む --- (※1)
data = json.load(open(INFILE, 'r', encoding='utf-8'))
# データをラベルとデータに分割 --- (※2)
labels = [t for t,v in data.items()]
values = [v for t,v in data.items()]
# 毎年1月のみラベルを表示する --- (※3)
show_labels = [(k if (i % 12 == 0) else '') for i,k in enumerate(data)]
# グラフを描画 --- (※4)
plt.bar(labels, values)
plt.xticks(show_labels, rotation=0)
plt.title('月ごとの投稿数')
plt.show()
