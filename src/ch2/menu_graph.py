import json, graphviz
# JSONデータを読み込む --- (※1)
with open('excel-menu-norm.json', encoding='utf-8') as fp:
    menu_data = json.load(fp)
# グラフを作成 --- (※2)
g = graphviz.Digraph('G', format='svg', filename='menu_graph')
g.attr(rankdir='LR')
g.attr('node', shape='record')
g.node('メニュー')
mtype_dic = {}
# メニューを一つずつ追加していく --- (※3)
for menu in menu_data:
    # 「本日のお勧め」か「通常」を指定
    if menu['mtype'] not in mtype_dic:
         mtype_dic[menu['mtype']] = True
         g.edge('メニュー', menu['mtype'])
    # メニューを追加
    g.edge(menu['mtype'], menu['name'])
    g.edge(menu['name'], str(menu['price']) + "円")
g.view()
