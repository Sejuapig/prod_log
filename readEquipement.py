import csv

def lunch():
	return read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/equipements.csv")

def read(path):
    fichier = csv.reader(open(path,"rt"), delimiter=',')
    tableau =[]
    
    for row in fichier:
        tableau.append([row[4],row[3],row[2]]) #id et nom et id installation
    return tableau[1:]

if __name__ == '__main__':
    read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/equipements.csv")