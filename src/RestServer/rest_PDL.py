from RestServer.libs.bottle import *
import RestServer.RecupBD as bd
import json
import cgi

@route('/')
def server_static():
	print("salut")
	return static_file("html.html", root='./RestServer/')
	activity, equipment, installation, equipment_activity = bd.run()

@route('/site/activitesg/<ville>')
def getAct(ville):
        act = bd.activites(ville)
        return act



	
run(host='localhost', port=8080)