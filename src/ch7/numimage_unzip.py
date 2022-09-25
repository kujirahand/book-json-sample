import gzip

SAVE_DIR = './images'
for name in ['train', 'test']:
    # images
    infile = '{}/{}-images.gz'.format(SAVE_DIR, name)
    outfile = '{}/{}-images'.format(SAVE_DIR, name)
    with gzip.open(infile, 'rb') as fp:
        data = fp.read()
    with open(outfile, 'wb') as fp:
        fp.write(data)
    # labels
    infile = '{}/{}-labels.gz'.format(SAVE_DIR, name)
    outfile = '{}/{}-labels.tsv'.format(SAVE_DIR, name)
    with gzip.open(infile, 'rb') as fp:
        data = fp.read()
    with open(outfile, 'wb') as fp:
        fp.write(data)
print('ok')

