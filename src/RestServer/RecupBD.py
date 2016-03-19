import admin.connexion as co
#from bson.json_util import dumps

def run():
	db, curseur = co.run()

	activity = []
	equipment = []
	installation = []

	activity = curseur.execute("select * from activity")
	equipment = curseur.execute("select * from equipment")
	installation = curseur.execute("select * from installation")

	dumps(activity)
	dumps(equipment)
	dumps(installation)

	return (activity, equipment, installation)

if __name__ == '__main__':
	run()