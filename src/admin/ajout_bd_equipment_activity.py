#!/usr/bin/python
import readFile.readEquipment_Activity as act
import admin.connexion as co

def run():
	"""Function allowing you to insert the equipment_activity table data in the database"""
	tableau = act.run()

	db, curseur =co.run()

	add= "INSERT OR IGNORE INTO equipment_activity(id_equipment, id_activity) VALUES(?,?)"

	for row in tableau:
		data= (row[0], row[1])
		curseur.execute(add, data)
	    
	db.commit()
	db.close()