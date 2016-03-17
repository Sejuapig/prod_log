#!/usr/bin/python
import admin.connexion as co

def run():
	db, curseur = co.run()

	curseur.execute("DROP TABLE IF EXISTS installation")
	cr_tb_install = "CREATE TABLE IF NOT EXISTS installation(id_installation INT, nom_installation TEXT PRIMARY KEY, adresse TEXT, code_postal TEXT, ville TEXT, latitude FLOAT, longitude FLOAT)"

	curseur.execute("DROP TABLE IF EXISTS equipment")
	cr_tb_equip = "CREATE TABLE IF NOT EXISTS equipment(id_equipment INT PRIMARY KEY , nom_equipment TEXT, id_installation INT)"

	curseur.execute("DROP TABLE IF EXISTS activity")
	cr_tb_act = "CREATE TABLE IF NOT EXISTS activity(id_activity INT PRIMARY KEY, nom_activity TEXT)"

	curseur.execute("DROP TABLE IF EXISTS equipment_activity")
	cr_tb_equip_act = "CREATE TABLE IF NOT EXISTS equipment_activity(id_equipment INT, id_activity INT, PRIMARY KEY (id_equipment, id_activity)  FOREIGN KEY(id_equipment) REFERENCES equipment(id),FOREIGN KEY(id_activity) REFERENCES activity(id))"

	curseur.execute(cr_tb_install)
	curseur.execute(cr_tb_equip)
	curseur.execute(cr_tb_act)
	curseur.execute(cr_tb_equip_act)

	db.commit()
	db.close()