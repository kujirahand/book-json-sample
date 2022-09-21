import json, japanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# JSONを読む --- (※1)
data = json.load(open('bbs_logs.json', encoding='utf-8'))
# 以下のデータを埋めるように数える --- (※2)
result = {
    '緊急': {'解決': 0, '未解決': 0}, 
    '高':{'解決':0, '未解決': 0}, 
    '中':{'解決':0, '未解決': 0}, 
    '低':{'解決':0, '未解決': 0}, 
}
for row in data:
    st = row['status']
    pr = row['priority']
    if st == '解決': result[pr]['解決'] += 1
    if st == '未処理' or st == '修正中' or st == '再修正依頼':
        result[pr]['未解決'] += 1
print(result)
# グラフを描画 --- (※3)
df = pd.DataFrame({
    '解決': [v['解決'] for k,v in result.items()],
    '未解決': [v['未解決'] for k,v in result.items()]
}, index=[k for k,_ in result.items()])
df.plot(kind="barh",stacked=True,figsize=(10,8))
plt.show()
