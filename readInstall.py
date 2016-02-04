import csv
def read(path):
    fichier = csv.reader(open(path,"rt"), delimiter=',')
    
    for row in fichier:
        print(row[1],row[2],row[9],row[10]) #numero et nom
        
if __name__ == '__main__':
    read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Installations.csv")