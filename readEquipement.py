import csv
def read(path):
    fichier = csv.reader(open(path,"rt"), delimiter=',')
    
    for row in fichier:
        print(row[4],row[3],row[2]) #id et nom et id installation
        
if __name__ == '__main__':
    read("/hometu/etudiants/m/e/E145465P/info2/prod_log/equipements.csv")