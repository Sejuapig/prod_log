from RestServer.libs.bottle import route, run
import RestServer.RecupBD as bd

@route('/')
def index():
	activity, equipment, installation = bd.run()
	html = 'Voici les installations sportives du Pays de la Loire :'
	

	return html

run(host='localhost', port=8080)