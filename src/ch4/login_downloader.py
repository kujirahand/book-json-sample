import requests, os, time, json
import urllib.parse
from bs4 import BeautifulSoup

# 初期設定 --- (※1)
LOGIN_URL = 'https://uta.pw/sakusibbs/users.php?action=login&m=try'
JSON_FILE = 'login_data.json'
# サンプルアカウント --- (※2)
USER_ID = 'JSON-PY'
PASSWORD = 'zR78fGp_zTSlgzLb'
# セッションを開始する --- (※3)
session = requests.session()

def login_to_site():
    # ログイン処理 --- (※4)
    html = session.post(LOGIN_URL, {
        'username_mmlbbs6': USER_ID,
        'password_mmlbbs6': PASSWORD,
    }).text
    time.sleep(1)
    # マイページのURLを得る --- (※5)
    mypage = None
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.select('#header_menu_linkbar > a'):
        if a.text == '★マイページ': mypage = a.attrs['href']
    if mypage is None:
        print('ログインに失敗しました')
        quit()
    # 絶対URLに変換
    mypage = urllib.parse.urljoin(LOGIN_URL, mypage)
    print('mypage=', mypage)
    # マイページを取得 --- (※6)
    html = session.get(mypage).text
    time.sleep(1)
    soup = BeautifulSoup(html, 'html.parser')
    # 作品一覧を取得 --- (※7)
    works = []
    for li in soup.select('#mmlist > li'):
        # 作品ページを取得 --- (※8)
        a = li.find('a')
        link = urllib.parse.urljoin(mypage, a.attrs['href'])
        name = a.text
        print(name, link)
        comments = get_comments(link)
        # 作品を追加 --- (※9)
        works.append({
            'name': name,
            'link': link,
            'comments': comments,
        })
    return works

def get_comments(artwork_url):
    # 作品ページを取得 --- (※10)
    html = session.get(artwork_url).text
    time.sleep(1)
    soup = BeautifulSoup(html, 'html.parser')
    # コメントを取得 --- (※11)
    comments = []
    for div in soup.select('#commentArea .comment'):
        print('comment=', div.text)
        comments.append(div.text)
    return comments

if __name__ == '__main__':
    works = login_to_site()
    # JSONファイルに保存 --- (※12)
    with open(JSON_FILE, 'w', encoding='utf-8') as fp:
        json.dump(works, fp)
