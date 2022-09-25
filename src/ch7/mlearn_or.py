import json
from sklearn import svm

# OR演算の学習データを読む --- (※1)
data_or = json.load(open('data_or.json'))

# 学習のためにラベルとデータに分ける --- (※2)
data = []
labels = []
for row in data_or:
    data.append(row['data'])
    labels.append(row['label'])

# 機械学習にSVMアルゴリズムを使う --- (※3)
clf = svm.SVC()
# データを学習 --- (※4)
clf.fit(data, labels)

# 機械学習でOR演算が解けるか確認 --- (※5)
test_data = [[1,0], [0,0], [1,1]]
pre = clf.predict(test_data)
for i, data in enumerate(test_data):
    print('+ テスト:', data)
    print('|   予測:', pre[i])
    print('|   答え:', data[0] or data[1])


