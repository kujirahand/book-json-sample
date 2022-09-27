import os, json, struct
SAVE_DIR = './images'
def main():
    # 学習用データ(train)とテスト用データ(test)を順に読む --- (※1)
    for data_type in ['train', 'test']:
        jsonfile = data_type + '-numimage.json'
        # ラベルデータと画像データを読む --- (※2)
        labels = read_idx2(data_type)
        images = read_idx3(data_type)
        # JSON形式で保存 --- (※3)
        print('JSONファイルに保存:', jsonfile)
        with open(jsonfile, 'w', encoding='utf-8') as fp:
            json.dump({'labels': labels, 'images': images}, fp)

# ファイルからデータを4バイト読み整数に変換して返す関数 --- (※4)
def read_i32(fp):
    i = fp.read(4)
    return struct.unpack('>i', i)[0]

# 画像データベース(idx3)を読み込む --- (※5)
def read_idx3(data_type):
    infile = 'qmnist-{}-images-idx3-ubyte.bin'.format(data_type)
    images = []
    with open(os.path.join(SAVE_DIR, infile), 'rb') as fp_image:
        # データベースのヘッダ情報を読む --- (※6)
        magic_number = read_i32(fp_image)
        num_images = read_i32(fp_image)
        size_h, size_w = read_i32(fp_image), read_i32(fp_image)
        size = size_h * size_w
        # 繰り返し画像データ(28x28)を読む --- (※7)
        for i in range(num_images):
            buf = fp_image.read(size)
            idata = struct.unpack('B' * size, buf)
            images.append(idata)
            if i % 5000 == 4999: print(i+1, '枚目を読みました:', data_type)
    return images

# ラベルデータベース(idx2)を読み込む --- (※8)
def read_idx2(data_type):
    infile = 'qmnist-{}-labels-idx2-int.bin'.format(data_type)
    labels = []
    with open(os.path.join(SAVE_DIR, infile), 'rb') as fp:
        # データベースのヘッダ情報を読む --- (※9)
        magic_number = read_i32(fp)
        num_images = read_i32(fp)
        num_cols = read_i32(fp)
        if num_cols != 8:
            print('load error:', in_label_file)
            quit()
        # 繰り返しラベルデータを読む --- (※10)
        for i in range(num_images):
            num_class = read_i32(fp) # 何の数字を表すか --- (※11)
            nist_series = read_i32(fp) # NISTのシリーズ
            w_id, w_idx = read_i32(fp), read_i32(fp) # 書き手を識別する
            nist_code,nist_idx = read_i32(fp), read_i32(fp) # NISTのコード
            dup, unused = read_i32(fp), read_i32(fp) # 未使用領域
            labels.append(num_class) # 必要なラベルデータのみ追加
    return labels

if __name__ == '__main__': main()
