import pyqrcode
qrcode = pyqrcode.create('https://kujirahand.com')
qrcode.png('url.png', scale=8)

