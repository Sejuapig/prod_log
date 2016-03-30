import admin.connexion as co
import json
import collections

def run():
	db, curseur = co.run()

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

def 

if __name__ == '__main__':
	run()