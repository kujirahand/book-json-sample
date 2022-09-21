import json, csv
# JSONを読み込む --- (※1)
with open('zipcode.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)
# CSVを出力 --- (※2)
with open('zipcode.csv', 'w', encoding='cp932') as fp:
    writer = csv.writer(fp)
    writer.writerow(['郵便番号', '住所'])
    for row in data:
        writer.writerow([row['code'], row['addr']])

