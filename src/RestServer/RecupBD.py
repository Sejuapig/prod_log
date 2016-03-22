import admin.connexion as co
#from bson.json_util import dumps

def run():
	db, curseur = co.run()

	curseur.execute("select * from activity")
	activity = curseur.fetchall()

	equipment = curseur.execute("select * from equipment")
	equipment = curseur.fetchall()

	installation = curseur.execute("select * from installation")
	installation = curseur.fetchall()

	for row in activity:
		print(row)

	for row in installation:
		print(row)
		
	#dumps(activity)
	#dumps(equipment)
	#dumps(installation)

	return (activity, equipment, installation)

if __name__ == '__main__':
	run()