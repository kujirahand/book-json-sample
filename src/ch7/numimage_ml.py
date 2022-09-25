from sklearn import svm
import json

with open('images/train-numimage.json', 'r') as fp:
    train = json.load(fp)

clf = svm.SVC()
clf.fit(train['data'], train['labels'])

with open('images/test-numimage.json', 'r') as fp:
    test = json.load(fp)
score = clf.score(test['data'], test['labels'])
print('正解率:', score)


