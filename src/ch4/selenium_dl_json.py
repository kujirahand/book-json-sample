from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, os, json

# ブラウザで指定するダウンロードフォルダを以下に指定する★ --- (※1)
if 'USERPROFILE' in os.environ:
    HOME_DIR = os.environ['USERPROFILE'] # Windowsの場合
else:
    HOME_DIR = os.environ['HOME'] # Macの場合
DOWNLOAD_DIR = os.path.join(HOME_DIR, 'Downloads')
# ダウンロードした時のファイル名 --- (※2)
DOWNLOA_FILE = os.path.join(DOWNLOAD_DIR, 'hyakunin.json')
# ダウンロード前に以前ダウンロードしたファイルがあれば削除 --- (※3)
if os.path.exists(DOWNLOA_FILE): os.unlink(DOWNLOA_FILE)
WAIT_TIME = 5

# Chromeを起動 --- (※4)
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
# 百人一首のダウンロードページを開く --- (※5)
driver.get('https://api.aoikujira.com/index.php?hyakunin-data')
time.sleep(WAIT_TIME)
# ダウンロードリンクを探してクリック --- (※6)
for a in driver.find_elements(By.CSS_SELECTOR, '#download-data li a'):
  if a.text == 'JSON形式でダウンロード':
      a.click() # クリックしてダウンロード
      time.sleep(WAIT_TIME)
# ダウンロードしたデータの内容を確認 --- (※7)
rows = json.load(open(DOWNLOA_FILE, 'r', encoding='utf-8'))
for row in rows:
  print(row['kami'], row['simo'])
