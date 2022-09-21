import json
# 楽譜を記述するための変数を宣言
# 音長 --- (※1)
L1 = 480 * 4 # 音長
L2 = int(L1 / 2) # 二分音符
L4 = int(L1 / 4) # 四分音符
L8 = int(L1 / 8) # 八分音符
L16 = int(L1 / 16) # 16分音符
# オクターブ --- (※2)
O3 = 12 * 3
O4 = 12 * 4
O5 = 12 * 5
O6 = 12 * 6
# ノート(ド,ド#,レ,レ#,ミ,ファ,ファ#,ソ,ソ#,ラ,ラ#,シ) --- (※3)
C, Cp, D, Dp, E, F, Fp, G, Gp, A, Ap, B = [i for i in range(12)]
# 楽譜を表すJSONを生成 --- (※4)
data = [
    {'note': O5 + C, 'length': L8},
    {'note': O5 + D, 'length': L8},
    {'note': O5 + E, 'length': L8},
    {'note': O5 + F, 'length': L8},
    {'note': O5 + E, 'length': L8},
    {'note': O5 + D, 'length': L8},
    {'note': O5 + C, 'length': L4},
    {'note': O5 + E, 'length': L8},
    {'note': O5 + F, 'length': L8},
    {'note': O5 + G, 'length': L8},
    {'note': O5 + A, 'length': L8},
    {'note': O5 + G, 'length': L8},
    {'note': O5 + F, 'length': L8},
    {'note': O5 + E, 'length': L4},
]
# 楽譜データをJSONで保存 --- (※5)
with open('kaeru-uta.json', 'w') as fp:
    json.dump(data, fp, indent=2)
print(json.dumps(data))
