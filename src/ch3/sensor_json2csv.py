import json
# JSONを読む
data = json.load(open('sensor.json', encoding='utf-8'))
# CSVとして出力
print("Time,Temperature,Humidity,CPU")
for r in data:
    print("{},{},{},{}".format(
        r['time'], r['temp'], r['humi'], r['cpu']))

