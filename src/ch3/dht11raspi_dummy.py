import json, time, requests
import random

# LAN内にあるサーバーのアドレス --- (※1)
server_url = 'http://192.168.0.103:8787'

# 繰り返しサーバーに送信
while True:
    temp = random.randrange(18, 22)
    humi = random.randrange(30, 40)
    print('温度:{}度/湿度:{}%'.format(temp, humi))
    # サーバーに値を送信 --- (※5)
    api = '{}?t={}&h={}'.format(server_url, temp, humi)
    try:
        requests.get(api)
    except:
        print('送信エラー:', api)
    time.sleep(10) # 10秒に1回値を読む

