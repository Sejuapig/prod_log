#!/usr/bin/python
import readFile.readActivite as act
import admin.connexion as co

def run():
	
	tableau = act.run()
	db, curseur =co.run()

	add_act= "INSERT OR IGNORE INTO activity(id_activity, nom_activity) VALUES(?,?)"

	for row in tableau:
		data= (row[0], row[1])
		curseur.execute(add_act, data)

	db.commit()
	db.close()