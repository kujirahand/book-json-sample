import numpy as np
import matplotlib.pyplot as plt
# NumPyで連続した値を生成してsinの値を計算
x = np.arange(0, 30, 0.1) 
y = np.sin(x) 
# グラフを描画
plt.plot(x, y) 
