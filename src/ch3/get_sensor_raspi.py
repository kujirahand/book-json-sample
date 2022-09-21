import RPi.GPIO as GPIO
import dht11
import json, time, requests, subprocess

# LAN内にあるサーバーのアドレス --- (※1)
server_url = 'http://192.168.0.103:8889/save'
# GPIOを初期化 --- (※2)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# CPU温度を取得する --- (※ 3)
def get_cpu_temp():
    try:
        proc = subprocess.run(['vcgencmd', 'measure_temp'],
        stdout = subprocess.PIPE)
        s = proc.stdout.decode('utf8')
        s = s.replace("'C", '').strip()
        temp = s.split('=')[1]
        return float(temp)
    except Exception as e:
        print('CPU温度の取得に失敗', e)
        return 0.0

# GPIO14でDHT11の値を読む用に設定 --- (※4)
sensor = dht11.DHT11(pin=14)
while True:
    # DHT11から値を取得 --- (※5)
    v = sensor.read()
    if v.is_valid(): # 成功の場合
        temp = v.temperature
        humi = v.humidity
        # CPU温度の取得
        cpu_temp = get_cpu_temp()
        print('温度:', temp, 'CPU:', cpu_temp, '湿度:', humi)
        # サーバーに値を送信 --- (※6)
        api = '{}?t={}&h={}&c={}'.format(
                server_url, temp, humi, cpu_temp)
        try:
            requests.get(api)
        except:
            print('送信エラー:', api)
        time.sleep(10) # 10秒に1回値を読む
    else: # 失敗の場合
        print("取得エラー: {}".format(v.error_code))
        time.sleep(1)

