# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import csv
import numpy as np


path = "D:\\python\\2012-01-21.html"
mastercsv = "D:\\python\\BTFV-ELO.csv"
elo = 800
games = 0
players = []
firstnames = []
lastnames = []


def get_players(file):
    with open(file, 'r') as r:
        html = bs(r, "html.parser")
        home = html.select(".col-md-6")
        for i in range(len(home)):
            helper = home[i].find_all("td", class_="")
            for j in range(len(helper)):
                players.append(helper[j].text.strip())
    names = players[1::2]
    for name in names:
        fullnames = name.split(', ')
        firstnames.append(fullnames[1])
        lastnames.append(fullnames[0])
    # firstnames = fullnames[1::2]
    # lastnames = fullnames[::2]
    print(firstnames, lastnames)

    return names, firstnames, lastnames


def compare_players(file):
    names, firstnames, lastnames = get_players(file)
    with open(mastercsv, 'r+', newline='') as elo_csv:

        reader = csv.DictReader(elo_csv)
        # print(lastnames)
        for row in reader:
            # print(row)
            indices = [i for i, x in enumerate(lastnames) if x == row['Lastname']]
            for i in indices:
                if
            if row['Lastname'] in lastnames:
                # x = lastnames.index(row['Lastname'])
                print(row['Lastname'], x)
                if row['Firstname'] in firstnames[x]:
                    print('izz da')
                elif row['Short'] in firstnames[x]:
                    print('izz als Short da')

            # for name in names:
            #     fullname = name.split(', ')
            #     first_name = fullname[1]
            #     last_name = fullname[0]
                # if first_name == row['Firstname'] and last_name == row['Lastname']:
                #     print('Vorhanden')
                # else:
                #     print('nicht vorhanden')
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
