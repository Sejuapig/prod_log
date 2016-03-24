def genereEnteteHtml():
	entete=html("<!DOCTYPE html>")
	entete+=html("<html>")
	entete+=html("<head> Voici les listes des installations :")
	entete+=html("<link href=\"vue/css/menu.css\" type=\"text/css\" rel=\"stylesheet\" /> ")
	entete+=html("</head>")
	return entete

def genereBody(str):
	body=html("<body>")
	body+=html("<form action="/hometu/etudiants/a/b/E149769S/2NDBBEY/Python/Production_logiciel/src/RestServer/" method="POST">")
	body+=html("Veuillez entrer une commune : <input id="commune" type="text" name="commune"> </br>")
	body+=html("<input type="submit" value="Envoyer"/>") 
	body+=html("</form>")
	return body
	
def generePied():
	pied=html("</body>")
	pied+=html("</html>")
	return pied