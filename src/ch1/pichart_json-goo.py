import json, japanize_matplotlib
import matplotlib.pyplot as plt
# JSONを読み込む --- (※1)
data = json.load(open('pi-goo.json', encoding='utf-8'))
# 描画のために値とラベルを分ける --- (※2)
values = [i[0] for i in data]
labels = [i[1] for i in data]
# 円グラフを描画 --- (※3)
plt.pie(values, labels=labels)
plt.show()
