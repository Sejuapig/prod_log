#!/usr/bin/python
import mysql.connector as conn
import readActivite as act

def lunch():
	tableau = act.lunch()

	db = conn.connect(host="infoweb",user="E145465P", password="mdp",database="E145465P")

	curseur = db.cursor()

	for row in tableau:
	    add_act= "INSERT IGNORE INTO activity (id, code, nom) VALUES(%s, %s, %s)"
	    data= (row[0], row[1], row[2])
	    curseur.execute(add_act, data)

	db.commit()
	db.close()