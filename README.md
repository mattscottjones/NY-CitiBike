# Citi Bike in New York City 2022 -Exploring Current User Behavior and Expansion Opportunities
<p align="center">
  <img width="1261" alt="Screenshot 2024-09-06 at 2 37 26 PM" src="https://github.com/user-attachments/assets/2aea39da-cba7-4af2-925f-7430462d15c6">
</p>
<h3 align="center">
  Scraping a Wikipedia page to find country interrelations in the 20th century.
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

1. Which countries had the most influence during the 20th Century?
2. What patterns in country relationships can we identify?

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
Data was scraped from the Wikipedia page, **[Key events of the 20th century](https://en.wikipedia.org/w/index.php?title=Key_events_of_the_20th_century&oldid=1244115362)**, in August 2024. Using BeautifulSoup the full text of the article was saved as a text file, `20th Century Events.txt`. And using Selenium, all names of countries in the article were compiled into a csv file `countries_list_20th_century_1.5.csv`. 

The full details of the data are available **[here](https://en.wikipedia.org/w/index.php?title=Key_events_of_the_20th_century&oldid=1244115362)**.
<br>
<br>
<br>
<i>**Potential Bias #1:** The information on Wikipedia is curated by editors around the world. Although there is little incentive for bias in this data, the method of data recording lends itself to possible errors.</i>
<br>
<br>
<i>**Potential Bias #2:** Relying on only one source to determine a country's global importance introduces sampling bias. Depending on the main contributing editors to this Wikipedia page, there may be an emphasis on certain countries' involvement in global affairs over others. For instance, in 2024, we're seeing the consequences of many decades of unrest between Egypt, Israel, Palestine, Syria, and other Middle Eastern countries. The preceding events, that began in the 20th century, are not mentioned in this article.</i>
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## PROJECT FILE SETUP
1. Project Management
     * Project brief laying out the expectations and deliverables
2. Data
     * Wikipedia text file: `20th Century Events.txt`
     * List of countries csv file: `countries_list_20th_century_1.5.csv`
     * Cleaned data files for analysis
3. Scripts: Jupyter notebooks containing all code
     * Creating a Virtual Environment
     * Data Scrape
     * Text Mining
     * Data Cleaning
     * NLP Network Analysis
     * Network Visualizations
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
