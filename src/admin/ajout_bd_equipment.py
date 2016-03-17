#!/usr/bin/python
import readFile.readEquipement as equip
import admin.connexion as co

def run():
	tableau = equip.run()

	db, curseur =co.run()

	addEquipment= "INSERT INTO equipment (id, nom, id_installation) VALUES(?,?,?)"

	for row in tableau:
		data= (row[0], row[1], row[2])
		curseur.execute(addEquipment, data)
	    
	db.commit()
	db.close()