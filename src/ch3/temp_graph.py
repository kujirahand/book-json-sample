import sys, json, japanize_matplotlib, re
import matplotlib.pyplot as plt
# 読み込み対象ファイルを確認 --- (※1)
jsonfile = "2022-07-31.json" # サンプルファイル
if len(sys.argv) >= 2:
    jsonfile = sys.argv[1]
data = json.load(open(jsonfile, encoding='utf-8'))
# 線グラフを描画するようにデータを分割 --- (※2)
x, temp, xx = [],[],[]
for i, row in enumerate(data):
    x.append(row['time'].split(' ')[1]) # 時間
    if (i % (60 * 4) == 0): xx.append(i)
    temp.append(float(row['temp'])) # 温度
# グラフを描画 --- (※3)
fig = plt.figure()
fig.set_size_inches(8, 4)
plt.plot(x, temp, label='温度', linewidth=0.7)
plt.xticks(xx, rotation=0) # 間引いて表示 --- (※4)
plt.legend() # 凡例を表示 --- (※5)
plt.savefig("temp_graph.png", dpi=300) # --- (※6)

