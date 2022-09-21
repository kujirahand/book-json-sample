from datetime import datetime
import pytz

# UTCのdatetimeデータを得る --- (※1)
dt = datetime.now(pytz.UTC)
print(dt.isoformat())

# 日本のタイムゾーンに変換 --- (※2)
dt_jst = dt.astimezone(pytz.timezone('Asia/Tokyo'))
print(dt_jst.isoformat())


