import json, requests, japanize_matplotlib
import matplotlib.pyplot as plt

# Web APIから好きなOSに関するJSONデータを取得 --- (※1)
url = 'https://api.aoikujira.com/like/api.php?m=get&item_id=8'
r = requests.get(url)

# 取得したJSONをPythonで扱えるように変換 --- (※2)
data = json.loads(r.text)

# グラフ描画のためにデータを分ける --- (※3)
labels, values = [], []
for it in data['answers']:
    labels.append(it['label'])
    values.append(it['point'])

# グラフを描画 --- (※4)
plt.barh(labels, values)
plt.title('好きなOSは?') 
plt.show()


