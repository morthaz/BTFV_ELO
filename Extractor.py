# -*- encoding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import os


comma = ","
path = "D:\\python\\2012-01-21.html"
players = []

def check_players(file):
    with open(file, 'r') as r:
        html = bs(r, "html.parser")
        home = html.select(".col-md-6")
        for i in range(len(home)):
            helper = home[i].find_all("td", class_="")
            for j in range(len(helper)):
                players.append(helper[j].text.strip())


        print(players[1::2])


check_players(path)
