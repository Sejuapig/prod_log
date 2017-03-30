from RestServer.libs.bottle import *
from urllib.parse import urlencode
from urllib import request as urllibrequest
import http.client
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
	commune = request.query.commune
	sport = request.query.sport
	
	if(sport =="waloo"):
		print("Waloo")

	if(commune ==""):
		print("vide")

	installation = bd.installation(commune)
	
	list_installation = [] 
	for row in installation:
		list_installation.append({"id_installation" : row[0], "nom_installation" : row[1], "adresse" : row[2], "code_postal" : row[3], "ville" : row[4], "latitude" : row[5], "longitude" : row[6]})

	API_KEY = "VUKSyIY4sVm2supyeSGPtZvm5m1E33Mi"

	try:
		proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'

		urlParams = {'location': commune, 'key': API_KEY, 'inFormat':'kvp', 'outFormat':'json'}
		url = "http://www.mapquestapi.com/geocoding/v1/address?" + urlencode(urlParams)

		req = urllibrequest.Request(url)
		req.set_proxy(proxy_host, 'http')

		resp = urllibrequest.urlopen(req)

		data = resp.read().decode('utf8')
		jsonData = json.loads(data)
		# FIXME le print n'est pas très secure...
		print(jsonData['results'][0]['locations'][0]['latLng'])
	except Exception as err:
		print("Unexpected error: {0}".format(err))


	#return json.dumps(list_installation)


def parseAct(activity):
	return activity['id_activity'], activity['nom_activity']


run(host='localhost', port=8070)

"""select * from installation, activity, equipment, equipment_activity where installation.ville = "Nantes" and equipment.id_installation = installation.id_installation and equipment_activity.id_equipment = equipment.id_equipment and equipment_activity.id_activity = activity.id_activity and activity.nom_activity = "football";"""