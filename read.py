import csv
def read(path):
    fichier = csv.reader(open(path,"rt"))
    
    for row in fichier:
        print(row[2],row[3],row[1]  row[180], row[181])