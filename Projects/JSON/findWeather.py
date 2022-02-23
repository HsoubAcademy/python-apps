import requests, json

# section 3
api_key = "e59574bf6b887f0e08af237fa247ff89"

# section 1
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# section 2
city_name = input("Enter city name : ")

# complete url address
complete_url = base_url + "q=" + city_name + "&units=metric" + "&appid=" + api_key

# response object
response = requests.get(complete_url)
#print(response.text)

x = json.loads(response.text)

if x["cod"] != "404":

    y = x["main"]

    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]

    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Temperature (in metric unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in metric unit) = " +
          str(current_pressure) +
          "\n humidity (in metric) = " +
          str(current_humidity) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")