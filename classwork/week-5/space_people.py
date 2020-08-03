#!/usr/bin/env python3

# http://api.open-notify.org/astros.json

import requests
from pprint import pprint

response = requests.get("http://api.open-notify.org/astros.json")
# print(response.text)
# print(type(response.text))

data = response.json()

people = data['people']

for person in people:
    print(f"{person['name']} is on {person['craft']}.")

# pprint(people)



