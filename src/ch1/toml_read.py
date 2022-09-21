import toml

# ファイルからデータを読み込む
with open('test.toml', 'r', encoding='utf-8') as fp:
    data = toml.load(fp)

# 読み込んだデータを表示
print('[table] key1=', data['table']['key1'])
print('[table] key2=', data['table']['key2'])
print('[A.B.C] keyA=', data['A']['B']['C']['keyA'])
print('[A.B.D] keyN=', data['A']['B']['D']['keyN'])
