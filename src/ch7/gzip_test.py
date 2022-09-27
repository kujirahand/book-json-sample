# GZIPファイルの読み書き方法
import gzip
# サンプルのテキストデータ
sample_text = '\n'.join([
    '愚かな人は一生懸命働いて力尽きる。',
    '町への行き方さえ知らないからだ。',
    '賢い人は強力で，人は知識によって力を増す。'])

# データをGZIPファイルへ圧縮して保存 --- (※1)
with gzip.open('test.txt.gz', 'wb') as fp:
    bin_data = sample_text.encode('utf-8') # bytesにエンコード
    fp.write(bin_data) # 圧縮して書き込み

# 圧縮したファイルを解凍して表示 --- (※2)
with gzip.open('test.txt.gz', 'rb') as fp:
    bin_data = fp.read() # 解凍して読み込み
    print(fp.read().decode('utf-8')) # 文字列にデコード


