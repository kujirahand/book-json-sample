import time, requests
URL_JSON = 'https://api.aoikujira.com/kawase/login-download.php?format=json'
# リクエストで通貨一覧をダウンロードしようとするが...
json_str = requests.get(URL_JSON).text
print('download=', json_str)
