# -*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import urllib.request
import os

"""
Datei crawled von der BTFV-Seite alle Spielberichte und extrahiert aus dem Spielbericht Mannschaftsnamen und Datum.
Es wird eine Kopie des Spielberichts mit diesen Informationen abgespeichert.
"""



# start: RumpfURL zu Spielberichten
start = 'https://btfv.de/sportdirector/spielbericht/anzeigen/'

# i: Initial von 0-2500 gecrawled, zurzeit werden die Spielberichte im Bereich 2080-2500 neu angelegt (nicht linear)
for i in range(2080, 2500):
    try:

        # r: crawled die einzelnen Spielberichte, die sich aus start, dem Counter und '/no_frame' zusammensetzen
        r = requests.get(start + str(i) + '/no_frame')
        html = bs(r.content, "html.parser")

        # team1, team2: selektiert den Teamnamen aus der Soup.
        team1 = html.select(".col-md-5")[0].text.strip()
        team2 = html.select(".col-md-5")[1].text.strip()

        # alles im nächsten Absatz ist dazu da, den Dateinamen zu ändern.
        title = html.select_one(".page-header").text
        title_list = title.split('  ')
        liga = title_list[0].split(' ')
        liga[0] = liga[0].strip()

        # Datumsextraktion
        spieltag = title_list[1].split(' vom ')
        nummer = spieltag[0]
        datum = spieltag[1].split('.')

        # Unterordner erstellen
        pfad = "C:\\Users\\menn\\projects\\BTFV_ELO\\BTFV-Spielergebnisse" + "\\" + liga[0] + "\\" + liga[1]
        if not os.path.exists(pfad):
            os.makedirs(pfad)

        # File speichern
        filename = team1 + "-" + team2 + "_" + datum[0] + "-" + datum[1] + "-" + datum[2].strip() + ".html"
        urllib.request.urlretrieve(start + str(i) + '/no_frame', pfad + "\\" + filename)
        print(i)
    except:
        print(str(i) + " does not exist")

print("Fertig!")







