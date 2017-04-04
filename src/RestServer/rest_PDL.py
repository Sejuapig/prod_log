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
	"""Function allowing you return the activities of the database for a given city and/or a given sport when you connect to the route"""
	commune = request.query.commune
	sport = request.query.sport

	#if there is no sport but a city
	if(sport =="Aucun"):
		installation = bd.installation(commune)
		list_installation = []
		for row in installation:
			list_installation.append({"id_installation" : row[0], "nom_installation" : row[1], "adresse" : row[2], "code_postal" : row[3], "ville" : row[4], "latitude" : row[5], "longitude" : row[6]})

	#if there is no city but a sport
	if(commune ==""):
		installation = bd.sport(commune)
		list_installation = []
		for row in installation:
			list_installation.append({"id_installation" : row[0], "nom_installation" : row[1], "adresse" : row[2], "code_postal" : row[3], "ville" : row[4], "latitude" : row[5], "longitude" : row[6]})

	#if there is no city and no sport
	if(commune =="" and sport == "Aucun"):
		return "Veuillez selectionner au moins une commune ou un sport."

	#if there is a city and a sport
	if(sport != "Aucun" and commune != ""):
		installation = bd.sport_installation(commune, sport)
		list_installation = []
		for row in installation:
			list_installation.append({"id_installation" : row[0], "nom_installation" : row[1], "adresse" : row[2], "code_postal" : row[3], "ville" : row[4], "latitude" : row[5], "longitude" : row[6]})

	#Clé API Google map :  AIzaSyAV5H8jgF1rKLszZfpRbhP7hivmsgAryY0

	API_KEY = "VUKSyIY4sVm2supyeSGPtZvm5m1E33Mi"

	try:
		#use to be able to bypass the proxy
		proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'

		#build the URL to connect to the API of reverse geocoding : MapQuest
		urlParams = {'location': commune, 'key': 'VUKSyIY4sVm2supyeSGPtZvm5m1E33Mi', 'inFormat':'kvp', 'outFormat':'json'}
		url = "http://www.mapquestapi.com/geocoding/v1/address?" + urlencode(urlParams)

		#connection to the URL
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
		listeJSON = json.dumps(list_installation)
		resEnForme = ""
		for i in range(0,len(list_installation)) :
			resEnForme += json.dumps("Nom de l'installation : " + list_installation[i]['nom_installation'] + '</br>' + "Adresse : " + list_installation[i]['adresse'] + '</br>' + "Code postal : " + list_installation[i]['code_postal'] + '</br>' + "Id : " + str(list_installation[i]['id_installation']) + '</br>' + "Latitude : " + str(list_installation[i]['latitude']) + '</br>' + "Longitude : " + str(list_installation[i]['longitude'])) + '</br>' + '</br>'

	button = '</br> <form action="http://localhost:8070/" methode="GET"> <input TYPE="submit" NAME="nom" VALUE="Nouvelle recherche"> </form>' 
	#print(jsonEnForme)
	return resEnForme + button
	#return static_file("map.html", root='./RestServer/', rows=tous)
	#output = template('./RestServer/map.tpl', rows=tous)
	#return output

run(host='localhost', port=8070)
