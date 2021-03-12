from bs4 import BeautifulSoup
import csv
import requests
import sys

txt = requests.get(sys.argv[1]).text

soup = BeautifulSoup(txt)

i = 1
for table in soup.findAll("table"):
    tab = []
    for row in table.findAll("tr"):
        t = [x.text for x in row.findAll(["th", "td"])]
        tab.append(t)
    with open(f"tabela{i}.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(tab)
    i+=1
    # print(tab)
