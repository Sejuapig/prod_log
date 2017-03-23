import admin.connexion as connexion
import json
import collections

def run():
	"""Function allowing you to collect data from the tables of the database and then parse it into json arrays and finally returning it"""
	db, curseur = connexion.connexion()

	curseur.execute("select * from activity")
	activity = curseur.fetchall()

	curseur.execute("select * from equipment")
	equipment = curseur.fetchall()

	curseur.execute("select * from installation")
	installation = curseur.fetchall()

	curseur.execute("select * from equipment_activity")
	equipment_activity = curseur.fetchall()

	list_activity = []
	for row in activity:
		d = collections.OrderedDict()
		d['id_activity'] = row[0]
		d['nom_activity'] = row[1]
		list_activity.append(d)

	list_equipment = [] 
	for row in equipment:
		d = collections.OrderedDict()
		d['id_equipment'] = row[0]
		d['nom_equipment'] = row[1]
		d['id_installation'] = row[2]
		list_equipment.append(d)

	list_installation = [] 
	for row in installation:
		d = collections.OrderedDict()
		d['id_installation'] = row[0]
		d['nom_installation'] = row[1]
		d['adresse'] = row[2]
		d['code_postal'] = row[3]
		d['ville'] = row[4]
		d['latitude'] = row[5]
		d['longitude'] = row[6]
		list_installation.append(d)

	list_equipment_activity = []
	for row in equipment_activity:
		d = collections.OrderedDict()
		d['id_equipment'] = row[0]
		d['id_activity']  = row[1]
		list_equipment_activity.append(d)

	activity = json.dumps(list_activity)
	equipment = json.dumps(list_equipment)
	installation = json.dumps(list_installation)
	equipment_activity = json.dumps(list_equipment_activity)

	
	activity = json.loads(activity)
	equipment = json.loads(equipment)
	installation = json.loads(installation)
	equipment_activity = json.loads(equipment_activity)
	
	return (activity, equipment, installation, equipment_activity)

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

	list_installation = [] 
	for row in installation:
		list_installation.append(row)

	print(list_installation)

	return json.dumps(installation)

if __name__ == '__main__':
	run()