#!/usr/bin/env python3

# http://api.open-notify.org/iss-now.json

import requests
from pprint import pprint

response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response.text)
# print(type(response.text))

data = response.json()

lat = float(data['iss_position']['latitude'])
lon = float(data['iss_position']['longitude'])

# print(lat)
# print(lon)
print(f'The ISS is at ({lat}, {lon}).')

