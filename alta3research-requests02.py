#!/usr/bin/python3

import requests
from pprint import pprint

FRUITS_URL = "http://127.0.0.1:2224/fruits"

resp = requests.get(FRUITS_URL).json()

pprint(resp)