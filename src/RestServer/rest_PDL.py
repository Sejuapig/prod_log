from RestServer.libs.bottle import route, run
import RestServer.RecupBD as bd
import json
import cgi

@route('/')
def index():
	activity, equipment, installation, equipment_activity = bd.run()
	
	html = ("""<head> Voici les listes des installations :
			</head>
			<body>
			<form action="" method="GET">
			Entrez une commune : <input id="commune" type="text" name="commune"> </br>
			<input type="submit" value="Envoyer"/> 
			</form>
			</body>
			</html>""")

	return (html)

run(host='localhost', port=8080)