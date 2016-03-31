from RestServer.libs.bottle import *
import RestServer.RecupBD as bd
import json
import cgi

@route('/')
def server_static():
	"""Function allowing you to display the website when you connect to the route"""
	return static_file("html.html", root='./RestServer/')


@route('/site/activite/<ville>')
def getAct(ville):
	"""Function allowing you return the activities of the database for a given city when you connect to the route"""
        act = bd.activites(ville)
        return act



	
run(host='localhost', port=8080)