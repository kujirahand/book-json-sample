# リスト型のデータをファイルに保存しようとして失敗している例
a_list = ["バナナ", "マンゴー", "キウイ"]
with open("test.txt", "w", encoding="utf-8") as fp:
    fp.write(a_list)
