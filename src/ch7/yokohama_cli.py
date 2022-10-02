import joblib, json, sys
from sklearn.ensemble import RandomForestRegressor

def predict(argv):
    # モデルを読み込む --- (※1)
    model = joblib.load('yokohama-kanagawa.model')
    area_list = json.load(open('yokohama-kanagawa-area.json'))
    # パラメータを得る --- (※2)
    m2 = float(argv[0])
    area_s = argv[1]
    station = int(argv[2])
    age = int(argv[3])
    # 地区名を数値に変換 --- (※3)
    area = -1
    for i, s in enumerate(area_list):
        if s == area_s: area = i
    if area == -1:
        print(area_list)
        quit()
    # 予測 --- (※4)
    a = model.predict([[m2, area, station, age]])
    print('予想価格: {:.1f}万円'.format(a[0]/10000))

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('[USAGE] yokohama_cli.py 面積 地区 最寄駅距離 築年数')
        quit()
    predict(sys.argv[1:])
 
