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
