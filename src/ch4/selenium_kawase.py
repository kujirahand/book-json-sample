from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, os, json

# 初期設定
JSON_FILE = './kawase.json'
# 取得したい通貨を小文字で指定
CHECKLIST = ['usd', 'eur', 'aud', 'sgd', 'myr', 'php']
WAIT_TIME = 5 # エラーが出るようなら大きな値を指定
result = {}

# Chromeを起動 --- (※1)
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
# 為替情報のログインページを開く --- (※2)
driver.get('https://api.aoikujira.com/kawase/login.php')
time.sleep(WAIT_TIME)
# IDとパスワードを入力 --- (※3)
id = driver.find_element(By.CSS_SELECTOR, '#form input[name=id]')
pw = driver.find_element(By.CSS_SELECTOR, '#form input[name=pw]')
id.clear()
id.send_keys('guest')
pw.clear()
pw.send_keys('0u1eirYwfkuqmRF0')
# 送信ボタンを得てクリック --- (※4)
btn = driver.find_element(By.CSS_SELECTOR, '#form input[type=submit]')
btn.click()
print('--- ログインします ---')
time.sleep(WAIT_TIME)
# 通貨ごとのリンク一覧を取得 --- (※5)
driver.get('https://api.aoikujira.com/kawase/login-info.php')
time.sleep(WAIT_TIME)
curr_dict = {}
for a in driver.find_elements(By.CSS_SELECTOR, '#currlist a'):
    href = a.get_attribute('href')
    text = a.text.lower() # 小文字にする
    curr_dict[text] = href
print('取得可能な通貨の一覧:', curr_dict)
# 必要な通貨のページを巡回 --- (※6)
print('--- 指定通貨を巡回します ---')
for curr in CHECKLIST:
    if curr not in curr_dict:
        print('通貨', curr, 'が一覧に存在しません')
        continue
    # 指定通貨のページを表示 --- (※7)
    try:
        driver.get(curr_dict[curr])
        time.sleep(WAIT_TIME)
        f_rate = driver.find_element(By.ID, 'f_rate')
        result[curr] = float(f_rate.get_attribute('value'))
        print('通貨', curr, '=', result[curr])
    except Exception as e:
        print('通貨', curr, 'でエラー。', e)
# 結果をJSONで保存 --- (※8)
with open(JSON_FILE, 'w', encoding='utf-8') as fp:
    json.dump(result, fp)
print('巡回を終えました。')

