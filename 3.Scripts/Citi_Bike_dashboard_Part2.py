############################# CITI BIKES DASHBOARD #####################################
#########################################################################################

import streamlit as st
import streamlit.components.v1 as components
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
from numerize.numerize import numerize
from PIL import Image
from IPython.core.display import display, HTML



############################## INITIAL SETTINGS #########################################
#########################################################################################

st.set_page_config(page_title = 'Citi Bike Strategy Dashboard', layout='wide')
st.html(
    "<h1><font color='#3881B5'>Citi Bikes</font> in New York City 2022 - <br>Exploring Current User Behavior <br>and Expansion Opportunities</h1>")

## Define side bar
st.sidebar.title('Navigator')
page = st.sidebar.selectbox('Select an aspect of the analysis',
  ['Intro Page',
   'Seasonality of Bike Usage',
   'Most Popular Stations',
   'Map of Aggregated Bike Trips', 
   'Recommendations'])

## Theme colors
colors = ['#2B4B8D', '#3881B5']
accent = '#EB392A'



################################## IMPORT DATA ##########################################
#########################################################################################

folderpath = r'/Users/matthewjones/Documents/CareerFoundry/Data Visualization with Python/Achievement 2/NY-CitiBike/2.Data/Processed_Data'

picturepath = r'/Users/matthewjones/Documents/CareerFoundry/Data Visualization with Python/Achievement 2/NY-CitiBike/4.Visualizations/Dashboard_Images'

htmlpath = r'/Users/matthewjones/Documents/CareerFoundry/Data Visualization with Python/Achievement 2/NY-CitiBike/4.Visualizations/Citi_Bike_Trips_Aggregated.html'

line_chart_data = pd.read_csv(os.path.join(folderpath, 'DB_line_chart_data.csv'), index_col = 0)
bar_chart_start = pd.read_csv(os.path.join(folderpath, 'DB_bar_chart_start.csv'), index_col = 0)
bar_chart_end = pd.read_csv(os.path.join(folderpath, 'DB_bar_chart_end.csv'), index_col = 0)
expensive = pd.read_csv(os.path.join(folderpath, 'data-16QWY.csv'))
pie_payment_data = pd.read_csv(os.path.join(folderpath, 'DB_pie_payment.csv'))
hist_duration_data = pd.read_csv(os.path.join(folderpath, 'DB_hist_duration.csv'), index_col = 0)



################################### INTRO PAGE ##########################################
#########################################################################################

if page == 'Intro Page':
    
    st.html(
        "<h5 style = 'width:75%;'><em>Citi Bike's popularity has increased since its launch in 2013, and during the Covid-19 pandemic, even more New York residents have seen the merit in bike sharing. The higher demand has led to distribution problems (i.e. too few bikes at popular stations, or too many bikes parked at stations making it impossible to return a bike). This application will diagnose where these distribution issues are most likely to arise, and theorize what the root of the problem may be.</em></h5>")

    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander('Weather Component and Bike Usage'):
            st.write(
                '''Is there a seasonal demand?''')
            st.write(
                '''Which bike types (Classic or Electric) are preferred when?''')
        with st.expander('Most Popular Stations'):
            st.write(
                '''Which stations are the most popular starting destinations?''')
            st.write(
                '''Which stations are the most popular ending destinations?''')
            st.write(
                '''Is there a difference between the two? If so, what does this say about user demand?''')
            st.write(
                '''Do users prefer different bike types at different stations?''')
        with st.expander('Interactive Map with Aggregated Bike Trips'):
            st.write(
                '''Where are the top 20 starting stations located?''')
            st.write(
                '''What are the most common routes?''')
        with st.expander('Recommendations'):
            st.write(
                '''Where are we most likely to see distribution issues?''')
            st.write(
                '''What is causing these issues?''')
            st.write(
                '''What can we do to mitigate any possible issues in the future?''')
        st.text("")
        st.html(
            "<h5 align='center'>To see more about these different aspects of the analysis, click on the drop down menu in the left sidebar</h5>")

    with col2:
        myImage = Image.open(os.path.join(picturepath, 'citibike_rental.jpg')) 
        #source: https://www.freepik.com/free-photo/girl-renting-city-bike-from-bike-stand_3626171.htm#fromView=search&page=1&position=34&uuid=a74d8363-c509-453b-a25e-3058501c3b9c
        st.image(myImage)



