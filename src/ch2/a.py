import json
# JSONデータを文字列としてプログラムに埋め込む --- (※1)
json_str = '''
  {"tokyo": [{"date": "6日(水)", "forecast": "\'\'\'曇"},
    {"date": "7日(木)", "forecast": "晴"}]}
'''
# 埋め込んだJSONをデシリアライズ
data = json.loads(json_str)
# 必要なデータを表示
print(data['tokyo'][0]['date'])
print(data['tokyo'][0]['forecast'])


