from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chromeを起動 --- (※1)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Googleのページを開く --- (※2)
driver.get('https://google.com')

# スクリーンショットを撮影 --- (※3)
time.sleep(5)
driver.save_screenshot('test.png')
driver.quit() # 終了