############################# WEATHER COMPONENT AND BIKE USAGE ##########################
#########################################################################################

elif page == 'Seasonality of Bike Usage':

    st.html(
        "<h2 align='center'>Daily Bike Trips and Avergage NYC Temperature</h2>"
    )
    st.html(
        "<h5 align='center'><em>Here comes the sun!</em></h5>"
    )
   
    ####################### LINE CHART #######################
    line_fig = make_subplots(specs = [[{"secondary_y": True}]])

    ## Electric bike rides area chart
    line_fig.add_trace(go.Scatter(x = line_chart_data['Date'], 
                                  y = line_chart_data['Daily Rides'], 
                                  fill = 'tozeroy', #fill down to xaxis
                                  fillcolor = 'rgba(56, 129, 181, 0.8)',
                                  mode = 'lines',
                                  line = {'color': '#3881B5'},
                                  name = 'Electric Bikes'),
                        secondary_y = False)

    ## Classic bike rides area chart
    line_fig.add_trace(go.Scatter(x = line_chart_data['Date'], 
                                  y = line_chart_data['Daily Classic Rides'], 
                                  fill = 'tozeroy', #fill down to xaxis
                                  fillcolor = 'rgba(43, 75, 141, 0.8)',
                                  mode = 'lines',
                                  line = {'color': '#2B4B8D'},
                                  name = 'Classic Bikes'),
                       secondary_y = False)

    ## Average temperature line chart
    line_fig.add_trace(
    go.Scatter(x = line_chart_data['Date'], 
               y = line_chart_data['Average Temperature'], 
               name = '',
               showlegend = False,
               marker={'color': line_chart_data['Average Temperature'],'color': accent}),
    secondary_y = True
    )

    ## Formatting axes and titles
    line_fig.update_layout(
        xaxis_title = '',
        yaxis1_title = dict(text = '<b>Bike Rides Daily</b>', 
                            font = dict(size = 22, color = '#2B4B8D')),
        yaxis2_title = dict(text = '<b>Average Temperature (in C)</b>', 
                            font = dict(size = 22, color = accent)),
        xaxis = dict(showgrid = False,
                     range = [dt(2022, 1, 1), dt(2023, 1, 1)],
                     tickfont = dict(size = 16, color = '#2B4B8D')),
        yaxis1 = dict(showgrid = False,
                      tickfont = dict(size = 14, color = '#2B4B8D'),
                      color = '#323232'),
        yaxis2 = dict(showgrid = False,
                      zeroline = False,
                      tickfont = dict(size = 14, color = '#2B4B8D'),
                      color = '#323232'),
        showlegend = True,
        legend = dict(yanchor = 'top',
                      y = 0.95,
                      xanchor = 'left',
                      x = 0.05,
                      font = dict(size = 16)
                     ),
        margin = dict(pad = 10),
        width = 900, height = 500
    )

    line_fig.update_yaxes(
        automargin = True
    )
    
    st.plotly_chart(line_fig, use_container_width=True)

    ####################### ANALYSIS #######################
    st.text("")
    st.text("")
    st.text("")
    st.html(
        "Average temperature and total daily bike rides are strongly correlated. <b style='color:#3881B5;'>Customers are more likely to use Citi Bikes in warmer weather</b>, and less likely to use them in colder weather. This pattern continued even with daily fluctuations in temperature. On September 27th and October 7th, the relatively high temperatures were paired with strong bike rental numbers. When the temperature dipped to a relative low of 10.3°C in between these two dates, bike rentals also dropped significantly. Rather than being a strictly seasonal trend, customers consider the weather daily when deciding to rent a Citi Bike.")
    st.text("")
    st.text("")
    st.html(
        "<h5 style='color:#3881B5;'>Possible reasons why more people bike in warm weather:</h5>")
    st.markdown(
        "- Summer is peak tourist season for international travelers$^{1}$.")
    st.markdown(
        "- Warm weather encourages outdoor exercise, so people may turn to our bicycles for daily transportation. This is consistent with data that subway usage in privileged areas goes down in summer months$^{2}$.")
    st.markdown(
        "- Commuters could work from home more more often during the summer and may not be traveling as long of distance as they would in the winter.")
    st.markdown(
        "- Children are out of school during the summer, and may be more likely to ride bikes")
    st.text("")
    st.html(
        "In addition to the overall increase daily bike rides over the summer, <b style='color:#3881B5;'>more customers choose Electric Bikes over the summer</b>. While the difference in Classic Bike rides taken is mild from May to July, the difference in Electric Bike rides taken is more dramatic. This is even despite known issues with heat sensitivity for Electric Bike batteries. Perhaps, the temperatures in New York City do not get high enough to cause performance issues.") 
    st.text("")
    st.text("")
    st.text("")
    st.html(
        "<em>(1) Source: Sea the City - When Is The Best Time To Visit New York City? (web)</em>")
    st.html(
        "<em>(2) Stechemesser, Annika et al. (2023) 'Inequality in behavioural heat adaptation: an empirical study with mobility data from the transport system in New York City, NY, USA'. The Lancet Planetary Health</em>")



