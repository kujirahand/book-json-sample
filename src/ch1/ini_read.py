import configparser
# 設定オブジェクトの作成
ini = configparser.ConfigParser()
# ファイルから読み込む
ini.read('test.ini', encoding='utf-8')
# 書き込んだ設定を読んで表示
print('[section1] key1=', ini['section1']['key1'])
print('[section1] key2=', ini['section1']['key2'])
print('[section2] keyA=', ini['section2']['keyA'])
