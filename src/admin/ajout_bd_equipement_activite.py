#!/usr/bin/python
import readFile.readEquipment_Activite as act
import admin.connexion as co

def run():
	tableau = act.run()

	db, curseur =co.run()

	add= "INSERT OR IGNORE INTO equipment_activity(id_equipment, id_activity) VALUES(?,?)"

	for row in tableau:
		data= (row[0], row[1])
		curseur.execute(add, data)
	    
	db.commit()
	db.close()