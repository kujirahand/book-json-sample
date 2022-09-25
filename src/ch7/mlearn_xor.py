import json
from sklearn import svm

# XOR演算の学習データを読む --- (※1)
data_xor = json.load(open('data_xor.json'))

# 学習のためにラベルとデータに分ける --- (※2)
data = []
labels = []
for row in data_xor:
    data.append(row['data'])
    labels.append(row['label'])

# SVMで学習 --- (※3)
clf = svm.SVC()
clf.fit(data, labels)

# 機械学習でXOR演算が解けるか確認 --- (※4)
labels_pred = clf.predict(data)

# 正しく判定できたか確認して正解率を出す --- (※5)
ok = 0
for i, pred in enumerate(labels_pred):
    ans = '👌 ok' if pred == labels[i] else '❌ ng'
    print('-', data[i], '>', pred, ans)
    ok += 1
print('正解率:', ok / len(data))

