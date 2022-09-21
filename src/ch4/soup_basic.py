from bs4 import BeautifulSoup

# HTML文字列を指定 --- (※1)
html = '''
<html><body><h1>Link</h1>
<ul>
  <li><a href="https://sakuramml.com/">Sakura</a></li>
  <li><a href="https://nadesi.com/">Nadesiko</a></li>
</ul>
</body></html>
'''

# BeautifulSoupでHTMLを解析 --- (※2)
soup = BeautifulSoup(html, 'html.parser')

# <li>タグのテキストを抽出する --- (※3)
print('--- <li> ---')
for li in soup.find_all('li'):
    print(li.text)

# <a>タグからリンクの一覧抽出する --- (※4)
print('--- <a> href ---')
for a in soup.find_all('a'):
        print(a.attrs['href'])

