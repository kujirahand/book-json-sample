import glob, gzip, re
SAVE_DIR = './images'

# .gz ファイルを列挙して繰り返す --- (※1)
for infile in glob.glob(SAVE_DIR + '/*.gz'):
    # 保存ファイル名を決定
    outfile = re.sub('\.gz$', '.bin', infile)
    # GZIP形式で圧縮されているファイルを読む --- (※2)
    with gzip.open(infile, 'rb') as fp:
        data = fp.read()
    # 読み込んだデータをファイルへ保存 --- (※3)
    with open(outfile, 'wb') as fp:
        fp.write(data)
print('ok')
