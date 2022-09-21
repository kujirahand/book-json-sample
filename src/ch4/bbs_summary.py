import json, japanize_matplotlib
import matplotlib.pyplot as plt

# JSONを読む --- (※1)
data = json.load(open('bbs_logs.json', encoding='utf-8'))
# データを数える --- (※2)
priority = {}
status = {}
for row in data:
    pr = row['priority']
    st = row['status']
    if pr not in priority: priority[pr] = 0
    if st not in status: status[st] = 0
    priority[pr] += 1
    status[st] += 1
print(priority)
print(status)
# グラフを描画 --- (※3)
fig = plt.figure()
# 優先度の円グラフを描画
ax1 = fig.add_subplot(1, 2, 1)
values = [v for _,v in priority.items()]
labels = [k for k,_ in priority.items()]
ax1.pie(values, labels=labels, autopct="%.1f")
ax1.set_title('優先度')
# 状態の円グラフを描画
ax2 = fig.add_subplot(1, 2, 2)
values = [v for _,v in status.items()]
labels = [k for k,_ in status.items()]
ax2.barh(labels, values)
ax2.set_title('状態')
plt.legend()
plt.show()
