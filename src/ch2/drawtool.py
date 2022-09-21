import tkinter as tk, json, os
# 初期設定 --- (※1)
savefile = 'drawtool.json'
is_mouse_down = False # 描画中か判定する
pos = [0, 0] # マウスボタンを押した場所
lines = [] # 描画データ

def main():
    # ウィンドウを作成しキャンバスとボタンを作成 --- (※2)
    global canvas
    app = tk.Tk()
    canvas = tk.Canvas(app, bg='white')
    app.geometry('800x600')
    canvas.pack(fill = tk.BOTH, expand = True)
    button = tk.Button(app, text="初期化", command=clear_draw)
    button.pack()
    # マウスイベントの設定 --- (※3)
    canvas.bind('<Button-1>', mouse_down) # マウスボタンを押した時
    canvas.bind('<ButtonRelease-1>', mouse_up) # 離した時
    canvas.bind('<Motion>', mouse_move) # カーソル動かした時
    load_file()
    draw_screen()
    app.mainloop() # --- (※4)

def load_file(): # JSONを読み込む --- (※5)
    global lines
    if not os.path.exists(savefile): return
    with open(savefile, 'r', encoding='utf-8') as fp:
        lines = json.load(fp)

def save_file(): # 描画データをJSONで保存 --- (※6)
    with open(savefile, 'w', encoding='utf-8') as fp:
        json.dump(lines, fp)

def draw_screen(): # データを元に描画 --- (※7)
    canvas.delete('all')
    for v in lines:
        canvas.create_line(v[0], v[1], v[2], v[3], 
                fill='black', width=10, capstyle="round")

def mouse_down(e): # マウスボタンを押した時 --- (※8)
    global pos, is_mouse_down
    pos = [e.x, e.y]
    is_mouse_down = True

def mouse_up(e): # マウスボタンを離した時 --- (※9)
    global is_mouse_down
    mouse_move(e)
    save_file()
    is_mouse_down = False

def mouse_move(e): # カーソル移動した時 --- (※10)
    global pos
    if not is_mouse_down: return
    lines.append([pos[0], pos[1], e.x, e.y])
    pos = [e.x, e.y]
    draw_screen()

def clear_draw():
    lines.clear()
    draw_screen()
    
if __name__ == '__main__': main()

