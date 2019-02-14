# -*- encoding: cp852 -*-
import requests
from bs4 import BeautifulSoup as bs
import urllib.request
import os
import time


start = 'https://btfv.de/sportdirector/spielbericht/anzeigen/'
for i in range(2080, 2500):
    try:
        r = requests.get(start + str(i) + '/no_frame')
        html = bs(r.text, "html.parser")

        team1 = html.select(".col-md-5")[0].text.strip()
        team2 = html.select(".col-md-5")[1].text.strip()

        title = html.select_one(".page-header").text
        title_list = title.split('  ')
        liga = title_list[0].split(' ')
        liga[0] = liga[0].strip()
        if liga[1].startswith('S') and liga[1].endswith('d'):
            liga[1] = 'Sued'
        elif liga[1].startswith('S') and liga[1].endswith('est'):
            liga[1] = 'Sued-West'
        elif liga[1].startswith('S') and liga[1].endswith('Ost'):
            liga[1] = 'Sued-Ost'



        spieltag = title_list[1].split(' vom ')
        nummer = spieltag[0]
        datum = spieltag[1].split('.')
        pfad = "D:\BTFV-Spielergebnisse" + "\\" + liga[0] + "\\" + liga[1]
        if not os.path.exists(pfad):
            os.makedirs(pfad)
        filename = team1 + "-" + team2 + "_" + datum[0] + "-" + datum[1] + "-" + datum[2].strip() + ".html"
        urllib.request.urlretrieve(start + str(i) + '/no_frame', pfad + "\\" + filename)
        print(i)
    except:
        print(str(i) + " does not exist")

print("Fertig!")







