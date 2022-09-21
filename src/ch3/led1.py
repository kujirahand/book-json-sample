import RPi.GPIO as GPIO
import json, time

# 制御するGPIO番号を指定 --- (※1)
gpio_pin = 14

# GPIOの初期化 --- (※2)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# 指定のGPIOピンを出力で使う --- (※3)
GPIO.setup(gpio_pin, GPIO.OUT)

while True:
    GPIO.output(gpio_pin, True) # 点灯 --- (※4)
    time.sleep(1)
    GPIO.output(gpio_pin, False) # 消灯
    time.sleep(1)

