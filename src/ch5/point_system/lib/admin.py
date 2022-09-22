import secrets
from flask import request, session, redirect
import html, kudb, urllib, conf
from lib import parts_html
# ----------------------------------------------------------------
# お店(管理者)のログイント処理 --- (※1)
def admin_login_page():
    pw = request.args.get('pw', '')
    if pw != conf.ADMIN_PASSWORD:
        return '管理者パスワードが違います'
    session['admin'] = True # --- (※2)
    return '管理者ログイン成功。会員証のQRLを読み込んでください。'

# ログアウト処理 --- (※3)
def admin_logout_page():
    del session['admin'] # --- (※4)
    return '管理者ログアウトしました'

# 管理者としてログインしているかどうか --- (※5)
def is_admin():
    return 'admin' in session

# ユーザー情報を取得しトークンが正しいかどうか検証 --- (※6)
def get_user(email, token):
    # ユーザー情報をデータベースから得る
    user = kudb.get_one(tag=email)
    if user is None: return None # ユーザーが存在しない
    # トークンを検証する --- (※7)
    token_hash = conf.calc_hash(user['salt'], token)
    if user['token_hash'] != token_hash:
        return None # トークンが間違っている
    return user
# ----------------------------------------------------------------
# お店でお客のQRコードを読み込んだ時のページ --- (※8)
def admin_point_page():
    # お店が管理者としてログインしているか確認 --- (※9)
    if not is_admin(): return '管理者ログインしてください'
    # パラメータの取得 --- (※10)
    p_email = request.args.get('email', '') # メール
    p_token = request.args.get('token', '') # トークン
    # ユーザー情報を取得 --- (※11)
    user = get_user(p_email, p_token)
    if user is None: return '再度会員証を読んでください。'
    # CSRF対策トークンを生成してセッションに保存 --- (※12)
    csrf_token = secrets.token_hex(8)
    session['csrf_token'] = csrf_token
    # ポイント増減フォームを表示 --- (※13)
    return parts_html.show('''
    <h1>{}様(現在{}ポイント)を変更</h1>
    <form action="/admin_point_inc" method="POST">
    <input type="hidden" name="token" value="{}">
    <input type="hidden" name="email" value="{}">
    <input type="hidden" name="csrf_token" value="{}">
    増減額:<input class="input" type="text" name="v" value="10">
    <input type="submit" class="button" value="変更">
    '''.format(
        html.escape(user['name']), user['point'],
        html.escape(p_token), html.escape(p_email), csrf_token))
# ----------------------------------------------------------------
# ポイントの増減処理 --- (※14)
def admin_point_inc_page():
    # お店が管理者としてログインしているか確認 --- (※15)
    if not is_admin(): return '管理者ログインしてください'
    # パラメータの取得 --- (※16)
    p_email = request.form.get('email', '') # メール
    p_token = request.form.get('token', '') # トークン
    p_value = request.form.get('v', '') # ポイント増減値
    p_csrf = request.form.get('csrf_token', '') # CSRF対策用
    # CSRF対策 --- (※17)
    if session.get('csrf_token', '') != p_csrf:
        return '[CSRF対策] 再度会員証を読み込んでください。'
    # ユーザー情報を取得 --- (※18)
    user = get_user(p_email, p_token)
    if user is None: return '再度会員証を読んでください。'
    # ポイントを増減する--- (※19)
    try:
        user['point'] += int(p_value)
        if user['point'] < 0: user['point'] = 0
    except Exception as e:
        return "失敗。数値を入力してください。"
    # データベースに保存
    kudb.update(tag=p_email, new_value=user)
    # ポイント増減フォームに戻る
    return redirect('/admin_point?email={}&token={}'.format(
        urllib.parse.quote(p_email), p_token))
# ----------------------------------------------------------------
# お客一覧の表示 --- (※20)
def admin_users_page():
    # お店が管理者としてログインしているか確認
    if not is_admin(): return '管理者ログインしてください'
    # データベースの値を参照してユーザー一覧を表示
    s = '<h1>お客様一覧</h1>'
    for user in kudb.get_all():
        s += '<div class="box">{} ({}ポイント)</div>'.format(
            html.escape(user['name']),
            user['point'])
    s += '<p><a href="/admin_logout">管理者ログアウト</a></p>'
    return parts_html.show(s)
