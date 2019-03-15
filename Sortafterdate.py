import os
import shutil

"""
Um eine Elo-Wertung zu erstellen sollten die Spielberichte chronologisch abgespeichert werden. 
"""

pfad = "G:\BTFV-Elo"
dateien = os.listdir(pfad)
i = 0
for element in dateien:
    if element != "Datumssortiert":

        # time.sleep(0.5)
        datum_ger = element.split('_')[-1].strip('.html')
        date = datum_ger.split('-')
        datum = date[2]+ "-" + date[1] + "-" + date[0]
        # print(datum)
        newpfad = pfad + "\\" + "Datumssortiert"
        pathin = pfad + '\\' + element
        pathout = newpfad + '\\' + datum + '(' + str(i) + ')' + '.html'
        # print(element)
        if not os.path.exists(newpfad):
            os.makedirs(newpfad)
        if not os.path.exists(newpfad + '\\' + datum + '.html'):
            shutil.copy(pfad + '\\' + element, newpfad + '\\' + datum + '.html')
        else:
            with open(pathin, 'rt') as fin:
                with open(pathout, 'wt') as fout:
                    for line in fin:
                        fout.write(line.replace('class=\"\"', 'class=\"player\"'))
            # shutil.copy(pfad + '\\' + element, newpfad + '\\'+ datum + '(' + str(i) + ')' + '.html')
        i += 1
        print(i)
        #
