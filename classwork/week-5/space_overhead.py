#!/usr/bin/env python3

# http://api.open-notify.org/iss-pass.json?lat=LAT&lon=LON

import requests
from datetime import datetime, timedelta, timezone
from dateutil import tz

LAT = 41.95
LON = -87.75

NUM = 100

JAPAN = tz.gettz('Asia/Tokyo')
CHICAGO = tz.gettz('America/Chicago')

URL = f"http://api.open-notify.org/iss-pass.json?lat={LAT}&lon={LON}&n={NUM}"

response = requests.get(URL)
# print(response.text)
# print(type(response.text))

data = response.json()
times = data['response']

for overhead in times:
    # print(overhead)
    risetime = overhead['risetime']

    # Convert string to
    dt = datetime.fromtimestamp(risetime)
    # convert utc to local
    dt_local = dt.replace(tzinfo=timezone.utc).astimezone(tz=CHICAGO)

    the_time = dt_local.strftime("%B %d %Y %-I:%M:%S %p %Z")

    duration = timedelta(seconds=overhead['duration'])

    print(f"The ISS will be over my head at {the_time} for {duration} seconds.")

