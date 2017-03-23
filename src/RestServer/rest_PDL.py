from RestServer.libs.bottle import *
import RestServer.RecupBD as bd
import json
import cgi

@route('/')
def server_static():
	"""Function allowing you to display the website when you connect to the route"""
	return static_file("html.html", root='./RestServer/')


@route('/site/activite')
def getAct():
	"""Function allowing you return the activities of the database for a given city when you connect to the route"""
	sport = request.query.sport
	commune = request.query.commune
	if(sport =="waloo"):

	if(commune ==""):
		

	installation = bd.installation(commune)
	
	list_installation = [] 
	for row in installation:
		list_installation.append({"id_installation" : row[0], "nom_installation" : row[1], "adresse" : row[2], "code_postal" : row[3], "ville" : row[4], "latitude" : row[5], "longitude" : row[6]})

	return json.dumps(list_installation)


def parseAct(activity):
	return activity['id_activity'], activity['nom_activity']


run(host='localhost', port=8070)

"""select * from installation, activity, equipment, equipment_activity where installation.ville = "Nantes" and equipment.id_installation = installation.id_installation and equipment_activity.id_equipment = equipment.id_equipment and equipment_activity.id_activity = activity.id_activity and activity.nom_activity = "football";"""