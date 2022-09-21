import tkinter as tk, json, os, sys

def main():
    # 読み込むファイルを調べる --- (※1)
    if len(sys.argv) <= 1:
        print("[USAGE] python3 draw_linerect.py (file)")
        quit()
    filename = sys.argv[1]
    # ウィンドウを作成 --- (※2)
    global canvas
    app = tk.Tk()
    canvas = tk.Canvas(app, bg='white')
    app.geometry('800x600')
    canvas.pack(fill = tk.BOTH, expand = True)
    # データファイルを読む --- (※3)
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)
    # 読み込んだ画像を描画 --- (※4)
    draw_screen(data)
    app.mainloop()

def draw_screen(data): 
    # データを元に描画 --- (※5)
    for v in data:
        # 直線か --- (※6)
        if v['type'] == 'line':
            xy = v['xy']
            canvas.create_line(xy[0], xy[1], xy[2], xy[3], 
                fill=v['color'], width=v['width'], capstyle='round')
        # 長方形(矩形)か --- (※7)
        if v['type'] == 'rect':
            xy = v['xy']
            canvas.create_rectangle(xy[0], xy[1], xy[2], xy[3],
                fill=v['fill'], width=v['width'], 
                outline=v['border'])

if __name__ == '__main__': main()
