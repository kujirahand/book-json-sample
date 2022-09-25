import requests
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data'
r = requests.get(url)
open('mushroom.csv', 'w').write(r.text)

