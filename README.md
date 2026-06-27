# Weather Data ETL Pipeline

## Overview

This project implements a simple ETL (Extract, Transform, Load) pipeline that fetches real-time weather data from the OpenWeatherMap API for multiple cities, processes the data, performs analysis, and stores the results in a CSV file.

![image alt](https://github.com/Leetstar/Basic-ETL-Pipeline/blob/d9159958e5f4ed8812d33eb964beb23a3189de84/architecture.png)


## Features

Extract: Fetches weather data from OpenWeatherMap API for 6 cities

Transform: Processes JSON data, cleans coordinates, filters hot cities

Load: Saves processed data to CSV file

Analyze: Calculates statistics and correlations


## Prerequisites

Python 3.6+

OpenWeatherMap API key (free tier available)


## Installation

1)Clone the repository:

```bash
git clone <repository-url>
cd weather-etl-pipeline
```
2)Install required packages:

```bash
pip install requests pandas
```

3)Configuration

Replace the API key in the script:

```python
API_KEY = "your_openweather_api_key_here"
```

## Pipeline Steps


1)Extract

Makes API calls to OpenWeatherMap for each city

Retrieves: temperature, humidity, pressure, coordinates, and weather description

Handles API errors gracefully

2)Transform

Converts API response to structured DataFrame

Formats coordinate data to readable format

Identifies cities with temperature > 35°C

3)Analyze

Calculates temperature statistics:

Mean temperature

Minimum temperature

Maximum temperature

Temperature range

Computes correlation between temperature and humidity

4)Load

Saves processed data to weather_data_cleaned.csv

Output Files

weather_data_cleaned.csv: Contains cleaned weather data for all cities

## Sample Output

```Text
	city	            coord	humidity	temp	pressure	    description
0	Kuwait City   	(29.3697, 47.9783)	21	40.60	999	     clear sky
1	London	        (51.5085, -0.1257)	36	34.53	1015	  scattered clouds
2	Tokyo	          (35.6895, 139.6917)	93	22.36	1005	  moderate rain
3	Mexico	        (15.0646, 120.7198)	82	26.89	1010	  overcast clouds
4	Doha	          (25.2867, 51.5333)	18	40.60	1000	  clear sky
5	Malaysia	            (2.5, 112.5)	95	23.40	1011	   overcast clouds

Hot cities (>35°C):
          city               coord  humidity   temp  pressure description
0  Kuwait City  (29.3697, 47.9783)        25  37.43      1002   clear sky
4         Doha  (25.2867, 51.5333)        16  40.11      1002   clear sky


Correlation between Temperature and Humidity: -0.979

Statistical Analysis:
Average temparature: 31.397
Minimum temparature: 22.360
Maximum temparature: 40.600
Temperature Range: 18.24
```
