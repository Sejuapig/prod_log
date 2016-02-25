import csv

def lunch():
    return read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/activites.csv")

def read(path):
    fichier = csv.reader(open(path,"rt"), delimiter=',')

<<<<<<< HEAD
=======
    tableau = []

>>>>>>> a1fcf1d53646ef8de6529732eeb272d91106c5dc
    for row in fichier:
        tableau.append(row[2], row[4],row[5]) #id, code et libelle
        
    return tableau[1:]

    if __name__ == '__main__':
    read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/activites.csv")