#!/usr/bin/python
import mysql.connector as conn
import readInstall as inst
import sqlite3 as conn2

def lunch():
	tableau = inst.lunch()

	#db = conn.connect(host="infoweb",user="E145465P", password="mdp",database="E145465P")
	db = conn2.connect("installation.db")

	curseur = db.cursor()
	curseur.execute('drop table if exists installation')
	cr_tb_install = "CREATE TABLE installation(id integer PRIMARY KEY NOT NULL, nom TEXT, adresse TEXT, code_postal TEXT, ville TEXT, latitude FLOAT, longitude FLOAT)"
	curseur.execute(cr_tb_install)
	for row in tableau:
		add_install= "INSERT INTO installation (id, nom, adresse, code_postal, ville, latitude, longitude) VALUES(?,?,?,?,?,?,?)"
		data= (row[0], row[1], row[2], row[3],row[4], row[5],row[6])
		data= (row[0], row[1], row[2], row[3],row[4], row[5],row[6])
		curseur.execute(add_install, data)

	db.commit()
	db.close()