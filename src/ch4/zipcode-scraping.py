import requests, time, json
from bs4 import BeautifulSoup
import urllib.parse

# 初期設定 --- (※1)
datafile = './zipcode.json'
ken = '東京都'
shi = '目黒区'
target_url = 'https://{}?m=shi&ken={}&shi={}'.format(
    'api.aoikujira.com/zip/list.php',
    urllib.parse.quote(ken),
    urllib.parse.quote(shi),
)

# HTMLファイルをダウンロード --- (※2)
html = requests.get(target_url).text
time.sleep(1) # アクセスしたら待機 --- (※3)
# HTMLを解析 --- (※4)
soup = BeautifulSoup(html, 'html.parser')
# 郵便番号と住所が記述された要素を取得 --- (※5)
tr_list = soup.select('#ziplist tr')
if len(tr_list) == 0:
    print('[エラー] 要素の取得に失敗')
    quit()
result = []
# テーブルの各行を取得 --- (※6)
for tr in tr_list:
    children = list(tr.children) # 子要素を取得 --- (※7)
    code = children[0].text
    addr = children[1].text
    print(code, addr)
    # ヘッダ行なら飛ばす --- (※8)
    if code == '郵便番号': continue
    result.append({'code': code, 'addr': addr})
# ファイルへ保存 --- (※9)
with open(datafile, 'w') as fp:
    json.dump(result, fp)

