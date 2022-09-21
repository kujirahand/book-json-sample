import kudb, json

kudb.connect('point.db') # DBに接続
alldata = kudb.get_all() # 全データを得る
print(json.dumps(alldata, ensure_ascii=False, indent=2)) # JSONで出力
