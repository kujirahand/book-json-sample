import json, graphviz, sys

def main():
    # JSONファイルの読み込み --- (※1)
    json_file = 'mindmap-idea.json'
    if len(sys.argv) >= 2:
        json_file = sys.argv[1]
    with open(json_file, encoding='utf-8') as fp:
        idea = json.load(fp)
    # グラフを作成 --- (※2)
    g = graphviz.Digraph('idea', engine='fdp',
          format='svg', filename=json_file+'_out')
    #g.attr('node', fontsize="46")
    # ルートから順に描画していく --- (※3)
    draw_obj(g, '', idea, 0)
    g.view()

# 再帰的にノードを描画する関数 --- (※4)
def draw_obj(g, root, node, level):
    # ノードの形状を決定
    shape = 'box'
    if level == 0: shape = 'doublecircle'
    elif level == 1: shape = 'oval'
    # ノードを作成 --- (※5)
    g.node(node['idea'], shape=shape)
    if root != '': g.edge(root, node['idea'])
    # 子ノードがあれば再帰的に描画 --- (※6)
    if 'children' in node:
        for i in node['children']:
            draw_obj(g, node['idea'], i, level + 1)
main()
