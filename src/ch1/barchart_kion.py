import csv, japanize_matplotlib
import matplotlib.pyplot as plt 
# 気温CSVファイルを読む --- (※1)
reader = csv.reader(open('kion_data_trim.csv', encoding='sjis'))
data = list(reader)
# ラベル行と気温データを変数に割り振る --- (※2)
labels = data[0]
temps = [float(v) for v in data[1]] #---(※3)
# グラフを描画 --- (※4)
plt.bar(labels, temps)
plt.title('最高気温')
plt.show()
