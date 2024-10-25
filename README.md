# Citi Bike in New York City 2022 -
# Exploring Current User Behavior and Expansion Opportunities
<p align="center">
  <img width="1261" alt="Screenshot 2024-09-06 at 2 37 26 PM" src="https://github.com/user-attachments/assets/2aea39da-cba7-4af2-925f-7430462d15c6">
</p>
<h3 align="center">
  Building a strategic data dashboard that answers Citi Bike business questions.
</h3>


## TABLE OF CONTENTS
<details>
<ul>
  <li><a href="#general-info">General Info</a></li>
  <li><a href="#tools">Tools</a></li>
  <li><a href="#data-source">Data Source</a></li>
  <li><a href="#project-file-setup">Project File Setup</a></li>
  <li><a href="#citation">Citation</a></li>
</ul>
</details>


## GENERAL INFO
Citi Bike's popularity has increased since its launch in 2013, and during the Covid-19 pandemic, even more New York residents have seen the merit in bike sharing. The higher demand has led to distribution problems (i.e. too few bikes at popular stations, or too many bikes parked at stations making it impossible to return a bike). This application will diagnose where these distribution issues are most likely to arise, and theorize what the root of the problem may be.

1. Is there a seasonal demand for Citi Bike?
2. How much should we scaling bikes back during the low-demand season?
3. Which stations are the most popular starting/ending stations?
4. Where are we most likely to see distribution issues?
5. What are some ideas for ensuring bikes are always stocked at the most popular stations?

<p align="center">
<img width=80% alt="-Pngtree—blue connecting network world map_7325681" src="https://github.com/user-attachments/assets/01be5328-fea9-417e-bdef-ebd57f7c5f58"> 
</p>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## TOOLS
For this project, the following Python libraries were used:
* pandas - for data analysis
* numpy - for mathematical equations
* matplotlib + seaborn + plotly - for data visualization
* keplergl - for geospatial visualization
* pillow - for supporting image file integration
* streamlit - to build and host the data app
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## DATA SOURCE
Open source data was acquired from the **[Citi Bike Database for the year 2022](https://citibikenyc.com/system-data)**. To supplement this data, weather data gathered from **[NOAA's](https://www.noaa.gov/)** API service was gathered. Only the daily average temperature was needed from this dataset. A separate open source dataset of the MTA subway entrance locations in New York City was obtained from **[Open NY](https://data.ny.gov/widgets/i9wp-a4ja)**.
Data was scraped from the Wikipedia page, **[Key events of the 20th century](https://en.wikipedia.org/w/index.php?title=Key_events_of_the_20th_century&oldid=1244115362)**, in 
<br>
<br>
<br>
<i>**Potential Bias #1:** There were a significant amount of outliers in respect to Citi Bike trip duration. About 5% of rides were too long to include in trip duration distribution data. So, this analysis does not take into account the behavior of customers who use Citi Bike for long distance trips.</i>
<br>
<br>
<i>**Potential Bias #2:** Only a sample of the data could be included in the geospatial and distribution visualizations. The sample is theoretically representative of the larger population, but testing this sample was out of the scope of this project. Data was sampled by:</i>
```
np.random.seed(32)
red = np.random.rand(len(df_duration_clean)) <= 0.975
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## PROJECT FILE SETUP
1. Project Management
     * Project brief laying out the expectations and deliverables
2. Data
     * Citi Bike ride data for 2022
     * New York Weather Data for 2022
     * Expensive New York neighborhood data: `data-16QWY.csv`
     * Subway entrance data: `MTA_Entrances_2024.csv`
     * Cleaned and wrangled data for dashboard visualizations
3. Scripts: Jupyter notebooks and python files
     * Sourcing Bike and Weather Data
     * Data Cleaning
     * Data Visualizations
     * Geospatial Visualizations
     * Final Database Data Wrangling
     * Creating a Data Dashboard
4. Visualizations
     * Images for the dashboard
     * Screenshots of the visualizations for sharing with stakeholders
     * Geospatial visualization HTML file
  
<p display="flex" justify-content="center" align="center" align-items="center" text-align="center">
<img width=48% alt="degree_centrality_20th-Century_countries" src="https://github.com/user-attachments/assets/dbf6f334-7e0c-405d-80ab-a65ba1e87d94">      <img width=48% alt="alt="Screenshot 2024-09-06 at 2 11 12 PM" src="https://github.com/user-attachments/assets/2adda307-685b-4f9e-beb5-3f63923d4e7c">
</p>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## CITATION
Citi Bike System Data (data pulled on October 14, 2024) [https://citibikenyc.com/system-data)](https://citibikenyc.com/system-data)
<p align="right">(<a href="#readme-top">back to top</a>)</p>
