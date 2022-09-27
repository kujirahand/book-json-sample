from sklearn import svm
import joblib
import json

# 学習用データを読み込む --- (※1)
with open('images/train-numimage.json', 'r') as fp:
    train = json.load(fp)

# SVMでデータを学習する --- (※2)
clf = svm.SVC(verbose=True)
clf.fit(train['images'], train['labels'])

# 学習結果のモデルをファイルに保存 --- (※3)
joblib.dump(clf, 'images/numimage.model')

# テスト用データを読む --- (※4)
with open('images/test-numimage.json', 'r') as fp:
    test = json.load(fp)

# 作成したモデルの精度をテスト --- (※5)
score = clf.score(test['images'], test['labels'])
print('正解率:', score)

