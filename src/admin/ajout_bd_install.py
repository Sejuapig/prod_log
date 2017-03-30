#!/usr/bin/python
# coding: utf8
import readFile.readInstall as inst
import admin.connexion as connexion

def run():
	"""Function allowing you to insert the installation table data in the database"""
	tableau = inst.run()

	conn = connexion.connexion()
	cursor = conn.cursor(prepared=True)

	insertQuery= "INSERT IGNORE INTO installation (id_installation, nom_installation, adresse, code_postal, ville, latitude, longitude) VALUES(?,?,?,?,?,?,?)"

	for row in tableau:
		data = (row[0], row[1], row[2], row[3],row[4], row[5],row[6])
		try:
			cursor.execute(insertQuery, data)
		except MySQLdb.Error as e :
			print(e)

	conn.commit()
	conn.close()