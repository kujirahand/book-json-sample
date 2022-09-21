import configparser
# 設定オブジェクトの作成
ini = configparser.ConfigParser()
# 設定を書き込む
ini['section1'] = {}
ini['section1']['key1'] = 'value1'
ini['section1']['key2'] = 'value2'
ini['section2'] = {}
ini['section2']['keyA'] = 'valueA'
ini['section2']['keyB'] = 'valueB'
# ファイルに書き込む
with open('test.ini', 'w', encoding='utf-8') as fp:
    ini.write(fp)
