#!/usr/bin/python
import mysql.connector as conn

db = conn.connect(host="infoweb",user="E145465P", password="mdp",database="E145465P")

curseur = db.cursor()

cr_tb_test = "CREATE TABLE IF NOT EXISTS test42(id INT PRIMARY KEY NOT NULL)"

#curseur.execute(cr_tb_test)

add_install= "INSERT INTO test42(id) VALUES(42)"

curseur.execute(add_install)

db.close()