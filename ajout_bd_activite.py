#!/usr/bin/python
import mysql.connector as conn
import readActivite as act

tableau = act.lunch()

db = conn.connect(host="infoweb",user="E145465P", password="mdp",database="E145465P")

curseur = db.cursor()

for row in tableau:
    add_act= "INSERT INTO activite (id, code, libelle) VALUES(%s, %s, %s)"
    data= (row[0], row[1], row[2])
    curseur.execute(add_act, data)
    
db.close()