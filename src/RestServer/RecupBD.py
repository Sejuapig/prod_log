import admin.connexion as connexion
import json
import collections

def activites(ville):
	"""Function allowing you to collect data from the table activity of the database for a given city and then parse it into json arrays and finally returning it"""
	conn = connexion.connexion()
	cursor = conn.cursor()

	cursor.execute("select * from activity where ville = "+ ville)
	activity = cursor.fetchall()

	return activity

def installation(ville):
	"""Function allowing you to collect data from the table activity of the database for a given city and then parse it into json arrays and finally returning it"""
	conn = connexion.connexion()
	cursor = conn.cursor()

	selectQuery = "select * from installation where ville = '"+ ville + "';"

	cursor.execute(selectQuery)
	installation = cursor.fetchall()
	print(installation)
	return installation

def sport(sport):
	"""Function allowing you to collect data from the table activity of the database for a given city and then parse it into json arrays and finally returning it"""
	conn = connexion.connexion()
	cursor = conn.cursor()

	selectQuery = "select * from installation, activity, equipment, equipment_activity where equipment.id_installation = installation.id_installation and equipment_activity.id_equipment = equipment.id_equipment and equipment_activity.id_activity = activity.id_activity and activity.nom_activity = '"+sport+"'";

	cursor.execute(selectQuery)
	installation = cursor.fetchall()
	print(installation)
	return installation

def sport_installation(ville, sport):
	"""Function allowing you to collect data from the table activity of the database for a given city and then parse it into json arrays and finally returning it"""
	conn = connexion.connexion()
	cursor = conn.cursor()

	selectQuery = "select * from installation, activity, equipment, equipment_activity where installation.ville = '"+ville+"' and equipment.id_installation = installation.id_installation and equipment_activity.id_equipment = equipment.id_equipment and equipment_activity.id_activity = activity.id_activity and activity.nom_activity = '"+sport+"'";

	cursor.execute(selectQuery)
	installation = cursor.fetchall()
	print(installation)
	return installation


	

if __name__ == '__main__':
	run()