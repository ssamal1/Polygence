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
#from pysal.esda.mapclassify import K
# from seaborn.palettes import color_palette
from shapely.geometry import Point
import openpyxl
import pymssql

import plotly.express as px
import geopandas as gpd
import plotly.figure_factory as ff

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc




#Set for identical results
np.random.seed(2021)
#Import Relevant Country Shapefile
poly = gpd.read_file('C:/Users/sansa/Hotspot/Polygence Data/CA_Counties/CA_Counties_TIGER2016.shp') 

#Repull conflict data (did this so I didn't have to continue to connect ICC vpn)
covid = pd.read_csv("C:/Users/sansa/Hotspot/Polygence Data/Hotspot Dataset - SubrecipientDetailReport (2).csv")


poly = poly[['NAME', 'geometry']]
poly.head





df  = covid.merge(poly, on='NAME', how='left')
df = gpd.GeoDataFrame(df, geometry='geometry')






w = weights.distance.KNN.from_dataframe(poly, k=5)


lisa = esda.moran.Moran_Local(df['Total Covid Cases'], w)


sig = 1 * (lisa.p_sim < 0.25)
hotspot = 1 * (sig * lisa.q==1)
coldspot = 3 * (sig * lisa.q==3)
doughnut = 2 * (sig * lisa.q==2)
diamond = 4 * (sig * lisa.q==4)
spots = hotspot + coldspot + doughnut + diamond


spot_labels = [ '0 ns', '1 hot spot', '2 doughnut', '3 cold spot', '4 diamond']
labels = [spot_labels[i] for i in spots]

values = covid['Total Covid Cases'].tolist()
fips = covid['FIPS'].tolist()

colorscale = [
    'rgb(193, 193, 193)',
    'rgb(239,239,239)',
    'rgb(195, 196, 222)',
    'rgb(144,148,194)',
    'rgb(255,0,0)',
    'rgb(255, 0, 0)'
]

from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Covid 19 Hotspot Analysis'),
    html.P("Select a candidate:"),
    dcc.RadioItems(
        id='candidate', 
        options=["Total", "May/Jun 2020", "Jul/Aug 2020", "Sep/Oct 2020"],
        value="Ttal",
        inline=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("candidate", "value"))
def display_choropleth(candidate):
    df = covid # replace with your own data source
    geojson = poly
    fig = px.choropleth(
        df, geojson=geojson, color=candidate,
        locations="Total Covid Cases", featureidkey="properties.district",
        projection="mercator", range_color=[0, 6500])
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig


app.run_server(debug=True)





'''


fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA'],
    binning_endpoints=[14348, 63983, 134827, 426762, 2081313], colorscale=colorscale,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='Covid Hotspots', title='California Covid Hotspot'
)
fig.layout.template = None
fig.show()


'''