from RestServer.libs.bottle import *
import RestServer.RecupBD as bd
import json
import cgi

@route('/')
def server_static():
	return static_file("html.html", root='./RestServer/')


@route('/site/activite/<ville>')
def getAct(ville):
        act = bd.activites(ville)
        return act



	
run(host='localhost', port=8080)