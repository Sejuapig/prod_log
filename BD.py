#!/usr/bin/python
import mysql.connector as conn

db = conn.connect(host="infoweb",user="E145465P", password="mdp",database="E145465P")

curseur = db.cursor()

query = "create or replace table données"

curseur.execute(query)

result = curseur.fetchall()

for row in result:
    print(row)
    
db.close()