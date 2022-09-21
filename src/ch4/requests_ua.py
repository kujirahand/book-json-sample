import requests
# User-Agentを指定
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# ヘッダを指定してアクセス
header = { 'User-Agent': ua }
response = requests.get('https://api.aoikujira.com/ip/ini', headers=header)
print(response.text)
