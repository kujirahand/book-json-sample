from datetime import datetime, timezone, timedelta

# ISO8601の文字列 → dateime --- (※1)
dt_iso8601 = '2022-11-12 13:14:15+09:00'
dt = datetime.fromisoformat(dt_iso8601)
print('ISO→datetime:', dt.strftime('%Y-%m-%d %H:%M:%S'))

# datetime → ISO8601の文字列 --- (※2)
dt = datetime.now()
print('datetime→ISO1:', dt.isoformat()) # タイムゾーンの指定がない

# タイムゾーン付きの現在時刻を出力する --- (※3)
JST = timezone(timedelta(hours=+9), 'JST')
dt = datetime.now(JST)
print('datetime→ISO2:', dt.isoformat())

# strftimeでISO8601の文字列を生成する場合 --- (※4)
print(dt.strftime('%Y-%m-%dT%H:%M:%S%z'))
