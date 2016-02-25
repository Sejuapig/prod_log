#!/usr/bin/python
import mysql.connector as conn
import readInstall as inst

def lunch():
	tableau = inst.lunch()

	db = conn.connect(host="infoweb",user="E145465P", password="mdp",database="E145465P")

	curseur = db.cursor()

	for row in tableau:
	    add_install= "INSERT IGNORE INTO installation (id, nom, adresse, code_postal, ville, latitude, longitude) VALUES(%s, %s, %s, %s,%s, %s,%s)"
	    data= (row[0], row[1], row[2], row[3],row[4], row[5],row[6])
	    curseur.execute(add_install, data)

	db.commit()
	db.close()