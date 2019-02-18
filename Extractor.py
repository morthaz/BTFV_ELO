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
    with open(mastercsv, 'r+', newline='') as elo_csv:
        reader = csv.reader(elo_csv, delimiter='\t')
        writer = csv.writer(elo_csv, delimiter='\t', quotechar='\n')
        new_players = 0
        existing_players = 0
        for row in reader:
            for name in names:
                if name in row:
                    names.remove(name)
                    existing_players += 1
                else:
                    break
            if not names:
                break
            else:
                for name in names:
                    fullname = name.split(', ')
                    first_name = fullname[0]
                    last_name = fullname[1]
                    writer.writerow(['\n' + last_name + '\t' + first_name + '\t' + str(startelo)+ '\t' + str(games)])
                    new_players += 1

    print("Existing = " + str(existing_players) + "| New = " + str(new_players))
        # print(players[1::2])



get_players(path)
