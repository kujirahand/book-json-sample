import json, japanize_matplotlib
import matplotlib.pyplot as plt 

# 人口推移のJSONファイルを読む --- (※1)
data = json.load(open('pop.json', encoding='utf-8'))

# 複数の線グラフを描画するようにデータを分割 --- (※2)
x, totals, man, woman = [],[],[],[]
for row in data:
    x.append(row['year']) # 西暦年
    totals.append(row['total']) # 男女合計
    man.append(row['man']) # 男性
    woman.append(row['woman']) # 女性

# グラフを描画 --- (※3)
p_total = plt.plot(x, totals, label='合計(千人)')
p_woman = plt.plot(x, woman, marker='.', label='女')
p_man = plt.plot(x, man, marker='x', label='男')
plt.legend() # 凡例を表示 --- (※4)
plt.show()

