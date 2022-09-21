import json, graphviz, sys

# JSONデータを読み込む --- (※1)
json_file = 'family-tokugawa.json'
if len(sys.argv) >= 2:
    json_file = sys.argv[1]
with open(json_file, encoding='utf-8') as fp:
    family = json.load(fp)

# グラフを作成 --- (※2)
g = graphviz.Graph('family', format='svg', filename=json_file+'_out')
g.attr('node', shape='box', dir='none')
g.attr(rankdir='TB') # 上下に並べる

# 一世代ずつノードをつなげる --- (※3)
for f in family:
    # 親の処理 --- (※4)
    g.attr(rankdir='TB')
    fa = f['parents'][0]
    mo = f['parents'][1] if len(f['parents']) >= 2 else '☆'
    pp = fa + '_' + mo
    with g.subgraph() as sg:
        sg.graph_attr['rank'] = 'same'
        # 「父 → 接続ポイント → 母」のノードを作る --- (※5)
        sg.node(fa, style='filled', fillcolor='#f0f0ff')
        sg.node(mo, style='filled', fillcolor='#fff0f0')
        sg.node(pp, shape='point')
        sg.edge(fa, pp, dir='none')
        sg.edge(pp, mo, dir='none')
    # 子と親をつなげる接続ポイントの処理 --- (※6)
    if len(f['children']) > 0:
        pc = pp + '_pc'
        g.node(pc, shape='point')
        g.edge(pp, pc, dir='none')
        # 子供たちの処理 --- (※7)
        for c in f['children']:
            g.node(c)
            g.edge(pc, c, dir='none')

# 出力と表示 -- (※8)
g.view()
