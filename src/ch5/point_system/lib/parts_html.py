# ----------------------------------------------------------------
# 各種HTMLを定義したもの
# ----------------------------------------------------------------
# ログインフォーム --- (※1)
login_form = '''
<h1 class="title">会員ログイン</h1>
<div class="box">
    <form action="/login" method="POST">
        <p>メールアドレス:<br>
        <input class="input" type="text" name="email"></p>
        <p>パスワード:<br>
        <input class="input" type="password" name="pw"></p>
        <p><input class="button" type="submit" value="ログイン"></p>
    </form>
    <a class="button" href="/new">新規登録はこちらへ</a>
</div>
'''
# ----------------------------------------------------------------
# 新規登録フォーム --- (※2)
new_user_form = '''
<h1 class="title">新規会員登録</h1>
 <div class="box">
    <form action="/new" method="POST">
    お名前:<br><input class="input" type="text" name="name"><br>
    メールアドレス:<br><input class="input" type="text" name="email"><br>
    パスワード:<br><input class="input" type="password" name="pw"><br><br>
    <input class="button is-primary" type="submit" value="登録"></form>
    <h2><a class="button" href="/">既に登録済みの方はこちらへ</a></h2></div>
'''
# ----------------------------------------------------------------
# HTMLのヘッダとフッタを定義 --- (※3)
html_frame = '''
<html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
<title>ポイントシステム</title></title><body><div class="content">
<div class="section">{}</div></div></body></html>
'''
# HTMLを表示するのに使う関数 --- (※4)
def show(html):
    return html_frame.format(html)
