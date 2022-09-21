import requests, time
# ページを指定
SET_API = 'https://api.aoikujira.com/session_test/set-data.php'
GET_API = 'https://api.aoikujira.com/session_test/get-data.php'

print('=== セッションなし ===') # --- (※1)
# set-dataのページにアクセス
print(requests.get(SET_API + '?data=12345').text.strip())
time.sleep(1)
# get-dataのページにアクセス
print(requests.get(GET_API).text)
time.sleep(1)

print('=== セッション利用 ===') # --- (※2)
# セッションを開始する
session = requests.session()
# set-dataのページにアクセス
print(session.get(SET_API + '?data=12345').text.strip())
time.sleep(1)
# get-dataのページにアクセス
print(session.get(GET_API).text)
time.sleep(1)

