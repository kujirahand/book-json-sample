from bs4 import BeautifulSoup

# HTML文字列を指定 --- (※1)
html = '''
<html><body>
  <ul id="a1">
    <li class="name">リンゴ</li>
    <li class="price">710円</li>
  </ul>
  <ul id="a2">
    <li class="name">バナナ</li>
    <li class="price">320円</li>
  </ul>
  <ul id="a3">
    <li class="name">マンゴー</li>
    <li class="price">630円</li>
  </ul>
</body></html>
'''

# BeautifulSoupでHTMLを解析 --- (※2)
soup = BeautifulSoup(html, 'html.parser')

# セレクタで商品の一覧を表示 --- (※3)
print('--- 商品名の一覧を得る ---')
for li in soup.select('ul > li.name'):
    print(li.text)

# セレクタでバナナの値段を調べる --- (※4)
print('---')
price = list(soup.select('#a2 > li.price'))[0]
print("バナナの値段", price.text) # --- (※4a)
price = list(soup.select('ul:nth-child(2) > li.price'))[0]
print('バナナの値段', price.string) # --- (※4b)
prices = list(soup.select('li.price'))
print('バナナの値段', prices[1].text) # --- (※4c)

# selectとfindを組み合わせてマンゴーの値段を調べる --- (※5)
for ul in soup.select('ul'):
    name = ul.find('li', {'class': 'name'}).text
    price = ul.find('li', {'class': 'price'}).text
    if name == 'マンゴー':
        print('マンゴーの値段', price)


