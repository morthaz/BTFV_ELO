import os
import shutil

"""
Um eine Elo-Wertung zu erstellen sollten die Spielberichte chronologisch abgespeichert werden. 
"""

base_path = os.path.dirname(os.path.abspath(__file__))
game_results_dir = os.path.dirname(os.path.abspath(__file__)) + "\\BTFV-Spielergebnisse"
i = 0
for subdir, dirs, files in os.walk(game_results_dir):
    for file in files:
        # time.sleep(0.5)
        datum_ger = file.split('_')[-1].strip('.html')
        date = datum_ger.split('-')
        datum = date[2]+ "-" + date[1] + "-" + date[0]
        # print(datum)
        new_path = base_path + "\\Datumssortiert"
        pathin = os.path.join(subdir, file)
        pathout = new_path + '\\' + datum + '(' + str(i) + ')' + '.html'
        print(pathin)
        print(pathout)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        if not os.path.exists(new_path + '\\' + datum + '.html'):
            shutil.copy(subdir + "\\" + file, base_path  + "\\Datumssortiert\\" + datum + '.html')
        else:
            with open(pathin, 'rt') as fin:
                print("open pathin rt")
                with open(pathout, 'wt') as fout:
                    print("open pathout wt")
                    for line in fin:
                        fout.write(line.replace('class=\"\"', 'class=\"player\"'))
            # shutil.copy(game_results_dir + '\\' + element, game_results_dir + '\\'+ datum + '(' + str(i) + ')' + '.html')
        i += 1
        print(i)