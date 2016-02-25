#!/usr/bin/python
import mysql.connector as conn
import readEquipement as equip

def lunch():
	tableau = equip.lunch()

	db = conn.connect(host="infoweb",user="E145465P", password="mdp",database="E145465P")

	curseur = db.cursor()

	for row in tableau:
	    add= "INSERT IGNORE INTO equipment (id, nom, id_installation) VALUES(%s, %s, %s)"
	    data= (row[0], row[1], row[2])
	    curseur.execute(add, data)
	    
	db.commit()
	db.close()