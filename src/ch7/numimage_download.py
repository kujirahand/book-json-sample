import os, requests
import urllib.request

# 保存ディレクトリを作成 --- (※1)
SAVE_DIR = './images'
if not os.path.exists(SAVE_DIR): os.mkdir(SAVE_DIR)

# データをダウンロード --- (※2)
base = 'https://github.com/facebookresearch/qmnist/raw/main'
for name in ['train', 'test']:
    # 画像データ
    url = base + '/qmnist-{}-images-idx3-ubyte.gz'.format(name)
    save_file = SAVE_DIR + '/{}-images.gz'.format(name)
    print(url)
    urllib.request.urlretrieve(url, save_file)
    # ラベルデータ
    url = base + '/qmnist-{}-labels.tsv.gz'.format(name)
    save_file = SAVE_DIR + '/{}-labels.gz'.format(name)
    print(url)
    urllib.request.urlretrieve(url, save_file)
print('ok')

