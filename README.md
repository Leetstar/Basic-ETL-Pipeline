Weather Data ETL Pipeline

Overview

This project implements a simple ETL (Extract, Transform, Load) pipeline that fetches real-time weather data from the OpenWeatherMap API for multiple cities, processes the data, performs analysis, and stores the results in a CSV file.

![image alt](https://github.com/Leetstar/Basic-ETL-Pipeline/blob/d9159958e5f4ed8812d33eb964beb23a3189de84/architecture.png)


Features

Extract: Fetches weather data from OpenWeatherMap API for 6 cities

Transform: Processes JSON data, cleans coordinates, filters hot cities

Load: Saves processed data to CSV file

Analyze: Calculates statistics and correlations


Prerequisites

Python 3.6+
OpenWeatherMap API key (free tier available)


Installation
1)Clone the repository:
