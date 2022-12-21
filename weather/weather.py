import requests

API_KEY = "04660775b13aed05381005c88cf1d93d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#Query parameters - basically what data we want

city = input("Enter a city name: ")
requestURL = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requestURL)
if response.status_code == 200: #success
    data = response.json()
    weather = data['weather'][0]['description']
    temp = round(data['main']['temp'] - 273.15,2)
    print("Weather:",weather)
    print("Tempature:",temp,"Celcius")
    

else:
    print("An Error Occured")