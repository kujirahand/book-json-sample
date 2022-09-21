import json, japanize_matplotlib
import matplotlib.pyplot as plt

# プレイ履歴を読み込む --- (※1)
savefile = 'janken_history.json'
with open(savefile, encoding='utf-8') as fp:
    history = json.load(fp)

# 履歴を確認して勝敗を数える --- (※2)
win, lose, draw = 0, 0, 0
hand = [0, 0, 0] # どの手で勝ったか
for i in history:
    if i['result'] == 'あいこ':
        draw += 1
    if i['result'] == '負け':
        lose += 1
    if i['result'] == '勝ち':
        win += 1
        hand[i['user']] += 1
# 勝率を計算して表示
print('勝率:', win / (win + lose))
# 勝敗グラフを描画 --- (※3)
plt.subplot(1, 2, 1) # 左の円グラフを描画
plt.pie([win, lose, draw], labels=['勝ち', '負け', 'あいこ'], autopct="%1.1f %%")
plt.title('勝敗')
plt.subplot(1, 2, 2) # 右の棒グラフを描画
plt.barh(['グー', 'チョキ', 'パー'], hand)
plt.title('どの手で勝ったか')
plt.show()
