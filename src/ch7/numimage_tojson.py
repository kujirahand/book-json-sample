import json, struct

SAVE_DIR = './images'

def read_i32(fp):
    i = fp.read(4)
    return struct.unpack('>i', i)[0]

for name in ['train', 'test']:
    # file path
    in_image_file = '{}/{}-images.bin'.format(SAVE_DIR, name)
    in_label_file = '{}/{}-labels.bin'.format(SAVE_DIR, name)
    outfile = '{}/numimage-{}.json'.format(SAVE_DIR, name)
    labels = []
    with open(in_label_file, 'rb') as fp_label:
        magic = read_i32(fp_label)
        num_rows = read_i32(fp_label)
        num_cols = read_i32(fp_label)
        if num_cols != 8:
            print('load error:', in_label_file)
            quit()
        for i in range(num_rows):
            klass = read_i32(fp_label)
            nist_series = read_i32(fp_label)
            writer_id = read_i32(fp_label)
            writer_index = read_i32(fp_label)
            nist_code = read_i32(fp_label)
            global_nist_index = read_i32(fp_label)
            duplicate = read_i32(fp_label)
            unuesed = read_i32(fp_label)

            labels.append(klass) # 必要なデータのみ追加
    images = []
    with open(in_image_file, 'rb') as fp_image:
        magic = read_i32(fp_image)
        num_images = read_i32(fp_image)
        size_h = read_i32(fp_image)
        size_w = read_i32(fp_image)
        size = size_h * size_w
        buf = fp_image.read(size)
        idata = struct.unpack('B' * size, buf)
        images.append(idata)
    # save to json
    print(outfile)
    with open(outfile, 'w', encoding='utf-8') as fp:
        json.dump({'labels': labels, 'data': images}, fp)

