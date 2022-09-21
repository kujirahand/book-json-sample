import os, json, japanize_matplotlib
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

def draw_graph(data, pngfile):
    # 線グラフを描画するようにデータを分割 --- (※1)
    x, temp, cpu, humi, xx = [],[],[],[],[]
    l_count = int(len(data) / 3)
    for i, row in enumerate(data):
        t = row['time'].split(' ')[1] # 時間
        t2 = t if (i % l_count == 0) else ''
        x.append(i)
        xx.append(t2)
        temp.append(float(row['temp'])) # 温度
        humi.append(float(row['humi'])) # 湿度
        cpu.append(float(row['cpu'])) # CPU温度
    # グラフ上段を描画 --- (※2)
    fig = plt.figure()
    ay1 = fig.add_subplot(3, 1, 1)
    ay1.plot(x, cpu, label='CPU温度', linewidth=0.7)
    ay1.set_xticks(x)
    ay1.set_xticklabels(xx)
    ay1.legend()
    # グラフ中段を描画 --- (※3)
    ay2 = fig.add_subplot(3, 1, 2)
    ay2.plot(x, temp, label='温度', linewidth=0.7)
    ay2.set_xticks(x)
    ay2.set_xticklabels(xx)
    ay2.legend()
    # グラフ下段を描画 --- (※4)
    ay3 = fig.add_subplot(3, 1, 3)
    ay3.plot(x, humi, label='湿度', linewidth=0.7)
    ay3.set_xticks(x)
    ay3.set_xticklabels(xx)
    ay3.legend()
    plt.savefig(pngfile, dpi=300) # --- (※5)
