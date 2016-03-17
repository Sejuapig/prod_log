#!/usr/bin/python
import admin.connexion as co

def run():
	db, curseur = co.run()

	curseur.execute("DROP TABLE IF EXISTS installation")
	cr_tb_install = "CREATE TABLE IF NOT EXISTS installation(id INT, nom TEXT, adresse TEXT, code_postal TEXT, ville TEXT, latitude FLOAT, longitude FLOAT)"

	curseur.execute("DROP TABLE IF EXISTS equipment")
	cr_tb_equip = "CREATE TABLE IF NOT EXISTS equipment(id INT, nom TEXT, id_installation INT)"

	curseur.execute("DROP TABLE IF EXISTS activity")
	cr_tb_act = "CREATE TABLE IF NOT EXISTS activity(id INT, code INT, nom TEXT)"

	curseur.execute(cr_tb_install)
	curseur.execute(cr_tb_equip)
	curseur.execute(cr_tb_act)

	db.commit()
	db.close()