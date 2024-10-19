############################# CITI BIKES DASHABOARD #####################################
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

st.set_page_config(page_title = 'Citi Bikes Strategy Dashboard', layout='wide')
st.title("Citi Bikes Strategy Dashboard")
st.markdown("The dashboard will help with the expansion problems Citi Bikes currently faces")
st.markdown("Right now, Citi Bikes runs into a situation where customers complain about bikes not being avaibale at certain times. This analysis aims to look at the potential reasons behind this.")



############################## IMPORT DATA ##############################################
#########################################################################################

folderpath = r'/Users/matthewjones/Documents/CareerFoundry/Data Visualization with Python/Achievement 2/NY-CitiBike/2. Data/Processed Data'

# df = pd.read_csv(os.path.join(folderpath, 'DB_reduced_bike_weather_data.csv'), index_col = 0, sep=', ')
top20 = pd.read_csv(os.path.join(folderpath, 'DB_top20_stations.csv'), index_col = 0)
df_temp = pd.read_csv(os.path.join(folderpath, 'DB_dualaxis_rides_temp.csv'), index_col = 0)



############################## DEFINE THE CHARTS ########################################
#########################################################################################


####################### BAR CHART #######################
fig = go.Figure(go.Bar(x = top20['start_station_name'],
                       y = top20['value'],
                       marker = {'color' : top20['value'], 'colorscale' : 'blues'}))

fig.update_layout(
    title = '<b>Top 20 Most Popular Citi Bike Stations in New York 2022</b>',
    xaxis_title = '<b>Start Stations</b>',
    yaxis_title ='<b>Total Trips</b>',
    width = 900, height = 600
)
fig.update_xaxes(
    automargin = True
)
st.plotly_chart(fig, use_container_width = True)


####################### LINE CHART #######################
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
    title = dict(text = '<b>Daily Bike Trips and Avergage NYC Temperature in 2022</b>',
                 font = dict(size = 18)),
    xaxis_title = '',
    yaxis1_title = dict(text = '<b>Bike Rides Daily</b>', 
                        font = dict(size = 14, color = '#2B4B8D')),
    yaxis2_title = dict(text = '<b>Average Temperature (in C)</b>', 
                        font = dict(size = 14, color = '#EB392A')),
    xaxis = dict(showgrid = False,
                 range = [dt(2022, 1, 1), dt(2023, 1, 1)]),
    yaxis1 = dict(showgrid = False),
    yaxis2 = dict(showgrid = False,
                  zeroline = False),
    showlegend = False,
    margin = dict(pad = 10),
    width = 900, height = 500
)

line_fig.update_yaxes(
    automargin = True
)
st.plotly_chart(line_fig, use_container_width=True)


####################### GEOSPATIAL VISUALIZATION #######################
# path_to_html = "Divvy Bike Trips Aggregated.html" 

# # Read file and keep in variable
# with open(path_to_html,'r') as f: 
#     html_data = f.read()

# ## Show in webpage
# st.header("Aggregated Bike Trips in Chicago")
# st.components.v1.html(html_data,height=1000)