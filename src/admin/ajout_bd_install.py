#!/usr/bin/python
import readFile.readInstall as inst
import admin.connexion as co

def run():
	"""Function allowing you to insert the installation table data in the database"""
	tableau = inst.run()

	db, curseur = co.run()

	add_install= "INSERT OR IGNORE INTO installation (id_installation, nom_installation, adresse, code_postal, ville, latitude, longitude) VALUES(?,?,?,?,?,?,?)"

	for row in tableau:
		data= (row[0], row[1], row[2], row[3],row[4], row[5],row[6])
		curseur.execute(add_install, data)

	db.commit()
	db.close()