################################ MOST POPULAR STATIONS ##################################
#########################################################################################

elif page == 'Most Popular Stations':

    st.html(
        "<h2 align='center'>Top 20 Most Popular Citi Bike Stations in New York</h2>"
    )
    st.html(
        "<h5 align='center'><em>If you've got the money, Citi Bike can take you there.</em></h5>"
    )

    
    ################## START/END TOGGLE #####################
    myKey = 'my_key'
    if myKey not in st.session_state:
        st.session_state[myKey] = False
    
    
    ####################### BAR CHARTS #######################
    if st.session_state[myKey]:
        col1, col2, col3 = st.columns(3)
        with col1:
            pass
        with col3:
            pass
        with col2:
            myBtn = st.button('Click to see Starting Stations', use_container_width=True)
            st.session_state[myKey] = False
        
        with st.sidebar:
         season_filter = st.multiselect(label= 'Select the season', options=bar_chart_end['season'].unique(),
         default= bar_chart_end['season'].unique())
         df1 = bar_chart_end.query('season == @season_filter')
         total_rides = float(df1['Total'].sum())    
         st.metric(label = 'Total Bike Rides', value= numerize(total_rides))

        ## Ending Stations Bar Chart
        bar_end_fig = go.Figure(px.bar(df1.sort_values(['Grand Total', 'rideable_type'], 
                                                                 ascending=[False, True]),
                                       x = 'end_station_name', 
                                       y = 'Total', 
                                       color = 'rideable_type',
                                       barmode = 'stack',
                                       color_discrete_sequence = colors))

        ## Formatting axes and titles
        bar_end_fig.update_layout(
            xaxis_title = dict(text = '<b>End Stations</b>', 
                               font = dict(size = 22, color = '#2B4B8D')),
            yaxis_title = dict(text = '<b>Total Trips</b>', 
                               font = dict(size = 22, color = '#2B4B8D')),
            xaxis = dict(tickfont = dict(size = 14, color = '#2B4B8D')),
            yaxis = dict(tickfont = dict(size = 14, color = '#2B4B8D')),
            legend_title_text = '',
            legend = dict(yanchor = 'top',
                          y = 0.95,
                          xanchor = 'right',
                          x = 0.95,
                          font = dict(size = 16)
                         ),
            width = 900, height = 600
        )

        bar_end_fig.update_xaxes(
            automargin = True 
        )

        st.plotly_chart(bar_end_fig, use_container_width = True)
        
    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            pass
        with col3:
            pass
        with col2:
            myBtn = st.button('Click to see Ending Stations', use_container_width=True)
            st.session_state[myKey] = True
        
        with st.sidebar:
         season_filter = st.multiselect(label= 'Select the season', options=bar_chart_start['season'].unique(),
         default= bar_chart_start['season'].unique())
         df2 = bar_chart_start.query('season == @season_filter')
         total_rides = float(df2['Total'].sum())    
         st.metric(label = 'Total Bike Rides', value= numerize(total_rides))

        ## Starting Stations Bar Chart
        bar_start_fig = go.Figure(px.bar(df2.sort_values('Grand Total', ascending=False),
                                         x = 'start_station_name', 
                                         y = 'Total', 
                                         color = 'rideable_type',
                                         barmode = 'stack',
                                         color_discrete_sequence = colors))

        ## Formatting axes and titles
        bar_start_fig.update_layout(
            xaxis_title = dict(text = '<b>Start Stations</b>', 
                               font = dict(size = 22, color = '#2B4B8D')),
            yaxis_title = dict(text = '<b>Total Trips</b>', 
                               font = dict(size = 22, color = '#2B4B8D')),
            xaxis = dict(tickfont = dict(size = 14, color = '#2B4B8D')),
            yaxis = dict(tickfont = dict(size = 14, color = '#2B4B8D')),
            legend_title_text = '',
            legend = dict(yanchor = 'top',
                          y = 0.95,
                          xanchor = 'right',
                          x = 0.95,
                          font = dict(size = 16)
                         ),
            width = 900, height = 600
        )

        bar_start_fig.update_xaxes(
        automargin = True 
        )

        st.plotly_chart(bar_start_fig, use_container_width = True)


    ####################### ANALYSIS #######################
    st.text("")
    st.text("")
    st.text("")
    st.html(
        "The station at <b style='color:#3881B5;'>W 21 St & 6 Ave</b> is the most popular starting and ending location for bike trips. This station sits right at the border between the expensive <b style='color:#3881B5;'>Chelsea and Flatiron District neighborhoods</b>. The table below list some of the most expensive neighborhoods in New York City (by median home sale price)$^{1}$. The selected rows are the neighborhoods with the most popular starting and ending stations.")
    st.text("")
    st.dataframe(
        expensive.style.applymap(
            lambda _: "background-color: #3881B5;", subset=([2,3], slice(None))),
        use_container_width = True
    )
    st.text("")
    st.html(
        "All of the top 20 starting and ending stations are in <b style='color:#3881B5;'>Manhattan</b>. This is interesting because Manhattan is only the 3rd most populous borough in New York City (Queens and Brooklyn having >400k more people)$^{2}$. The resident population does not predict how popular Citi Bikes would be.")
    st.text("")
    st.html(
        "<h5 align='center' style='color:#3881B5;'>Are New York City residents the ones traveling to these places?</h5>")
    st.text("")
    st.markdown(
        "Except for one station, all of the most popular starting stations were also the most popular ending stations. This could be an argument for communters being our largest demographic. However, the most popular stations are almost all near major tourist destinations: Central Park, Washington Square Park, Union Square, Madison Square Gardens/Penn Station, 9/11 Memorial, etc. It's likely that these stations are so popular because of their proximity to tourist destinations.")
    st.text("")
    st.text("")
    st.text("")
    st.html("<em>(1) Source: Property Shark - 50 Most Expensive Neighborhoods Q2 2024 (web)</em>")
    st.html("<em>(2) Source: U.S. Census Bureau (web)</em>")



