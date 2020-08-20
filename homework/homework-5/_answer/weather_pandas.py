from pprint import pprint

import pandas as pd
import requests

# https://openweathermap.org/api/one-call-api

APPID="ea42045886608526507915df6b33b290"
LAT = 41.95
LON = -87.75
EXCLUDE=(
    "current",
    "minutely",
    "hourly",
    # "daily",
)
UNITS="imperial"

URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={','.join(EXCLUDE)}&appid={APPID}&units={UNITS}"

# print(URL)

response = requests.get(URL)
data = response.json()

df = pd.json_normalize(data['daily'])
print(df)



# pprint(data['daily'])

# # df = pd.DataFrame(data['daily'])

# # print(df['temp'])

