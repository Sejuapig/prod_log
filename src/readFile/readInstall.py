import csv

def lunch():
    return read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/Installations.csv")
     
def read(path):
    fichier = csv.reader(open(path,"rt"), delimiter=',')
    
    tableau= []
        
    for row in fichier:
       tableau.append([row[1],row[0],row[7],row[4],row[2],row[9],row[10]]) #numero, nom et coordonées
    
    
    return tableau[1:]
if __name__ == '__main__':
    read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/Installations.csv")
    
