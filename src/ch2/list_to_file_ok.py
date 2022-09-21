# リスト型のデータをファイルに保存(成功例)
import json
a_list = ["バナナ", "マンゴー", "キュウイ"]
with open("a_list.json", "w", encoding="utf-8") as fp:
    # リストをJSON文字列に変換
    json_str = json.dumps(a_list, ensure_ascii=False)
    fp.write(json_str)

