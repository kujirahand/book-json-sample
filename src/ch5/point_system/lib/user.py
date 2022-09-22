from flask import request, session, redirect
import pyqrcode, io, base64, html, secrets, kudb, urllib
import conf
from lib import parts_html
# ----------------------------------------------------------------
# ユーザーの会員証を表示する --- (※1)
def index_page():
    # ログインしていなければログインフォームを表示 --- (※2)
    if 'login' not in session:
        return parts_html.show(parts_html.login_form)
    # ログインしているなら会員証(QRコード)を表示 --- (※3)
    email = session['login']
    user = kudb.get_one(tag=email)
    if user is None: return 'ユーザー情報の取得に失敗'
    # 不正利用対策のためQRコードに毎回異なるトークンを埋め込む --- (※4)
    token = secrets.token_hex(14) # ランダムなトークンを作る
    user['token_hash'] = conf.calc_hash(user['salt'], token)
    url = request.host_url + 'admin_point?email={}&token={}'.format(
        urllib.parse.quote(user['email']), token)
    kudb.update(tag=user['email'], new_value=user) # トークンをDBに保存
    # QRコードをインメモリで作成 --- (※5)
    buf = io.BytesIO()
    pyqrcode.create(url).png(buf, scale=3)
    png = base64.b64encode(buf.getvalue()).decode("ascii")
    # 会員証のHTMLを表示 --- (※6)
    return parts_html.show('''
    <div class="box"><h1>{name} 様 ({point}ポイント)</h1></div>
    <div class="box">会員証:<br>
        <img src="data:image/png;base64,{png}" width="400">
        <p>debug:<br>{url}</p>
        <p><a href="/?r={r}" class="button">情報更新</a></p>
        <p><a href="/logout" class="button">ログアウト</a></p>
    </div>'''.format(
        name=html.escape(user['name']),
        point=user['point'],
        png=png, url=url, r=secrets.token_hex(8)))

# ----------------------------------------------------------------
# ユーザーの新規登録 --- (※7)
def new_user_page():
    # パラメータの取得(POSTメソッド) --- (※8)
    p_name = request.form.get('name', '')
    p_email = request.form.get('email', '')
    p_pw = request.form.get('pw', '')
    if p_name == '' or p_email == '' or p_pw == '':
        # パラメータが指定されていなければ新規登録フォームを表示
        return parts_html.show(parts_html.new_user_form)
    # ユーザー登録を行う --- (※9)
    # ただし過去に同じメールアドレスが登録されていれば失敗 --- (※10)
    users = kudb.find(keys={'email': p_email})
    if len(users) > 0: return '失敗,登録済みのメールアドレスです。'
    # パスワードからハッシュ値を作成 --- (※11)
    salt = secrets.token_hex(16)
    pw_hash = conf.calc_hash(salt, p_pw)
    # データベースに追加 --- (※12)
    kudb.insert({'salt': salt, 'name': p_name, 'email': p_email,
        'pw_hash': pw_hash, 'point': 0}, tag=p_email)
    return redirect('/') # ログインページへリダイレクト

# ----------------------------------------------------------------
# ログイン処理 --- (※13)
def login_page():
    # パラメータを取得(POSTメソッド) --- (※14)
    p_email = request.form.get('email', '')
    p_pw = request.form.get('pw', '')
    # データベースからユーザー情報を取得 --- (※15)
    user = kudb.get_one(tag=p_email)
    if user is None: return 'ログイン失敗'
    # パスワードが合致するか確認 --- (※16)
    check_hash = conf.calc_hash(user['salt'], p_pw)
    if check_hash != user['pw_hash']: return 'ログイン失敗'
    # ログインしていることをセッションに保存 --- (※17)
    session['login'] = p_email
    return redirect('/') # トップページにリダイレクト

# ----------------------------------------------------------------
# ログアウト処理 --- (※18)
def logout_page():
    del session['login']
    return redirect('/')
