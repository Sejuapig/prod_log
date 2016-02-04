import csv
def read(path):
    fichier = csv.reader(open(path,"rt"), delimiter=',')
    
    for row in fichier:
        print(row[2], row[4],row[5]) #id, code et libelle
        
if __name__ == '__main__':
    read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/activites.csv")