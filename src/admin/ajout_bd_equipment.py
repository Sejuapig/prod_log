#!/usr/bin/python
# coding: utf8
import admin.connexion as connexion
import readFile.readEquipment as equip

def run():
	"""Function allowing you to insert the equipment table data in the database"""

	tableau = equip.run()
	conn = connexion.connexion()
	cursor = conn.cursor(prepared=True)

	insertQuery= "INSERT IGNORE INTO equipment (id_equipment, nom_equipment, id_installation) VALUES(?,?,?)"

	for row in tableau:
		data= (row[0], row[1], row[2])
		try:
			cursor.execute(insertQuery,data)
		except MySQLdb.Error as e :
			print(e)
	    
	conn.commit()
	conn.close()