#!/usr/bin/python3

import requests
from pprint import pprint

# Variable to store URL for Fruit Basket data
FRUIT_BASKET_URL = "http://127.0.0.1:2224/fruits"

# Send a GET request to the Fruit Basket URL and return a json object
resp = requests.get(FRUIT_BASKET_URL).json()

# Print out resp
pprint(resp)