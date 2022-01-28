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


import requests

CITY = ""
API_KEY = ""
UNITS = "Metric"
UNIT_KEY = "C"
#UNIT_KEY = "F"
LANG = "en"
#LANG = "nl"
#LANG = "hu"

# with open("cache/weather.json", "rw+") as f:
#     data = json.loads(f.read())


REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&lang={}&appid={}&units={}".format(CITY, LANG,  API_KEY, UNITS))

try:
    # HTTP CODE = OK
    CURRENT = REQ["weather"][0]["description"].capitalize()
    TEMP = int(float(REQ["main"]["temp"]))
    print("{}, {} °{}".format(CURRENT, TEMP, UNIT_KEY))
    # else:
    #     print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable print the data")
