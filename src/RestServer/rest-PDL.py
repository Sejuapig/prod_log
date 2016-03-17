from libs.bottle import route, run
import RecupBD

@route('/InstallationsSportivesPDL')
def index():
    return ('Voici les installations sportives du Pays de la Loire : ')

run(host='localhost', port=8080)