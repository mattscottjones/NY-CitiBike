############################# CITI BIKES DASHBOARD #####################################
#########################################################################################

import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from datetime import datetime as dt



############################## INITIAL SETTINGS #########################################
#########################################################################################

st.set_page_config(page_title = 'Citi Bike Strategy Dashboard', layout='wide')
st.title("Citi Bike Strategy Dashboard")
st.markdown("#### This dashboard will help analyze current user behavior and identify expansion opportunities")
st.markdown("_Citi Bike's popularity has increased since its launch in 2013, and during the Covid-19 pandemic, even more New York residents have seen the merit in bike sharing. The higher demand has led to distribution problems (i.e. too few bikes at popular stations, or too many bikes parked at stations making it impossible to return a bike)._")
st.markdown("_We need to diagnose where these distribution issues are most likely to arise, and what the root of the problem may be._")



############################## IMPORT DATA ##############################################
#########################################################################################

folderpath = r'/Users/matthewjones/Documents/CareerFoundry/Data Visualization with Python/Achievement 2/NY-CitiBike/2. Data/Processed Data'

top20 = pd.read_csv(os.path.join(folderpath, 'DB_top20_stations.csv'), index_col = 0)
df_temp = pd.read_csv(os.path.join(folderpath, 'DB_dualaxis_rides_temp.csv'), index_col = 0)



############################## DEFINE THE CHARTS ########################################
#########################################################################################


####################### BAR CHART #######################
st.header("Top 20 Most Popular Citi Bike Stations in New York 2022")
fig = go.Figure(go.Bar(x = top20['start_station_name'],
                       y = top20['value'],
                       marker = {'color' : top20['value'], 'colorscale' : 'blues'}))

fig.update_layout(
    xaxis_title = dict(text = '<b>Start Stations</b>', 
                        font = dict(size = 22)),
    yaxis_title = dict(text = '<b>Total Trips</b>', 
                        font = dict(size = 22)),
    xaxis = dict(tickfont = dict(size=16)),
    yaxis = dict(tickfont = dict(size=16)),
    width = 900, height = 600
)
fig.update_xaxes(
    automargin = True
)
st.plotly_chart(fig, use_container_width = True)


####################### LINE CHART #######################
st.header("Daily Bike Trips and Avergage NYC Temperature in 2022")
line_fig = make_subplots(specs = [[{"secondary_y": True}]])


line_fig.add_trace(
go.Scatter(x = df_temp.index, 
           y = df_temp['bike_rides_daily'], 
           name = 'Daily bike rides',
           marker = {'color': df_temp['bike_rides_daily'],'color': '#2B4B8D'},
           fill = 'tozeroy'),
secondary_y = False
)

line_fig.add_trace(
go.Scatter(x = df_temp.index, 
           y = df_temp['avgTemp'], 
           name = 'Daily temperature',
           marker={'color': df_temp['avgTemp'],'color': '#EB392A'}),
secondary_y = True
)

line_fig.update_layout(
    xaxis_title = '',
    yaxis1_title = dict(text = '<b>Bike Rides Daily</b>', 
                        font = dict(size = 22, color = '#2B4B8D')),
    yaxis2_title = dict(text = '<b>Average Temperature (in C)</b>', 
                        font = dict(size = 22, color = '#EB392A')),
    xaxis = dict(showgrid = False,
                 range = [dt(2022, 1, 1), dt(2023, 1, 1)],
                 tickfont = dict(size=16)),
    yaxis1 = dict(showgrid = False,
                  tickfont = dict(size=14)),
    yaxis2 = dict(showgrid = False,
                  zeroline = False,
                  tickfont = dict(size=14)),
    showlegend = False,
    margin = dict(pad = 10),
    width = 900, height = 500
)

line_fig.update_yaxes(
    automargin = True
)
st.plotly_chart(line_fig, use_container_width=True)


####################### GEOSPATIAL VISUALIZATION #######################
path_to_html = r'/Users/matthewjones/Documents/CareerFoundry/Data Visualization with Python/Achievement 2/NY-CitiBike/4. Visualizations/Citi_Bike_Trips_Aggregated.html'

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Aggregated Bike Trips in New York")
st.components.v1.html(html_data,height=1000)