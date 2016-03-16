#!/usr/bin/python
import mysql.connector as conn

def lunch():
	db = conn.connect(host="infoweb",user="E145465P", password="mdp",database="E145465P")

	curseur = db.cursor()

	curseur.execute("DROP TABLE IF EXISTS installation")
	cr_tb_install = "CREATE TABLE IF NOT EXISTS installation(id INT PRIMARY KEY NOT NULL, nom TEXT, adresse TEXT, code_postal TEXT, ville TEXT, latitude FLOAT, longitude FLOAT)"

	curseur.execute("DROP TABLE IF EXISTS installation")
	cr_tb_equip = "CREATE TABLE IF NOT EXISTS equipment(id INT PRIMARY KEY NOT NULL, nom TEXT, id_installation INT)"

	curseur.execute("DROP TABLE IF EXISTS installation")
	cr_tb_act = "CREATE TABLE IF NOT EXISTS activity(id INT PRIMARY KEY NOT NULL, code INT, nom TEXT)"

	curseur.execute(cr_tb_install)
	curseur.execute(cr_tb_equip)
	curseur.execute(cr_tb_act)

	db.commit()
	db.close()