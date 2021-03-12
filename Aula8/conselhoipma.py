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

r = requests.get(
    "https://www.ipma.pt/pt/otempo/prev.localidade.hora/#Braga&Braga")
with open("cena.html") as f:
    soup = BeautifulSoup(f.read(), features="html.parser")

semana = soup.find('div', {'id': 'weekly'})
weather = []
for dia in semana:
    day = dia.find('div', {'class': 'date'}).text
    descr = dia.find('img', {'class': 'weatherImg'})["title"]
    temp_min = dia.find('span', {'class': 'tempMin'}).text
    temp_max = dia.find('span', {'class': 'tempMax'}).text
    if dia.find('img', {'class': 'iuvImg'}) is not None:
        uv = dia.find('img', {'class': 'iuvImg'})["title"].split()[-1]
    else:
        uv = -100
    dicionario = {
        "date": day,
        "prev_text": descr,
        "temp_min": temp_min,
        "temp_max": temp_max,
    }
    if uv != -100:
        dicionario["uv"] = uv
    weather.append(dicionario)

print(weather)
