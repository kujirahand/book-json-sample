import json, requests, time
server = 'http://localhost:8889/save'
data = json.load(open('sensor.json'))
while True:
    for row in data:
        temp = row['temp']
        humi = row['humi']
        cpu = row['cpu']
        api = "{}?t={}&h={}&c={}".format(server, temp, humi, cpu)
        try:
            requests.get(api)
            print('成功:', api)
        except:
            print('送信失敗:', api)
        time.sleep(10)
