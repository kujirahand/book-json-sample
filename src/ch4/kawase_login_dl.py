from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, os, json, requests
# 初期設定
WAIT_TIME = 5
URL_LOGIN = 'https://api.aoikujira.com/kawase/login.php'
URL_JSON = 'https://api.aoikujira.com/kawase/login-download.php?format=json'
# Chromeを起動
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
# 為替情報のログインページを開く --- (※1)
driver.get(URL_LOGIN); time.sleep(WAIT_TIME)
# IDとパスワードを入力してログイン
id = driver.find_element(By.CSS_SELECTOR, '#form input[name=id]')
pw = driver.find_element(By.CSS_SELECTOR, '#form input[name=pw]')
id.clear(); id.send_keys('guest')
pw.clear(); pw.send_keys('0u1eirYwfkuqmRF0')
btn = driver.find_element(By.CSS_SELECTOR, '#form input[type=submit]')
btn.click()
time.sleep(WAIT_TIME)
# ブラウザのCookie一覧を変数に書き出す --- (※2)
cookies = { c['name']: c['value'] for c in driver.get_cookies() }
# リクエストで通貨一覧をダウンロード --- (※3)
json_str = requests.get(URL_JSON, cookies=cookies).text
print('download=', json_str)
# ファイルに保存 --- (※4)
with open('kawase_all.json', 'w', encoding='utf-8') as fp:
    fp.write(json_str)
