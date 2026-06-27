###
import requests
API_KEY = "9ba08c20d79704bed1770f3374f8650c"  # replace with your OpenWeather key
cities = ["Kuwait City","London","Tokyo","Mexico","Doha","Malaysia"]

weather_data=[]
for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code==200:
         data = response.json()
         weather_data.append({
         "city":city,
         "coord":data['coord'],
         "humidity":data['main']['humidity'],
         "temp":data['main']['temp'],
         "pressure":data['main']['pressure'],
        'description':data['weather'][0]['description']
         })
    else:
        print("Failed to get response.status_code()")
print(weather_data)
