#!/usr/bin/python
import readFile.readInstall as inst
import admin.connexion as co

def run():
	tableau = inst.run()

	db, curseur = co.run()

	add_install= "INSERT INTO installation (id, nom, adresse, code_postal, ville, latitude, longitude) VALUES(?,?,?,?,?,?,?)"

	for row in tableau:
		data= (row[0], row[1], row[2], row[3],row[4], row[5],row[6])
		curseur.execute(add_install, data)

	db.commit()
	db.close()