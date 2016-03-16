
import sqlite3
import csv

def connexionInstall():
	conn = sqlite3.connect('installation.db')
	cursor = conn.cursor()
	cursor.execute('drop table if exists installation')
	cr_tb_install = "CREATE TABLE installation(id integer PRIMARY KEY NOT NULL, nom TEXT, adresse TEXT, code_postal TEXT, ville TEXT, latitude FLOAT, longitude FLOAT)"
	cursor.execute(cr_tb_install)

	fichier = csv.reader(open("/hometu/etudiants/m/e/E145465P/info2/prod_log/Production_logiciel/Installations.csv","rt"), delimiter=',')

	tableau = []
	ex ="INSERT INTO installation (id, nom, adresse, code_postal, ville, latitude, longitude) VALUES(?, ?, ?, ?,?, ?,?)"
	for row in fichier:
		data = (row[1],row[0],row[7],row[4],row[2],row[9],row[10])
		cursor.execute(ex,data)
		#tableau.append([row[2], row[4],row[5]]) #id, code et libelle   
	#return tableau[1:]
	conn.commit()
	conn.close()


if __name__ == '__main__':
	connexionInstall()