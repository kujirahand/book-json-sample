import toml

# TOMLとして保存するデータを辞書型で定義
data = {}
# テーブルにキーを書き込む
data['table'] = {}
data['table']['key1'] = 100
data['table']['key2'] = 'value2'
# 構造化されたデータにキーを書き込む
data['A'] = {}
data['A']['B'] = {}
data['A']['B']['C'] = {}
data['A']['B']['D'] = {}
data['A']['B']['C']['keyA'] = 'valueA'
data['A']['B']['C']['keyB'] = 200
data['A']['B']['D']['keyN'] = 'valueN'
# TOMLに変換してファイルに保存
with open('test.toml', 'w', encoding='utf-8') as fp:
    toml.dump(data, fp)

