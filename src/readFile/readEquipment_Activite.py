import csv

def run():
	return read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/csvFiles/activites.csv")

def read(path):
	fichier = csv.reader(open(path,"rt"), delimiter=',')

	tableau = []

	for row in fichier:
		tableau.append([row[4], row[2]]) #id de l'activité et id de l'équipement   
	return tableau[1:]

if __name__ == '__main__':
	read("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/csvFiles/activites.csv")