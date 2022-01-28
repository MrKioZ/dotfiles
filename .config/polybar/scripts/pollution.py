#!/bin/python
# -*- coding: utf-8 -*-
import requests

API_KEY = ""

r = requests.get("http://api.airvisual.com/v2/nearest_city?key={}".format(API_KEY))

pollution = r['data']['current']['pollution']['aqius']

print('{}'.format(pollution))
