# 会員証ポイントシステム
from flask import Flask
import kudb, conf
from lib import admin, user

# ----------------------------------------------------------------
# Flaskとデータベースを初期化 --- (※1)
app = Flask(__name__)
app.secret_key = conf.SESSION_SECRET # セッションを使うために必要
kudb.connect(conf.DB_PATH)

# ----------------------------------------------------------------
# お客(ユーザー)が使うメソッド一覧 --- (※2)
@app.route('/') # 会員証とポイントを表示する
def index_page(): return user.index_page()

@app.route('/new', methods=['GET', 'POST']) # 新規ユーザーの登録
def new_user_page(): return user.new_user_page()

@app.route('/login', methods=['POST']) # ログイン処理
def login_page(): return user.login_page()

@app.route('/logout') # ログアウト処理
def logout_page(): return user.logout_page()

# ----------------------------------------------------------------
# お店(管理者)が使うメソッドの定義 --- (※3)
@app.route('/admin_login') # お店用ログイン
def admin_login_page(): return admin.admin_login_page()

@app.route('/admin_logout') # お店用ログアウト
def admin_logout_page(): return admin.admin_logout_page()

@app.route('/admin_point') # QRコードを読み込んだ時に表示
def admin_point_page(): return admin.admin_point_page()

@app.route('/admin_point_inc', methods=['POST']) # ポイントを変更
def admin_point_inc_page(): return admin.admin_point_inc_page()

@app.route('/admin_users') # お客の一覧を表示する
def admin_users_page(): return admin.admin_users_page()

# ----------------------------------------------------------------
# サーバー起動 --- (※4)
if __name__ == '__main__':
    app.run('0.0.0.0', conf.PORT_NO, debug=True)
