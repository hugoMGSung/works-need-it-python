import json
import folium
from folium.plugins import HeatMap

json_data=open('./data/seoul_submunicipalities_geo.json', encoding='utf-8').read()
data = json.loads(json_data)

json=[]
for i in range(len(data['features'])):
    json.append(data['features'][i]['geometry']['coordinates'])

jsonlat=[]
jsonlng=[]
for i in range(len(json)):
    jsonlat.append(json[i][0])
    jsonlng.append(json[i][1])


m = folium.Map(location=(37.5776087830657, 126.976896737645), zoom_start=14)

heatMap = HeatMap(zip(jsonlng, jsonlat),
                min_opacity=0.1,
                max_val=5,
                radius=10, blur=15,
                max_zoom=5,color='red')

m.add_child(heatMap)
m