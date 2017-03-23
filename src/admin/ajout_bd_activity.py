#!/usr/bin/python
import admin.connexion as connexion
import readFile.readActivity as act

def run():
	"""Function allowing you to insert the activity table data in the database"""
	
	tableau = act.run()
	conn = connexion.connexion()
	cursor = conn.cursor(prepared=True)

	insertQuery= "INSERT IGNORE INTO activity(id_activity, nom_activity) VALUES(?,?)"

	for row in tableau:
		data= (row[0], row[1])
		cursor.execute(insertQuery,data)

	conn.commit()
	conn.close()
