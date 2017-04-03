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
		installation = bd.installation(commune)
		list_installation = []
		for row in installation:
			list_installation.append({"id_installation" : row[0], "nom_installation" : row[1], "adresse" : row[2], "code_postal" : row[3], "ville" : row[4], "latitude" : row[5], "longitude" : row[6]})

	if(commune ==""):
		installation = bd.sport(commune)
		list_installation = []
		for row in installation:
			list_installation.append({"id_installation" : row[0], "nom_installation" : row[1], "adresse" : row[2], "code_postal" : row[3], "ville" : row[4], "latitude" : row[5], "longitude" : row[6]})

	if(commune =="" and sport =="waloo"):
		return "Veuillez selectionner au moins une commune ou un sport."
		
	if(sport != "waloo" and commune != ""):
		installation = bd.sport_installation(commune, sport)
		list_installation = []
		for row in installation:
			list_installation.append({"id_installation" : row[0], "nom_installation" : row[1], "adresse" : row[2], "code_postal" : row[3], "ville" : row[4], "latitude" : row[5], "longitude" : row[6]})

	#Clé API Google map :  AIzaSyAV5H8jgF1rKLszZfpRbhP7hivmsgAryY0 

	API_KEY = "VUKSyIY4sVm2supyeSGPtZvm5m1E33Mi"

	try:
		proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'

		urlParams = {'location': commune, 'key': 'VUKSyIY4sVm2supyeSGPtZvm5m1E33Mi', 'inFormat':'kvp', 'outFormat':'json'}
		url = "http://www.mapquestapi.com/geocoding/v1/address?" + urlencode(urlParams)

		req = urllibrequest.Request(url)
		req.set_proxy(proxy_host, 'http')

		resp = urllibrequest.urlopen(req)

		data = resp.read().decode('utf8')
		jsonData = json.loads(data)
		# FIXME le print n'est pas très secure...
		lat = jsonData['results'][0]['locations'][0]['latLng']['lat']
		lng = jsonData['results'][0]['locations'][0]['latLng']['lng']
		print('latitude : ' + str(lat))
		print('longitude : ' + str(lng))
	except Exception as err:
		print("Unexpected error: {0}".format(err))

	if(len(list_installation) == 0):
		return "Aucune ativité disponible."
	else:
		tous = json.dumps(list_installation)
		jsonEnForme = ""
		for i in range(0,len(list_installation)) :
			jsonEnForme += json.dumps("Nom de l'installation : " + list_installation[i]['nom_installation'] + '</br>' + "Adresse : " + list_installation[i]['adresse'] + '</br>' + "Code postal : " + list_installation[i]['code_postal'] + '</br>' + "Id : " + str(list_installation[i]['id_installation']) + '</br>' + "Latitude : " + str(list_installation[i]['latitude']) + '</br>' + "Longitude : " + str(list_installation[i]['longitude'])) + '</br>' + '</br>'

	#print(jsonEnForme)
	return jsonEnForme
	#return static_file("map.html", root='./RestServer/')

run(host='localhost', port=8070)