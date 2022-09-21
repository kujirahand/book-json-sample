import RPi.GPIO as GPIO
import dht11
import json, time, requests

# LAN内にあるサーバーのアドレス --- (※1)
server_url = 'http://192.168.0.103:8787'

# GPIOを初期化 --- (※2)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# GPIO14でDHT11の値を読む --- (※3)
sensor = dht11.DHT11(pin=14)

while True:
    # センサーの値を取得 --- (※4)
    v = sensor.read()
    if v.is_valid(): # 成功の場合
        temp = v.temperature
        humi = v.humidity
        print('温度:{}度/湿度:{}%'.format(temp, humi))
        # サーバーに値を送信 --- (※5)
        api = '{}?t={}&h={}'.format(server_url, temp, humi)
        try:
            requests.get(api)
        except:
            print('送信エラー:', api)
        time.sleep(10) # 10秒に1回値を読む
    else: # 失敗の場合
        print("取得エラー: {}".format(v.error_code))
        time.sleep(1)

