#!/usr/bin/env python3

# Using the OpenWeather One Call API, display the daily forecast for the next 7 days. Each day's forecast should display:

# the day (e.g. August 3)
# the minimum and maximum temperatures in Fahrenheit and rounded to the nearest integer (e.g. 63)
# probability of precipitation in percentage format (e.g.
# You can display this via the terminal or use Pandas to display a graphic.


import requests
from pprint import pprint
from datetime import date, datetime, timedelta

LAT = 41.9069952
LON = -87.77236479999999

today = date.today()

response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall?lat=41.9069952&lon=-87.77236479999999&units=imperial&exclude=hourly&dt=1586468027&appid=ea42045886608526507915df6b33b290"
)

data = response.json()
loc = data["timezone"]
forecast = data["daily"]
temp = data["current"]["temp"]
hum = data["current"]["humidity"]
# pprint(forecast)


for weather in forecast:

    date = datetime.fromtimestamp(weather['dt']).strftime("%b-%d-%Y")

    temp = weather["temp"]['max']

    print(f"This is the forecast for {date} in {loc}.")
    print(f"the temperature for today is {temp}. ")
    print(f"the humidity for today is {hum}. ")
    # break


# 5 day outlook failed attempt:

# response = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=Chicago&appid=ea42045886608526507915df6b33b290")

# x = response.json()
# current_temperature = data["temp"]

# pprint(current_temperature)
