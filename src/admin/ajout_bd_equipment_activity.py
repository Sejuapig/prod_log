#!/usr/bin/python
# coding: utf8
import mysql
import admin.connexion as connexion
import readFile.readEquipment_Activity as act

def run():
	"""Function allowing you to insert the equipment_activity table data in the database"""

	tableau = act.run()
	conn = connexion.connexion()
	cursor = conn.cursor(prepared=True)

	insertQuery= "INSERT INTO equipment_activity(id_equipment, id_activity) VALUES(?,?)"

	for row in tableau:
		try :
			data = (row[1], row[0])
			cursor.execute(insertQuery, data)
<<<<<<< HEAD
		except MySQLdb.Error as e :
			print(e)
=======
		except mysql.connector.errors.IntegrityError as err:
			 print("Error: {}".format(err))
>>>>>>> 8fb9aafabea0afcfbea0d4d5c954c097e475aa6c

	conn.commit()
	conn.close()