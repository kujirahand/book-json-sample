from datetime import datetime

# UNIXタイムスタンプ → datetime --- (※1)
timestamp = 1663398895.844902
dt = datetime.fromtimestamp(timestamp)
print(dt.strftime('%Y-%m-%d %H:%M:%S'))

# datetime → UNIXタイムスタンプ --- (※2)
dt = datetime.now() # 現在時刻
timestamp_s = dt.strftime('%s')
print(timestamp_s)

