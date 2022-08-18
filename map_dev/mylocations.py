import folium
import webbrowser
import os
import json

from folium.map import Popup

m = folium.Map(location=[37.564214, 127.001699],
	tiles="OpenStreetMap",
    zoom_start=15)

folium.Marker(location=[37.564214, 127.001699], icon=folium.Icon(color='red', icon='star')).add_to(m)

with open('./data/seoul_municipalities_geo.json',mode='rt',encoding='utf-8') as f:
    geo = json.loads(f.read())
    f.close()

folium.GeoJson(
    geo,
    name='seoul_municipalities'
).add_to(m)
 
m.save('mylocation.html')

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(os.getcwd() + '/mylocation.html')
