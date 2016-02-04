#!/usr/bin/python
import mysql.connector as conn

db = conn.connect(host="infoweb",user="E145465P", password="mdp",database="E145465P")

curseur = db.cursor()

query = "CREATE TABLE IF NOT EXISTS(id INT PRIMARY KEY NOT NULL)"

curseur.execute(query)

    
db.close()