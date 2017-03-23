import csv

def run():
	"""Function allowing you to return the .csv data in an array"""
	return read("../../prod_log/csvFiles/activites.csv")

def read(path):
	""""Function allowing you to read the .csv files in the path and collect the rows wanted"""
	fichier = csv.reader(open(path,"rt"), delimiter=',')

	tableau = []

	for row in fichier:
		tableau.append([row[4], row[2]]) #id de l'activité et id de l'équipement   
	return tableau[1:]

if __name__ == '__main__':
	read("../../prod_log/csvFiles/activites.csv")