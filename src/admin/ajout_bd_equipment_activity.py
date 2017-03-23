#!/usr/bin/python
import readFile.readEquipment_Activity as act
import admin.connexion as connexion

def run():
	"""Function allowing you to insert the equipment_activity table data in the database"""
	tableau = act.run()

	conn = connexion.connexion()
	cursor = conn.cursor(prepared=True)

	insertQuery= "INSERT IGNORE INTO equipment_activity(id_equipment, id_activity) VALUES(?,?)"

	for row in tableau:
		data= (row[0], row[1])
		cursor.execute(insertQuery, data)
	    
	conn.commit()
	conn.close()