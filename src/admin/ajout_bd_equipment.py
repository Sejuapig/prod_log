#!/usr/bin/python
import readFile.readEquipment as equip
import admin.connexion as co

def run():
	tableau = equip.run()

	db, curseur =co.run()

	addEquipment= "INSERT OR IGNORE INTO equipment (id_equipment, nom_equipment, id_installation) VALUES(?,?,?)"

	for row in tableau:
		data= (row[0], row[1], row[2])
		curseur.execute(addEquipment, data)
	    
	db.commit()
	db.close()