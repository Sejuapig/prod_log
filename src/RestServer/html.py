def genereEnteteHtml():
	"""Function allowing you to generate the header of the html website"""
	entete=html("<!DOCTYPE html>")
	entete+=html("<html>")
	entete+=html("<head> Voici les listes des installation :")
	entete+=html("<link href=\"vue/css/menu.css\" type=\"text/css\" rel=\"stylesheet\" /> ")
	entete+=html("</head>")
	return entete

def genereBody(str):
	"""Function allowing you to generate the body of the html website"""
	body=html("<body>")
	body+=html("<form action="/hometu/etudiants/a/b/E145725x/2Annee/python/Production_logiciel/src/RestServer/" method="POST">")
	body+=html("Veuillez entrer une commune : <input id="commune" type="text" name="commune"> </br>")
	body+=html("<input type="submit" value="Envoyer"/>") 
	body+=html("</form>")
	return body
	
def generePied():
	"""Function allowing you to generate the footer of the html website"""
	pied=html("</body>")
	pied+=html("</html>")
	return pied