import admin.connexion as co
import json
import collections
#from bson.json_util import dumps

def run():
	db, curseur = co.run()

	curseur.execute("select * from activity")
	activity = curseur.fetchall()

	curseur.execute("select * from equipment")
	equipment = curseur.fetchall()

	curseur.execute("select * from installation")
	installation = curseur.fetchall()

	objects_list = []
	for row in activity:
		d = collections.OrderedDict()
		d['id_activity'] = row[0]
		d['nom_activity'] = row[1]
		#print(row[0])
		objects_list.append(d)

	#print(objects_list)

	print('--------------------------------------------')
	objects_list = json.dumps(objects_list, ensure_ascii=False).encode('utf8')
	print(objects_list)
	#for row in objects_list:
	print(objects_list['id_activity'])
	j = json.dumps(objects_list)
	objects_file = 'student_objects.js'
	f = open(objects_file,'w', encoding ='utf-8')
	f.write(j)

	return (activity, equipment, installation)

if __name__ == '__main__':
	run()