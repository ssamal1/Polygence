import pandas as pd
import numpy as np
#from pycorenlp import StanfordCoreNLP
import time
import sqlalchemy
import sqlite3
from itertools import count
from pysal.lib import weights
import esda
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
import libpysal as lps
import numpy as np
import matplotlib.pyplot as plt
# from pysal.esda.mapclassify import K
# from seaborn.palettes import color_palette
from shapely.geometry import Point
import openpyxl
import pymssql
from esda.getisord import G_Local 

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


import plotly.express as px

#Set for identical results
np.random.seed(2021)
#Import Relevant Country Shapefile
poly = gpd.read_file("C:/Users/sansa/Hotspot/Polygence Data/CA_Counties/CA-06-california-counties.json")    

#Repull conflict data (did this so I didn't have to continue to connect ICC vpn)
covid = pd.read_csv("C:/Users/sansa/Hotspot/Polygence Data/Hotspot Dataset - SubrecipientDetailReport (2).csv")

pol = poly[['NAME', 'geometry']]

df  = covid.merge(pol, on='NAME', how='left')

df = gpd.GeoDataFrame(df, geometry='geometry')

w = weights.distance.KNN.from_dataframe(poly, k=5)

lisa = esda.moran.Moran_Local(df['Total Covid Cases'], w)


sig = 1 * (lisa.p_sim < 0.25)
hotspot = 1 * (sig * lisa.q==1)
coldspot = 3 * (sig * lisa.q==3)
doughnut = 2 * (sig * lisa.q==2)
diamond = 4 * (sig * lisa.q==4)


poly = poly.to_crs(epsg=4326)
poly.crs
minx, miny, maxx, maxy = poly.geometry.total_bounds

center_lon=(maxx-minx)/2+minx
center_lon

center_lat=(maxy-miny)/2+miny
center_lat


# map it!
fig = px.choropleth_mapbox(poly, 
                           geojson=poly.geometry, 
                           locations=poly.index, 
                           color='',
                           color_continuous_scale="tropic",
                           mapbox_style="carto-positron",
                           zoom=9, 
                           center = {"lat": center_lat, "lon": center_lon},
                           hover_name=poly.NAME,
                           title='TITLE',
                           opacity=0.5
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()





