import RPi.GPIO as GPIO
import json, time

# データファイルの指定 --- (※1)
datafile = "led2.json"
# GPIO番号を指定 --- (※2)
led1 = 14
led2 = 15

# JSONファイルを読み込む --- (※3)
with open(datafile, encoding='utf-8') as fp:
    data = json.load(fp)

# GPIOを初期化 --- (※4)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# GPIOを出力モードに設定 --- (※5)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

while True:
    for i in data:
        # LEDの状態を変更 --- (※6)
        v1 = i['led1']
        v2 = i['led2']
        delay = i['delay']
        GPIO.output(led1, v1)
        GPIO.output(led2, v2)
        # 待機 --- (※7)
        time.sleep(delay)

