import requests, os, time, json
import urllib.parse
from bs4 import BeautifulSoup

# 初期設定 --- (※1)
BBS_URL = 'https://nadesi.com/cgi/bug/index.php'
LOGFILE = 'bbs_logs.json'
MAX_PAGES = 5 # 最大ページ数
logs = [] # 収集済みログデータ保存用
pages = [] # ダウンロード済みページ管理用

# 掲示板にアクセスしてデータを取り出す --- (※2)
def get_logs(target_url):
    # 最大ページ数の確認 --- (※3)
    if len(pages) > MAX_PAGES:
        return # 最大ページ数を超えたなら戻る
    # 二重にページを取得していないかチェック --- (※4)
    if target_url in pages:
        return # 既にダウンロード済みなら戻る
    pages.append(target_url)
    # HTMLをダウンロード --- (※5)
    html = requests.get(target_url).text
    time.sleep(1) # アクセスしたら待機
    # HTMLを解析 --- (※6)
    soup = BeautifulSoup(html, 'html.parser')
    # 掲示板のログデータを抽出 --- (※7)
    for row in soup.select('#body div.thread > table tr'):
        # trの下のtd要素を抽出 --- (※8)
        td_list = list(row.children)
        # ログページのURLを取得 --- (※9)
        a = td_list[0].find('a')
        if a is None: continue
        # ログのURLを絶対URLに変換 --- (※10) 
        href = a.attrs['href']
        href = urllib.parse.urljoin(target_url, href)
        # ログの各種情報を辞書型に入れる --- (※11)
        info = {
            'id': td_list[0].text,
            'title': td_list[1].text,
            'date': td_list[3].text,
            'priority': td_list[4].text,
            'status': td_list[5].text,
            'link': href,
        }
        print(info['id'], info['title'], info['link'])
        logs.append(info) # ログに追加
    # 次へボタンのリンクを求める --- (※12)
    for e in soup.select('.pager > a'):
        if e.text != '次へ→': continue
        link = e.attrs['href']
        # リンクを絶対URLに変換
        link = urllib.parse.urljoin(target_url, link)
        # 再帰的に掲示板の内容をダウンロード --- (※13)
        get_logs(link)

def save_logs():
    # ログの内容をファイルに保存 --- (※14)
    with open(LOGFILE, 'w', encoding='UTF-8') as fp:
        json.dump(logs, fp, ensure_ascii=False)
    print('ログの数:', len(logs))

if __name__ == '__main__':
    get_logs(BBS_URL) # データを取得
    save_logs() # データを保存

