import csv

def run():
	"""Function allowing you to return the .csv data in an array"""
	return read("../../prod_log/csvFiles/Installations.csv")
	 
def read(path):
	""""Function allowing you to read the .csv files in the path and collect the rows wanted"""
	fichier = csv.reader(open(path,"rt"), delimiter=',')
	
	tableau= []
		
	for row in fichier:
	   tableau.append([row[1],row[0],row[7],row[4],row[2],row[9],row[10]]) #numero, nom et coordonées

	return tableau[1:]

if __name__ == '__main__':
	read("../../prod_log/csvFiles/Installations.csv")