import kudb

# データベースに接続
kudb.connect('test.db')
# 既存のデータを全部クリア
kudb.clear()

# データの一括挿入 --- (※1)
kudb.insert_many([
    {"name": "マンゴー", "price": 660},
    {"name": "バナナ", "price": 320},
    {"name": "パイナップル", "price": 830},
    {"name": "ココナッツ", "price": 450},
])

# 最後に挿入した2件を取り出して表示 --- (※2)
for row in kudb.recent(2):
    print('recent =>', row)

# 「バナナ」を検索して表示 --- (※3)
for row in kudb.find(keys={"name": "バナナ"}):
    print('バナナ =>', row)

# idを指定してデータを削除 --- (※4)
kudb.delete(id=1) # マンゴーを削除

# データを指定して削除 --- (※5)
kudb.delete(doc_keys={"name": "バナナ"}) # バナナを削除

# 残りのデータ数を表示 --- (※6)
print("残り=", kudb.count_doc(), "件")

# データの更新 --- (※7)
kudb.update(id=3, new_value={
    "name": "パイナップル", "price": 600})
print('id=3 =>', kudb.get(id=3))

