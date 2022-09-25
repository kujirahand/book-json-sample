import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.inspection import DecisionBoundaryDisplay
import random, json

classifiers = {
    'Nearest Neighbors': KNeighborsClassifier(),
    'Linear SVM': SVC(kernel="linear", C=0.025),
    'RBF SVM': SVC(gamma=2, C=1),
    'Decision Tree': DecisionTreeClassifier(max_depth=5),
    'Random Forest': RandomForestClassifier(),
    'Neural Net': MLPClassifier(alpha=1, max_iter=1000),
    'AdaBoost': AdaBoostClassifier(),
    'Naive Bayes': GaussianNB(),
    'QDA': QuadraticDiscriminantAnalysis()
}


# キノコデータを読み出す --- (※1)
data = json.load(open('mushroom_onehot.json', 'r'))

# 学習データとテストデータに分ける --- (※2)
x_train, x_test, y_train, y_test = train_test_split(
        data['data'], data['labels'], test_size=0.2)

# SVMでデータを学習 --- (※3)
for name, clf in classifiers.items():
    # データを学習
    clf.fit(x_train, y_train)
    # 精度を確認
    score = clf.score(x_test, y_test)
    print('- {}: {}'.format(name, score))
