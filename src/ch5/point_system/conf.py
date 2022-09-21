import os, hashlib

# プロジェクト全体で使う共通設定 --- (※1)
ROOT_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(ROOT_DIR, 'point.db') # データファイル
PORT_NO = 8888 # サーバーが利用するポート
ADMIN_PASSWORD = 'abcd' # 管理者パスワード
PW_SALT = '2c3rtGl0NH#lIj' # パスワードをハッシュ化するのに利用
SESSION_SECRET = 'YjfV7K8OQ4XzHs00' # セッションの暗号化のため

# SALTを付けて独自のハッシュ値を計算する関数 --- (※2)
def calc_hash(salt, password):
    token = PW_SALT + salt + password
    return hashlib.sha256(token.encode('utf-8')).hexdigest()

