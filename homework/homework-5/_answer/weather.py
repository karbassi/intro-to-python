from datetime import datetime

import requests

# https://openweathermap.org/api/one-call-api
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={YOUR API KEY}

APPID = "ea42045886608526507915df6b33b290"
LAT = 41.95
LON = -87.75
EXCLUDE = (
    "current",
    "minutely",
    "hourly",
    # "daily",
)
UNITS = "imperial"

URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={','.join(EXCLUDE)}&appid={APPID}&units={UNITS}"

response = requests.get(URL)
data = response.json()
# print(data['daily'])

for day in data["daily"]:
    date = datetime.fromtimestamp(day["dt"]).strftime("%a %b %-d")
    min = day["temp"]["min"]
    max = day["temp"]["max"]
    pop = day["pop"]

    forecast = day['weather'][0]['description']
    # print(forecast)

    print(f"{date}: {forecast}")




    # print(
    #     f"On {date}, the minimum temp will be {min:.0f}°F and maximum temp will be {max:.0f}°F. Probability of precipitation is at {pop:.0%}."
    # )
