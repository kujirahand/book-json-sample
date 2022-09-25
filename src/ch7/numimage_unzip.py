import gzip

SAVE_DIR = './images'
for name in ['train', 'test']:
    for f in ['images', 'labels']:
        infile = '{}/{}-{}.gz'.format(SAVE_DIR, name, f)
        outfile = '{}/{}-{}.bin'.format(SAVE_DIR, name, f)
        print(outfile)
        with gzip.open(infile, 'rb') as fp:
            data = fp.read()
        with open(outfile, 'wb') as fp:
            fp.write(data)
print('ok')

