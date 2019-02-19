# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import csv


path = "D:\\python\\2012-01-21.html"
mastercsv = "D:\\python\\BTFV-ELO.csv"
elo = 800
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
    return names


def compare_players(file):
    names = get_players(file)
    with open(mastercsv, 'r+', newline='') as elo_csv:

        reader = csv.DictReader(elo_csv)
        for row in reader:
            for name in names:
                fullname = name.split(', ')
                first_name = fullname[1]
                last_name = fullname[0]
                if first_name == row['Firstname'] and last_name == row['Lastname']:
                    print(name)
            # readrow = reader[row].split(',')
            # name_dict = { "Player" + row:{"Name": readrow[0] + ' ' + readrow[1], "ELO": readrow[2], "Games": readrow[3]}}
            # print(name_dict)
            # for name in names:
            #     if name in row:
            #         names.remove(name)
            #         existing_players += 1
            #     else:
            #         break
            # if not names:
            #     break


def write_players(file):
    names = get_players(file)
    with open(mastercsv, 'r+', newline='') as elo_csv:
        fieldnames = ['Lastname', 'Firstname', 'Short', 'ELO', 'Games']
        writer = csv.DictWriter(elo_csv, quotechar='\n', fieldnames=fieldnames)
        writer.writeheader()
        new_players = 0
        existing_players = 0
        for name in names:
            fullname = name.split(', ')
            first_name = fullname[1]
            last_name = fullname[0]
            first_name_short = fullname[1][0] + '.'
            name_dict = writer.writerow({'Lastname': last_name, 'Firstname': first_name, 'Short': first_name_short,
                             'ELO': str(elo), 'Games': str(games)})
            new_players += 1
    print("Existing = " + str(existing_players) + "| New = " + str(new_players))
    # print(players[1::2])


compare_players(path)
