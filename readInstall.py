import csv
def read(path):
    fichier = csv.reader(open(path,"rt"), delimiter=',')
    
    for row in fichier:
        print(row[1],row[0],row[7],row[4],row[2],row[9],row[10]) #numero et nom et coordonées
        
if __name__ == '__main__':
    read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/Installations.csv")