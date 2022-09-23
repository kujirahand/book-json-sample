# ライブラリを取り込む
import matplotlib.pyplot as plt

# データを用意する
values = [60, 30, 10]
labels = ['A', 'B', 'C']

# 円グラフを描画する
plt.pie(values, labels=labels)
plt.show()

