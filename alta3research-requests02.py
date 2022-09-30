#!/usr/bin/python3

import requests
from pprint import pprint

FRUIT_BASKET_URL = "http://127.0.0.1:2224/fruits"

resp = requests.get(FRUIT_BASKET_URL).json()

pprint(resp)