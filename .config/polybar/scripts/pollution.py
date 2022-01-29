#!/bin/python
# -*- coding: utf-8 -*-
import requests, json, os, time
from datetime import datetime, timedelta

API_KEY = ""

with open(f'/home/{os.getlogin()}/.config/polybar/scripts/cache/weather.json', 'r+') as f:
    data = json.loads(f.read())
    last_request = datetime.strptime(data['last_request'].split('.')[0], "%Y-%m-%dT%H:%M:%S")


if ((datetime.now() - last_request) >= timedelta(hours=6)) or (data['pollution'] == 0):
    r = requests.get("http://api.airvisual.com/v2/nearest_city?key={}".format(API_KEY))

    pollution = r['data']['current']['pollution']['aqius']

    data['last_request'] = str(datetime.now().isoformat())


    with open(f'/home/{os.getlogin()}/.config/polybar/scripts/cache/weather.json', 'w+') as f:
        data['pollution'] = pollution
        f.write(json.dumps(data))

else:
    pollution = data['pollution']

if pollution <= 50:
    os.environ["POLLUTION_COLOR"] = "#a8e05f"
elif pollution <= 100:
    os.environ["POLLUTION_COLOR"] = "#fdd64b"
elif pollution <= 150:
    os.environ["POLLUTION_COLOR"] = "#ff9b57"
elif pollution <= 200:
    os.environ["POLLUTION_COLOR"] = "#fe6a69"
elif pollution <= 250:
    os.environ["POLLUTION_COLOR"] = "#a97abc"
elif pollution <= 300:
    os.environ["POLLUTION_COLOR"] = "#a87383"

print('{}'.format(pollution))
