import requests, os, time, json
import urllib.parse
from bs4 import BeautifulSoup

# 初期設定 --- (※1)
shodou_url = 'https://uta.pw/shodou/index.php?master'
save_dir = os.path.join(os.path.dirname(__file__), 'images')
logfile = 'images.json'

# 書道掲示板の画像をダウンロード --- (※2)
def download_shodou(target_url):
    # 保存先のディレクトリがなければ作成 --- (※3)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    # HTMLをダウンロード --- (※4)
    html = requests.get(target_url).text
    time.sleep(1) # アクセスしたら待機 --- (※5)
    # HTMLを解析 --- (※6)
    soup = BeautifulSoup(html, 'html.parser')
    # 画像一覧が配置されている要素一覧を取得 --- (※7)
    a_div = soup.select('#contents_body > div')
    if len(a_div) == 0:
        print('[エラー] 要素の取得に失敗')
        return
    images = []
    # 抽出範囲からさらに画像の一覧を抽出 --- (※8)
    for img in a_div[0].find_all('img'):
        # <img src="xxx">のsrcを取得 --- (※9)
        src = img.attrs['src']
        alt = img.attrs['alt']
        # 絶対URLに変換 --- (※10)
        a_url = urllib.parse.urljoin(target_url, src)
        # ファイル名を決めてダウンロード
        fname = os.path.join(save_dir, src.replace('/', '_'))
        download_to_file(a_url, fname)
        # データとして保存
        images.append({'title': alt, 'url': a_url, 'file': fname})
    # 作業内容をログとしてJSONに保存 --- (※11)
    with open(logfile, 'w', encoding='utf-8') as fp:
        json.dump(images, fp)

# 実際に画像をダウンロード --- (※12)
def download_to_file(url, file):
    print('download:', url)
    # コンテンツをダウンロード --- (※13)
    bin = requests.get(url).content
    time.sleep(1) # アクセスしたら待機
    # 画像ファイルへ保存 --- (※14)
    with open(file, 'wb') as fp:
        fp.write(bin)

if __name__ == '__main__':
    download_shodou(shodou_url)

