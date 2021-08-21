import folium
from socket import socket
import pandas as pd



map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles ="Stamen Terrain")
v = pd.read_csv("Volcanoes_USA.txt")

### Load data from Vulcanoes.txt
lat = list(v["LAT"])
lon = list(v["LON"])
elev = list(v["ELEV"])
name = list(v["NAME"])


def get_elevation_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 2000:
        return 'orange'
    else:
        return 'red'


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

### Creating Feature Group

fg = folium.FeatureGroup(name=["My Map"])

for lt, ln, el, name in zip(lat,lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=get_elevation_color(el))))

map.add_child(fg)

map.save("Map1.html")