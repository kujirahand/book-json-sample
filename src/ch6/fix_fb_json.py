import sys, re

def fix_json(filename):
    # ファイルを開く --- (※1)
    with open(filename, 'r', encoding='utf-8') as fp:
        text = fp.read()
    # 正規表現で\uXXXXの連続部分を抽出 --- (※2)
    text = re.sub(r'(\\u[0-9a-fA-F]{4})+', conv_chars, text)
    print(text)

def conv_chars(m):
    # 正規表現で\uXXXXの部分をバイト配列に追加 --- (※3)
    ch = bytearray(b'')
    for n in re.findall(r'[0-9a-fA-F]+', m.group(0)):
        ch.append(int(n, 16))
    return bytes(ch).decode('utf-8') # 文字列に戻す --- (※4)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('[USAGE] python3 fix_fb_json.py filename')
        quit()
    fix_json(sys.argv[1])

