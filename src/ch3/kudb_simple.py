import kudb
# データベースに接続 --- (※1)
kudb.connect('test.db')

# データを挿入 --- (※2)
kudb.insert({"name": "マンゴー", "price": 660})
kudb.insert({"name": "バナナ", "price": 320})
kudb.insert({"name": "パイナップル", "price": 830})
kudb.insert({"name": "ココナッツ", "price": 450})

# データを全部取り出して順に表示 --- (※3)
print("--- 全部抽出 ---")
for row in kudb.get_all():
    print(row["name"], row["price"], "円")

# データベースを閉じる --- (※4)
kudb.close()