####################### INTERACTIVE MAP OF AGGREGATED BIKE TRIPS ########################
#########################################################################################

elif page == 'Map of Aggregated Bike Trips':

    st.html(
        "<h2 align='center'>Aggregated Bike Trips in New York</h2>"
    )
    st.html(
        "<h5 align='center'><em>Where the subway ends, Citi Bike begins.</em></h5>"
    )

    
    ####################### GEOSPATIAL VISUALIZATION #######################
    with open(htmlpath,'r') as f: 
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height = 1000)

    ####################### ANALYSIS #######################
    st.text("")
    st.text("")
    st.text("")
    st.html(
        "The above map juxtaposes the aggregate all Citi Bike trip paths taken in 2022 with the layout of the MTA subway entrances. The data has been refined to only include the trip paths along which there were >1200 different trips. With that filter in place, the majority of the most popular trip paths happened within Manhattan. Despite there being subway stations branching out into the Bronx, Queens, and Brooklyn, very few trips starting or ending in those areas were popular enough to make it onto this map.")
    st.text("")
    st.html(
        "<h5 align='center' style='color:#3881B5;'>Citi Bike rides are connected to the MTA subway system</h5>")
    st.text("")
    st.html(
        "We can also see that the most popular trip paths were short, and tended to go along an avenue (headed north or south), or along a street (headed east or west). Interacting with the map also reveals that <b style='color:#3881B5;'>these short paths were often starting/ending at subway stations, or they were between stations</b>. Looking at the lower tip of Manhattan, there are a cluster of subway entrances, and very few popular bike paths. Conversely, on the western coast of Manhattan (by the Hudson River), there are few subway entrances and many popular bike paths (these paths also some of the longest on the map). <b style='color:#3881B5;'>People in New York rely on the subway to travel long distances, but use Citi Bike to fill in the gaps between those longer trips.</b>")
    st.text("")
    st.html("And finally, most of these common trip paths are between popular tourist destinations. Looking at popular paths around Central Park: almost all paths starting on the perimeter of Central Park ended at another station on an opposite side of Central Park. Not only is this a popular tourist destination, but Citi Bike is a popular way to travel through the park.")



