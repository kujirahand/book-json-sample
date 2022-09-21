import json, graphviz, sys
# JSONデータを読み込む --- (※1)
json_file = 'family-tokugawa.json'
# 引数があれば、読むファイルを変更する
if len(sys.argv) >= 2:
    json_file = sys.argv[1]
with open(json_file, encoding='utf-8') as fp:
    family = json.load(fp)
# Graphvizでグラフを作成 --- (※2)
g = graphviz.Graph('family', format='svg', filename=json_file+'_s')
# 一世代ずつノードをつなげる --- (※3)
for f in family:
    # 親の処理 --- (※4)
    fa = f['parents'][0]
    mo = f['parents'][1] if len(f['parents']) >= 2 else ''
    fa_mo = fa + '_' + mo # 父と母の接続ポイント
    # 「父 → 接続ポイント → 母」のノードを作る --- (※5)
    g.node(fa, style='filled', fillcolor='#f0f0ff', shape="box")
    g.node(fa_mo, shape='point')
    g.edge(fa, fa_mo, '夫', dir='none')
    if mo != '': # 母が明らかであれば父とつなげる
        g.node(mo, style='filled', fillcolor='#fff0e0')
        g.edge(fa_mo, mo, '妻', dir='none')
    if len(f['children']) > 0:
        # 子供たちの処理 --- (※7)
        for child in f['children']:
            g.node(child, style='filled', fillcolor='#f0f0ff', shape="box")
            g.edge(fa_mo, child, '子', dir='forward')
# 出力と表示
g.view()
