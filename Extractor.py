# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import os
import csv



path = "D:\\python\\2012-01-21.html"
mastercsv = "D:\\python\\BTFV-ELO.csv"
startelo = 800
games = 0
players = []

def get_players(file):
    with open(file, 'r') as r:
        html = bs(r, "html.parser")
        home = html.select(".col-md-6")
        for i in range(len(home)):
            helper = home[i].find_all("td", class_="")
            for j in range(len(helper)):
                players.append(helper[j].text.strip())
    names = players[1::2]
    print(names[0])
    with open(mastercsv, 'r+', newline='') as elo_csv:
        reader = csv.reader(elo_csv, delimiter='\t')
        writer = csv.writer(elo_csv, delimiter='\n')
        new_players = 0
        existing_players = 0
        for row in reader:
            for i in range(len(names)):
                if names[i] in row:
                    names.remove(name)
                    existing_players += 1
                else:
                    break
            if not names:
                break
            else:
                for i in range(len(names)):
                    writer.writerow(['\n' + names[i] + '\t' + str(startelo)+ '\t' + str(games)])
                    new_players += 1

    print("Existing = " + str(existing_players) + "| New = " + str(new_players))
        # print(players[1::2])



get_players(path)
