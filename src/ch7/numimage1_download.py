import os, requests

# 保存ディレクトリを作成 --- (※1)
SAVE_DIR = './images'
if not os.path.exists(SAVE_DIR): os.mkdir(SAVE_DIR)

# データをダウンロードする関数 --- (※2)
def download(url, save_path):
    if not os.path.exists(save_path):
        open(save_path, 'wb').write(requests.get(url).content)

# URLとファイルの一覧 --- (※3)
baseurl = 'https://github.com/facebookresearch/qmnist/raw/main/'
files = [
  'qmnist-train-images-idx3-ubyte.gz',
  'qmnist-train-labels-idx2-int.gz',
  'qmnist-test-images-idx3-ubyte.gz',
  'qmnist-test-labels-idx2-int.gz'
]
# データをダウンロード --- (※4)
for fname in files:
    url = baseurl + fname
    save_file = os.path.join(SAVE_DIR, fname)
    print(url)
    download(url, save_file)
print('ok.')
