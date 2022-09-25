from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import random, json

# キノコデータを読み出す --- (※1)
data = json.load(open('mushroom_onehot.json', 'r'))

# 学習データとテストデータに分ける --- (※2)
x_train, x_test, y_train, y_test = train_test_split(
        data['data'], data['labels'], test_size=0.2)

# K−近傍法でデータを学習 --- (※3)
clf = KNeighborsClassifier()
clf.fit(x_train, y_train)

# 学習内容を元にしてテストデータを予測 --- (※4)
y_pred = clf.predict(x_test)

# 正解率を確認する --- (※5)
ok = 0
for i, v in enumerate(y_pred):
    if v == y_test[i]:
        ok += 1
        print(i, ':👌 正解', v)
    else:
        print(i, ':❌ 不正解', v, '!=', y_test[i])
print('正解数=', ok, '/', len(y_test))
print('正解率=', ok / len(y_test))
