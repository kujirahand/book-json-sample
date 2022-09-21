from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, os, json

# 画像の保存先を指定
SAVE_DIR = './s_images'
if not os.path.exists(SAVE_DIR): os.mkdir(SAVE_DIR)
result = []

# Chromeを起動 --- (※1)
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
# 書道掲示板の一覧ページを開く --- (※2)
driver.get('https://uta.pw/shodou/index.php?master')
time.sleep(1)
# 画像一覧を得る --- (※3)
arts = driver.find_elements(By.CSS_SELECTOR,
    '#recent_list > .article')
for art in arts:
    # img要素を得る --- (※4)
    img = art.find_element(By.CSS_SELECTOR, 'img')
    src = img.get_attribute('src')
    alt = img.get_attribute('alt')
    print(alt, src)
    # 画像が切れるのを防ぐために少しずつスクロールする --- (※5)
    driver.execute_script('window.scrollBy(0,100)')
    # 画像をファイルに保存 --- (※6)
    png_file = os.path.join(SAVE_DIR, os.path.basename(src))
    with open(png_file, 'wb') as fp:
        fp.write(img.screenshot_as_png)
    result.append({
        'title': alt,
        'url': src,
        'file': png_file,
    })
# JSONを保存 --- (※7)
with open('s_images.json', 'w', encoding='utf-8') as fp:
    json.dump(result, fp)

