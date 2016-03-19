import csv

def run():
	return read("../../Production_logiciel/csvFiles/Installations.csv")
	 
def read(path):
	fichier = csv.reader(open(path,"rt"), delimiter=',')
	
	tableau= []
		
	for row in fichier:
	   tableau.append([row[1],row[0],row[7],row[4],row[2],row[9],row[10]]) #numero, nom et coordonées

	return tableau[1:]

if __name__ == '__main__':
	read("/../../../Production_logiciel/csvFiles/Installations.csv")