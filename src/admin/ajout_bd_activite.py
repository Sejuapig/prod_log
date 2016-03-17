#!/usr/bin/python
import readFile.readActivite as act
import admin.connexion as co

def run():
	tableau = act.run()
	db, curseur =co.run()

	add_act= "INSERT INTO activity (id, code, nom) VALUES(?,?,?)"

	for row in tableau:
		data= (row[0], row[1], row[2])
		curseur.execute(add_act, data)

	db.commit()
	db.close()