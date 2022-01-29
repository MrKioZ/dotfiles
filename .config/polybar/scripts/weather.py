#!/bin/python
# -*- coding: utf-8 -*-

# Procedure
# Surf to https://openweathermap.org/city
# Fill in your CITY
# e.g. Antwerp Belgium
# Check url
# https://openweathermap.org/city/2803138
# you will the city code at the end
# create an account on this website
# create an api key (free)
# LANG included thanks to krive001 on discord


import requests, json, os, time
from datetime import datetime, timedelta

CITY = ""
API_KEY = ""
UNITS = "Metric"
UNIT_KEY = "C"
#UNIT_KEY = "F"
LANG = "en"
#LANG = "nl"
#LANG = "hu"

with open(f'/home/{os.getlogin()}/.config/polybar/scripts/cache/weather.json', 'r+') as f:
    data = json.loads(f.read())
    last_request = datetime.strptime(data['last_request'].split('.')[0], "%Y-%m-%dT%H:%M:%S")


if ((datetime.now() - last_request) >= timedelta(hours=12)) or (data['temp'] == 0):
    try:
        REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&lang={}&appid={}&units={}".format(CITY, LANG,  API_KEY, UNITS))
        CURRENT = REQ["weather"][0]["main"].capitalize()
        TEMP = int(float(REQ["main"]["temp"]))

        with open(f'/home/{os.getlogin()}/.config/polybar/scripts/cache/weather.json', 'w+') as f:
            data['current'] = CURRENT
            data['temp'] = TEMP
            f.write(json.dumps(data))

    except (ValueError, IOError):
        print("Error: Unable print the data")
else:
    CURRENT = data['current']
    TEMP = data['temp']

# CURRENT = 'Rain'

if CURRENT == "Thunderstorm":
    CURRENT = " "
elif CURRENT == "Drizzle":
    CURRENT = ""
elif CURRENT == "Rain":
    CURRENT = ""
elif CURRENT == "Snow":
    CURRENT = ""
elif CURRENT == "Clear":
    CURRENT = ""
elif CURRENT == "Clouds":
    CURRENT = ""
else:
    CURRENT = ""

print("{}  {} °{}".format(CURRENT, TEMP, UNIT_KEY))

