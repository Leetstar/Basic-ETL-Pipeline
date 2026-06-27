#Transform the dataset

import pandas as pd
df = pd.DataFrame(weather_data)
df

import pandas as pd
df = pd.DataFrame(weather_data)
df['coord'] = df['coord'].apply(lambda x: f"({x['lat']}, {x['lon']})")

df

df.describe()
 
#cities with temparature greater than 35
hot_cities = df[df['temp'] > 35]
print(hot_cities)

#Correlation btw temparatue and humidity
correlation = df['temp'].corr(df['humidity'])
print(f"\nCorrelation between Temperature and Humidity: {correlation:.3f}")

#avearge temparature , minimum temparatue and max temparature
print(f"Average temparature: {df['temp'].mean():.3f}")
print(f"Minimum temparature: {df['temp'].min():.3f}")
print(f"Maximum temparature: {df['temp'].max():.3f}")
print(f"Temperature Range: {df['temp'].max() - df['temp'].min():.2f}")