################################# RECOMMENDATIONS #######################################
#########################################################################################

else:

    st.html(
        "<h2 align='center'>Recommendations</h2>"
    )

    col1, col2 = st.columns(2)
    with col1:
        myImage2 = Image.open(os.path.join(picturepath, 'citibike_station_close.jpg')) 
        #source: https://unsplash.com/photos/blue-citi-bike-bicycles-parked-on-sidewalk-8ol9rD0BHAU
        st.image(myImage2)

        
    with col2:
        st.text("")
        with st.expander("When and where could we see Citi Bike distribution issues?"):
            st.markdown(
                '''We should be most vigilant at our popular stations during summer months, because our customers enjoy using our bikes when the weather is warm. During winter and early spring, we should consider scaling back and investing in newer stations (with the goal of having these newers stations up and running by summer.''')
            st.html(
                "Only stations in expensive Manhattan neighborhoods receive enough traffic to warrant our attention. Specifically, stations also near popular tourist destinations. These stations are both most likely to have too few bikes available (popular starting stations), and most likely to have too few docking stations available (popular ending stations). <b style='color:#3881B5;'>In future analysis, we should look at the timing of bike rentals to see when these stations are most likely to face these two issues.</b>")
        with st.expander("What could be causing this issue?"):
            st.html(
                "The data presents two possible situations: <b style='color:#3881B5;'>1) Rich New Yorkers</b> using Citi Bike to commute to and from work, especially in the summer when the subway system deals with unbearable heat. <b style='color:#3881B5;'>2) Tourists</b> visiting New York using Citi Bike to travel between destinations on their sightseeing journeys. While these two situations are not mutually exclusive, our membership numbers (see below) indicate that it may be the native New Yorkers who drive most of our demand. We have about 3x as many members as we do casual riders.")
        with st.expander("Where can we expand to next?"):
            st.markdown(
                "- Along shores where subways cannot reach. The many beaches in Brooklyn (e.g. Sheepshead Bay) that would make excellent places to travel by bike. Our stations near Central Park and the Hudson River should be the model for ideal Citi Bike station placement because they don't depend on changing real estate values.")
            st.markdown(
                "- Other affluent neighborhoods in Brooklyn (i.e. Park Slope, Williamsburg, Brooklyn Heights, Cobble Hill, etc.) Because Brooklyn has a larger population than Manhattan, there's much more room to grow in this borough.")
            st.markdown(
                "- Areas in Brooklyn and Queens that are not well-connected by the subway system. The distance between subway stations in these boroughs is even greater than the distance we see in Manhattan.")
        with st.expander("Strategies to ensure docking stations are stocked"):
            st.markdown(
                "- Assign individuals to monitor individual neighborhoods or areas (like Central Park). People are generally taking short trips that start and end within the same neighborhood, so it's likely that if one station is running low on docked bikes, there's another station within the neighborhood that is nearing capacity. Keeping an individual focused on one area allows them to be much more expedient in solving an issue as it arises.")
            st.markdown(
                "- Ensure that docking stations are never more than 80% of capacity. We always want the option to dock a bicycle available at every Citi Bike station. And keeping fully docked stations is both an inefficient use of time and detrimental to our brand's image. We want people to think Citi Bike is an in-demand product, and fully docked stations send the message that nobody wants to use our bikes.")
            
    st.text("")
    st.text("")
    st.text("")
    st.html(
        "<h5 align='center'><em>Citi Bike members are the bulk of our users and take shorter trips (a median of just 9-10 minutes) than casual users. We need to prioritize making these short trips seamless to maintain our favorable rider experience and continued growth.</em></h5>")
    col1, col2 = st.columns([0.6, 0.4])
    with col1:
        ########################### DURATION HISTOGRAM #########################
        hist_fig = px.histogram(hist_duration_data,
                                x = 'trip_duration',
                                nbins = 50,
                                color = 'member_casual',
                                color_discrete_sequence = ['#2B4B8D', '#3881B5'])

        hist_fig.update_layout(bargap = 0.05)

        ## Calculate median for line label
        member_median_data = hist_duration_data.loc[hist_duration_data['member_casual'] == 'Member']
        member_median = np.median(member_median_data['trip_duration'])
        casual_median_data = hist_duration_data.loc[hist_duration_data['member_casual'] == 'Casual']
        casual_median = np.median(casual_median_data['trip_duration'])

        ## Add median line and annotation for both member and casual charts
        hist_fig.add_vline(x = member_median,
                           line_width = 2,
                           line_dash = 'solid',
                           line_color = accent)
        hist_fig.add_annotation(x = member_median,
                                y = 45000,
                                text = f"<b>Member Median: <br>{member_median:.0f} sec</b>",
                                font = dict(color = '#2B4B8D', size = 14),
                                showarrow = False,
                                xshift = -24,
                                yshift = 0)

        hist_fig.add_vline(x = casual_median,
                           line_width = 2,
                           line_dash = 'solid',
                           line_color = accent)
        hist_fig.add_annotation(x = casual_median,
                                y = 35000,
                                text = f"<b>Casual Median: <br>{casual_median:.0f} sec</b>",
                                font = dict(color = '#2B4B8D', size = 14),
                                showarrow = False,
                                xshift = 24,
                                yshift = 0)

        ## Formatting axes and titles
        hist_fig.update_layout(legend_title_text = '',
                               legend = dict(yanchor = 'top',
                                             y = 0.95,
                                             xanchor = 'right',
                                             x = 0.65,
                                             font = dict(size = 16)),
                               xaxis_title = dict(text = '<b>Trip Duration (in seconds)</b>',
                                                  font = dict(size = 18, color = '#2B4B8D')),
                               yaxis_title = dict(text = ''),
                               xaxis = dict(tickfont = dict(size = 14, color = '#2B4B8D')),
                               yaxis = dict(tickfont = dict(size = 14, color = '#2B4B8D'),
                                            visible = False),
                               width = 900, height = 400)
        
        st.plotly_chart(hist_fig, use_container_width = True)

    with col2:
        ####################### MEMBER STATUS PIE CHART ########################
        pie_fig = px.pie(pie_payment_data,
                         values = 'value',
                         names = 'member_casual',
                         color = 'member_casual',
                         color_discrete_sequence = ['#3881B5', '#2B4B8D'],
                         hole = 0.6,
                         labels = ['<b>Member</b>', '<b>Casual</b>'])

        ## Formatting pie chart and labels
        pie_fig.update_traces(textinfo = 'label+percent',
                              textfont_weight='bold',
                              textfont_size = 15,
                              insidetextorientation = 'horizontal',
                              showlegend = False,
                              rotation = 0)

        pie_fig.update_layout(height = 450, width = 450)

        st.plotly_chart(pie_fig, use_container_width = True)







