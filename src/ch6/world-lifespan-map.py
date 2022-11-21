import json, folium, geopandas
import matplotlib.pyplot as plt

# 地理データを読む --- (※1)
countries = geopandas.read_file('world.geo.json/countries.geo.json')

# JSONを読む --- (※2)
with open('world-lifespan.json', 'r', encoding='utf-8') as fp:
  data = json.load(fp)

# データを色に変換する --- (※3)
max_val = max([v for k,v in data.items()])
min_val = min([v for k,v in data.items()])
cmap = plt.get_cmap('coolwarm')
norm = plt.Normalize(vmin=min_val, vmax=max_val)
coldata, agedata = {}, {}
for cn, age in data.items():
    # 韓国とロシアの国名が地理データとマッチしないので微修正 --- (※3a)
    if cn == 'Republic of Korea': cn = 'South Korea'
    if cn == 'Russian Federation': cn = 'Russia'
    coldata[cn] = '#' + bytes(cmap(norm(age), bytes=True)[:3]).hex()
    agedata[cn] = age # 国名の変更のため

# 地図の色をコールバック関数で指定する --- (※4)
def get_style(o):
  name = o['properties']['name']
  if name not in coldata: return {}
  return {'fillColor': coldata[name], 'weight': 1, 
          'fillOpacity': 0.5, 'color': 'silver'}

# 地図を表示する準備 --- (※5)
map = folium.Map(location=[0, 0], zoom_start=2)

# 地図上にデータを描画するように指定 --- (※6)
for cn, age in coldata.items():
  gis = countries[countries['name'] == cn]
  if len(gis) == 0: continue
  folium.GeoJson(gis, style_function=get_style,
    tooltip='{} {}才'.format(cn, agedata[cn])).add_to(map)

# HTMLで出力 --- (※7)
map.save('world-lifespan.html')
# Colabで画面にマップを出力
map
