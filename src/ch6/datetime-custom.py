from datetime import datetime

# 独自の日時文字列 → dateime --- (※1)
dt_custom = 'Fri Jun 22 01:22:24 +0000 2022'
dt = datetime.strptime(dt_custom, '%a %b %d %H:%M:%S %z %Y')
print('独自→datetime:', dt.strftime('%Y-%m-%d %H:%M:%S'))

# dateime → 独自日時文字列
print('dateitme→独自', dt.strftime('%a %b %d %H:%M:%S %z %Y'))
