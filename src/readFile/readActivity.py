import csv

def run():
	return read("../../Production_logiciel/csvFiles/activites.csv")

def read(path):
	fichier = csv.reader(open(path,"rt"), delimiter=',')

	tableau = []

	for row in fichier:
		tableau.append([row[4], row[5]]) #id et libelle   
	return tableau[1:]

if __name__ == '__main__':
	read("../../Production_logiciel/csvFiles/activites.csv")