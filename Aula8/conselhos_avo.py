#!/usr/bin/python3
from datetime import date
import os
import re
import sys
from getopt import getopt
import requests
import shelve
from tqdm import tqdm
from bs4 import BeautifulSoup

weather = [
    {
        'date': '2 Dom',
        'prev_txt': 'Céu nublado por nuvens altas',
        'temp_min': 13,
        'temp_max': 28,
        'uv': 8
    },
    {
        'date': '3 Seg',
        'prev_txt': 'Céu pouco nublado',
        'temp_min': 11,
        'temp_max': 27,
        'uv': 9
    },
    {
        'date': '4 Qua',
        'prev_txt': 'Céu limpo',
        'temp_min': 9,
        'temp_max': 31,
        'uv': 8
    }
]
today = date.today().day
for day in weather:
    if today is not int(day["date"].split()[0]):
        continue
    else:
        if day["temp_min"] < 15:
            print("Leva um casaco")
        if day["uv"] > 7:
            print("Sai do sol que faz mal!")
