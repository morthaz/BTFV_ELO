import os
import shutil

"""
Um eine Elo-Wertung zu erstellen sollten die Spielberichte chronologisch abgespeichert werden. 
"""

pfad = "D:\BTFV-Elo"
dateien = os.listdir(pfad)
i=0
for element in dateien:
    if element != "Datumssortiert":

        # time.sleep(0.5)
        datum_ger = element.split('_')[-1].strip('.html')
        date = datum_ger.split('-')
        datum = date[2]+ "-" + date[1] + "-" + date[0]
        # print(datum)
        newpfad = pfad + "\\" + "Datumssortiert"
        # print(element)
        if not os.path.exists(newpfad):
            os.makedirs(newpfad)
        if not os.path.exists(newpfad + '\\' + datum + '.html'):
            shutil.copy(pfad + '\\' + element, newpfad + '\\' + datum + '.html')
        else:
            shutil.copy(pfad + '\\' + element, newpfad + '\\'+ datum + '(' + str(i) + ')' + '.html')
        i += 1
        print(i)
        #
